# Examples: Optimization, Caching, Quantization, and Serving

Reusable snippets matching `lesson.md`.

## 1. Latency budget from traces

```python
# aggregate span durations per stage from your tracing backend
budget = {
    "api":       {"p50": 3,   "p95": 8},
    "retrieve":  {"p50": 25,  "p95": 60},
    "rerank":    {"p50": 40,  "p95": 120},
    "generate":  {"p50": 1200,"p95": 3800},   # dominant -> optimize here
    "guardrail": {"p50": 15,  "p95": 40},
}
# target: cut generate p95 3800 -> 2500 (shorter answers / smaller model / streaming UX)
```

## 2. Tenant-safe cache key (the critical pattern)

```python
import hashlib, json

def cache_key(tenant_id, allowed_levels, question, prompt_version, index_version) -> str:
    payload = json.dumps({
        "t": tenant_id,
        "acl": sorted(allowed_levels),
        "q": question,
        "pv": prompt_version,
        "iv": index_version,
    }, sort_keys=True)
    return "ans:" + hashlib.sha256(payload.encode()).hexdigest()
# Omitting tenant_id here is a cross-tenant data leak. Omitting versions serves stale answers.
```

## 3. Cache-aside with TTL

```python
async def cached_answer(req, ctx) -> AskResponse:
    key = cache_key(ctx.tenant_id, ctx.allowed_levels, req.question,
                    PROMPT_VERSION, INDEX_VERSION)
    if (hit := await redis.get(key)) is not None:
        CACHE_HITS.inc()
        return AskResponse.model_validate_json(hit)
    result = await answer(req, ctx)
    await redis.set(key, result.model_dump_json(), ex=3600)   # 1h TTL
    return result
```

## 4. Cross-tenant cache test

```python
@pytest.mark.asyncio
async def test_cache_no_cross_tenant(cache):
    a = await cached_answer(Req("deadline?"), ctx(tenant="A"))
    b = await cached_answer(Req("deadline?"), ctx(tenant="B"))
    # different tenants -> different keys -> B must not get A's cached object
    assert a.request_id != b.request_id or a.answer != b.answer or keys_differ("A", "B")
```

## 5. Stable-prefix prompt ordering (maximises cache + attention)

```python
# stable first (cacheable prefix), variable last
prompt = [
    {"role": "system", "content": SYSTEM_PROMPT},        # stable -> cached
    {"role": "system", "content": OUTPUT_SCHEMA},        # stable -> cached
    {"role": "user", "content": render_context(chunks)}, # variable
    {"role": "user", "content": question},               # variable
]
```

## 6. Offline batch embeddings (batch hard)

```python
async def embed_corpus(chunks, batch_size=256):
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        vecs = await embedder.embed_batch([c.text for c in batch])  # one API call per batch
        await store.upsert(batch, vecs)
# offline path: maximise throughput, per-item latency irrelevant
```

## 7. Quantization before/after eval (per risk level)

```python
async def quant_report(golden):
    full = await run_eval(model="llama-3-8b-fp16", golden=golden)
    quant = await run_eval(model="llama-3-8b-q4", golden=golden)
    return {risk: {
        "faithfulness_delta": quant[risk]["faithfulness"] - full[risk]["faithfulness"],
        "latency_delta_ms": full[risk]["p95_ms"] - quant[risk]["p95_ms"],
    } for risk in ("low", "medium", "high")}
# REJECT if high-risk faithfulness_delta is materially negative, however good the speedup.
```

## 8. Serving decision matrix (markdown)

```md
| Factor       | Hosted API | vLLM      | TGI       | Triton |
|--------------|-----------|-----------|-----------|--------|
| ops burden   | none      | medium    | medium    | high   |
| $/1k req     | 0.80 (measured) | 0.18 (measured @ our volume) | 0.20 | 0.19 |
| p95 (ours)   | 3.8s      | 4.1s      | 4.3s      | 4.0s   |
| privacy      | low       | high      | high      | high   |
| pick if      | low volume| high volume + GPU ops | HF stack | multi-model + experts |
```

## 9. Streaming with guardrail delay (safety-preserving)

```python
async def safe_stream(gen, guardrail, lookahead=12):
    buffer = []
    async for tok in gen:
        buffer.append(tok)
        if len(buffer) > lookahead:
            chunk = buffer.pop(0)
            if not await guardrail.ok(chunk):        # check before user sees it
                yield {"event": "error", "code": "unsafe_output"}; return
            yield {"event": "token", "text": chunk}
    for tok in buffer:                                # flush remaining through guardrail
        if await guardrail.ok(tok):
            yield {"event": "token", "text": tok}
```

## 10. Optimization decision record

```md
# Decision: response caching for /ask
Baseline: p95 3.9s, $0.80/1k, faithfulness(high) 0.96
+cache (1h TTL, tenant-keyed): p95 hit 40ms / miss 3.9s; hit rate 34%;
        $0.53/1k; faithfulness(high) 0.96 (unchanged)
Decision: ADOPT. 34% hits cut cost 34%; no quality change (cache stores exact answers).
Risk handled: key includes tenant_id + prompt_version + index_version; cross-tenant test passes.
```
