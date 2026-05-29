# Homework: Optimization, Caching, Quantization, and Serving

Graded against `../../syllabus/evaluation_rubric.md`. Outputs under `my_work/`.

## Required

1. **Latency budget.** Using your chapter-12 traces, decompose `/ask` p50/p95
   latency by stage in `my_work/latency_budget.md`. Set a target per stage and
   identify the biggest gap. Confirm (almost certainly) that generation
   dominates.

2. **Cache design.** Write `my_work/cache_design.md` specifying what you cache
   (prompt prefix? embeddings? final answer?), the key format **including
   tenant_id, prompt_version, index_version**, TTLs, and invalidation. State
   the cross-tenant leak risk and its mitigation.

3. **Cross-tenant cache test.** Implement a response cache and write a test
   proving tenant A can never receive tenant B's cached answer. This is the
   chapter's headline safety test.

4. **Warm vs cold measurement.** Measure latency for a cache-miss vs a
   cache-hit request. Report the delta and the hit rate on a representative
   workload in `my_work/cache_results.md`.

5. **Serving decision matrix.** Fill `my_work/serving_matrix.md` comparing
   hosted API vs vLLM vs TGI vs Triton on quality, p95, throughput, $/1k, and
   ops burden — with numbers from your measurements where possible, and an
   honest ops-hours estimate for self-hosting.

6. **Optimization decision record.** Pick one optimization (caching, smaller
   model for easy cases, or context compression). Record before/after cost,
   latency, AND quality (golden set, per risk level) in
   `my_work/optimization_decision.md`. Keep it only if quality held.

## Stretch

7. **Quantization eval.** If self-hosting an open model, run a before/after
   golden-set eval (per risk level) on a quantized vs full-precision model.
   Report where (if anywhere) quality degraded.

8. **Streaming + guardrail.** Show how your streaming endpoint handles a
   guardrail decision without having already shown unsafe tokens (delay or
   per-chunk check).

9. **KV-cache memory probe.** On a self-hosted setup, measure serving memory
   vs prompt length at fixed concurrency; find the length/concurrency point
   that risks OOM.

## Acceptance

- The latency budget identifies the dominant stage with numbers.
- The cross-tenant cache test passes; the cache key includes tenant + versions.
- Every adopted optimization has before/after cost, latency, AND quality.
- The serving matrix uses your own numbers, not vendor claims.
