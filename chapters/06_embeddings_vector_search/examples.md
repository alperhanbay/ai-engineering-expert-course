# Examples: Embeddings and Vector Search

Reusable snippets matching `lesson.md`.

## 1. Verify normalisation, pick the metric

```python
import numpy as np

def is_normalised(vec) -> bool:
    return abs(np.linalg.norm(vec) - 1.0) < 1e-3

v = embed("normalisation check")
assert is_normalised(v), "model output not unit-length; cosine != dot, set metric accordingly"
# Normalised -> cosine and dot agree. Use the metric the model card specifies.
```

## 2. Recall@k and MRR

```python
def recall_at_k(retrieved_ids: list[str], relevant_ids: set[str], k: int) -> float:
    top = retrieved_ids[:k]
    return 1.0 if any(r in relevant_ids for r in top) else 0.0

def reciprocal_rank(retrieved_ids: list[str], relevant_ids: set[str]) -> float:
    for i, rid in enumerate(retrieved_ids, 1):
        if rid in relevant_ids:
            return 1.0 / i
    return 0.0

# Aggregate over the labelled set:
recall5 = sum(recall_at_k(r, rel, 5) for r, rel in cases) / len(cases)
mrr = sum(reciprocal_rank(r, rel) for r, rel in cases) / len(cases)
```

## 3. Filtered (pre-filter) vector search — Qdrant style

```python
results = await client.search(
    collection_name="chunks",
    query_vector=query_vec,
    query_filter={
        "must": [
            {"key": "tenant_id", "match": {"value": tenant_id}},
            {"key": "access_level", "match": {"any": allowed_levels}},
        ]
    },
    limit=top_k,
)
# Authorisation predicate is applied DURING search, not after.
```

## 4. pgvector retrieval with filter

```sql
SELECT c.id, c.text, e.vector <=> $1 AS distance
FROM embeddings e
JOIN chunks c ON c.id = e.chunk_id
WHERE c.tenant_id = $2
  AND e.index_version = $3
  AND c.access_level = ANY($4)
ORDER BY e.vector <=> $1
LIMIT $5;
```

## 5. Reciprocal Rank Fusion (hybrid)

```python
def rrf(dense_ranking: list[str], lexical_ranking: list[str], k: int = 60) -> list[str]:
    scores: dict[str, float] = {}
    for ranking in (dense_ranking, lexical_ranking):
        for rank, doc_id in enumerate(ranking, 1):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank)
    return sorted(scores, key=scores.get, reverse=True)
```

## 6. Cross-tenant leak test

```python
import pytest

@pytest.mark.asyncio
async def test_no_cross_tenant_retrieval(store, seed_two_tenants):
    q = embed("anything that exists in tenant B")
    results = await store.search(query_vector=q, tenant_id="tenant_A", limit=20)
    assert all(r.payload["tenant_id"] == "tenant_A" for r in results)
```

## 7. HNSW ef_search sweep

```python
async def sweep_ef(store, cases, ef_values=(16, 32, 64, 128, 256)):
    rows = []
    for ef in ef_values:
        await store.set_search_params(ef_search=ef)
        recalls, lats = [], []
        for q, rel in cases:
            t0 = time.perf_counter()
            res = await store.search(q.vector, limit=5)
            lats.append((time.perf_counter() - t0) * 1000)
            recalls.append(recall_at_k([r.id for r in res], rel, 5))
        rows.append({"ef": ef, "recall@5": mean(recalls), "p95_ms": p95(lats)})
    return rows   # find the knee: smallest ef where recall plateaus
```

## 8. Dual-index migration cutover (config flip)

```python
# Retrieval reads the active index version from config, not a hard-coded name.
async def retrieve(query: str, tenant_id: str, settings: Settings):
    vec = await embed(query, model=settings.embedding_model)
    return await store.search(
        collection=f"chunks_{settings.index_version}",   # 'v17' -> 'v18' is a config change
        query_vector=vec,
        query_filter={"must": [{"key": "tenant_id", "match": {"value": tenant_id}}]},
        limit=settings.top_k,
    )
```

## 9. Reconciliation: SQL vs vector store

```sql
-- chunks that exist in SQL but may be missing/extra in the vector store
SELECT c.id
FROM chunks c
LEFT JOIN embeddings e ON e.chunk_id = c.id AND e.index_version = 'v17'
WHERE c.tenant_id = $1 AND e.id IS NULL;
```

## 10. Benchmark harness skeleton

```python
async def benchmark(cases, configs):
    results = []
    for name, retrieve in configs.items():   # {"dense": fn, "hybrid": fn}
        recalls1, recalls5, mrrs, lats = [], [], [], []
        for q, rel in cases:
            t0 = time.perf_counter()
            ids = [r.id for r in await retrieve(q)]
            lats.append((time.perf_counter() - t0) * 1000)
            recalls1.append(recall_at_k(ids, rel, 1))
            recalls5.append(recall_at_k(ids, rel, 5))
            mrrs.append(reciprocal_rank(ids, rel))
        results.append({
            "config": name,
            "recall@1": mean(recalls1), "recall@5": mean(recalls5),
            "mrr": mean(mrrs), "p95_ms": p95(lats),
        })
    return results
```
