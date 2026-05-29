# Examples: Advanced RAG, Retrieval, and Reranking

Reusable snippets matching `lesson.md`.

## 1. Two-stage retrieve + cross-encoder rerank

```python
async def retrieve_and_rerank(query: str, ctx, n: int = 50, k: int = 5):
    candidates = await store.search(embed(query), tenant_id=ctx.tenant_id, limit=n)
    scores = await reranker.score(query, [c.text for c in candidates])
    ranked = [c for c, _ in sorted(zip(candidates, scores),
                                   key=lambda x: x[1], reverse=True)]
    return ranked[:k]
```

## 2. Confidence-aware rerank policy

```python
CONFIDENCE_GAP = 0.08   # tuned on the eval set

def needs_rerank(candidates) -> bool:
    if len(candidates) < 2:
        return False
    return (candidates[0].score - candidates[1].score) < CONFIDENCE_GAP

async def smart_retrieve(query, ctx, n=50, k=5):
    cands = await store.search(embed(query), tenant_id=ctx.tenant_id, limit=n)
    if needs_rerank(cands):
        scores = await reranker.score(query, [c.text for c in cands])
        cands = [c for c, _ in sorted(zip(cands, scores), key=lambda x: x[1], reverse=True)]
    return cands[:k]
```

## 3. Multi-query expansion

```python
async def multi_query_retrieve(query: str, ctx, k=5):
    variants = await llm.generate_variants(query, n=3)   # synonyms / perspectives
    seen, fused = {}, []
    for q in [query, *variants]:
        for rank, c in enumerate(await store.search(embed(q), tenant_id=ctx.tenant_id, limit=10), 1):
            seen[c.id] = seen.get(c.id, 0) + 1 / (60 + rank)   # RRF across variants
    return sorted(seen, key=seen.get, reverse=True)[:k]
```

## 4. Hybrid via RRF (dense + BM25)

```python
def rrf(rankings: list[list[str]], k: int = 60) -> list[str]:
    scores: dict[str, float] = {}
    for ranking in rankings:
        for rank, doc_id in enumerate(ranking, 1):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank)
    return sorted(scores, key=scores.get, reverse=True)

dense = [c.id for c in await store.search(embed(q), limit=20)]
lexical = [c.id for c in await bm25.search(q, limit=20)]
hybrid = rrf([dense, lexical])[:5]
```

## 5. Query router (LLM classifier)

```python
ROUTES = ["rag", "analytics", "tool", "refuse"]

async def route(query: str) -> str:
    label = await llm.classify(query, labels=ROUTES, temperature=0)
    return label if label in ROUTES else "refuse"   # unknown -> safe default

async def handle(query, ctx):
    match await route(query):
        case "rag":       return await rag_answer(query, ctx)
        case "analytics": return await sql_analytics(query, ctx)
        case "tool":      return await tool_workflow(query, ctx)
        case _:           return refuse(query, ctx)
```

## 6. Parent-child retrieval

```python
async def parent_child_retrieve(query, ctx, k=5):
    children = await store.search(embed(query), tenant_id=ctx.tenant_id,
                                  filter={"granularity": "child"}, limit=k)
    parent_ids = {c.metadata["parent_id"] for c in children}
    return await chunks.get_many(parent_ids, tenant_id=ctx.tenant_id)  # pass parents to gen
```

## 7. Experiment harness (one variable at a time)

```python
CONFIGS = {
    "baseline":  lambda q, ctx: dense_retrieve(q, ctx, k=5),
    "hybrid":    lambda q, ctx: hybrid_retrieve(q, ctx, k=5),
    "rerank":    lambda q, ctx: retrieve_and_rerank(q, ctx, n=50, k=5),
}

async def run_experiment(cases, golden):
    rows = []
    for name, retrieve in CONFIGS.items():
        m = await evaluate(retrieve, cases, golden)   # recall@5, ndcg@5, faithfulness, cite, p95
        rows.append({"config": name, **m})
    return rows
```

## 8. Routing confusion matrix

```python
from collections import Counter

def confusion(eval_cases, route_fn) -> dict:
    cm = Counter()
    for q, true_route in eval_cases:
        cm[(true_route, route_fn(q))] += 1
    return dict(cm)   # {(true, predicted): count}; off-diagonal = mis-routes
```

## 9. Faithfulness check alongside ranking (the key guardrail)

```python
async def rerank_report(cases, golden):
    base = await evaluate(dense_retrieve, cases, golden)
    rer  = await evaluate(retrieve_and_rerank, cases, golden)
    return {
        "ndcg_delta": rer["ndcg@5"] - base["ndcg@5"],
        "faithfulness_delta": rer["faithfulness"] - base["faithfulness"],  # MUST not drop
        "p95_delta_ms": rer["p95_ms"] - base["p95_ms"],
    }
# A positive ndcg_delta with a negative faithfulness_delta means REJECT the reranker.
```

## 10. Decision record template

```md
# Decision: adopt cross-encoder reranking?

Baseline: dense, k=5 -> recall@5 0.78, ndcg@5 0.71, faithfulness 0.88, p95 1.4s
+rerank (n=50): recall@5 0.78, ndcg@5 0.86, faithfulness 0.90, p95 2.1s
Decision: ADOPT, but confidence-aware (rerank ~30% of queries).
Reason: +0.15 ndcg AND +0.02 faithfulness; +0.7s p95 only on reranked queries.
Rejected: multi-query (recall@5 +0.01, within noise; +0.9s p95). Not worth it.
```
