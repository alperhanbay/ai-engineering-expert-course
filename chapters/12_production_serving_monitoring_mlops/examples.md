# Examples: Production Serving, Monitoring, and MLOps

Reusable snippets matching `lesson.md`.

## 1. OpenTelemetry span per stage

```python
from opentelemetry import trace
tracer = trace.get_tracer("ai-service")

async def answer(req, ctx):
    with tracer.start_as_current_span("ask", attributes={"request_id": ctx.request_id,
                                                          "tenant_id": ctx.tenant_id}):
        with tracer.start_as_current_span("retrieve"):
            chunks = await retrieve(req.question, ctx)
        with tracer.start_as_current_span("generate") as gen:
            result = await generate(req, chunks)
            gen.set_attribute("output_tokens", result.output_tokens)
        return result
```

## 2. Prometheus-style metrics

```python
from prometheus_client import Counter, Histogram, Gauge

REQS = Counter("ask_requests_total", "asks", ["tenant", "status"])
LAT = Histogram("ask_latency_seconds", "latency", ["stage"])
NO_ANSWER = Counter("ask_no_answer_total", "refusals", ["tenant"])
INFLIGHT = Gauge("ask_inflight", "in-flight requests")
TOKENS = Counter("llm_tokens_total", "tokens", ["prompt_version", "kind"])  # kind=in/out
```

## 3. Quality telemetry (the AI-specific part)

```python
def record_quality(result, ctx):
    if result.answer is None:
        NO_ANSWER.labels(tenant=ctx.tenant_id).inc()
    CITATION_RATE.labels(prompt_version=result.prompt_version).observe(
        1.0 if result.citations else 0.0)
    TOKENS.labels(prompt_version=result.prompt_version, kind="out").inc(result.output_tokens)
```

## 4. SLO definitions

```md
| SLO            | Target                         | Alert when |
|----------------|--------------------------------|-----------|
| latency        | p95 /ask < 3s, p99 < 6s        | p95 > 3s for 5m |
| availability   | 99.5% non-5xx                  | error budget burn |
| quality (high) | faithfulness >= 0.95           | nightly eval < 0.95 |
| no-answer acc  | 100% on unanswerable set       | any miss |
| cost           | < $X / 1k requests             | daily budget 80% |
```

## 5. Runbook skeleton

```md
# Runbook: Hallucination Incident
Severity: high if high-risk domain.
1. CONTAIN: flip feature flag to refuse-mode (or fallback) for affected route.
2. ATTRIBUTE: query answers WHERE prompt_version=? AND completed_at in window;
   confirm the cohort and the artifact change (manifest diff).
3. ROLLBACK: deploy previous release_manifest (code + prompt + index).
4. VERIFY: nightly eval green; no-answer/faithfulness back to baseline.
5. LEARN: add the failing question to golden-vN+1 as a regression case.
```

## 6. Cohort analysis query (chapter 02 schema)

```sql
SELECT prompt_version,
       AVG((metadata->>'faithfulness')::float) AS faithfulness,
       COUNT(*) AS n
FROM answers
WHERE completed_at >= NOW() - INTERVAL '24 hours'
GROUP BY prompt_version
ORDER BY faithfulness ASC;
```

## 7. Manifest-level rollback (not just code)

```bash
# rollback restores the FULL artifact set, not only the image
PREV=$(cat releases/last_good.txt)
yq '.docker_image' releases/$PREV.yaml      # image
yq '.prompt_version' releases/$PREV.yaml    # prompt -> set active prompt
yq '.index_version' releases/$PREV.yaml     # index -> flip retrieval config
./scripts/deploy.sh --manifest releases/$PREV.yaml
```

## 8. Scheduled production eval (drift catcher)

```python
# cron nightly: run golden set against LIVE system, alert on drop with no deploy
async def nightly_eval():
    report = await run_eval(golden="golden/v3.jsonl", target="prod")
    store_eval_run(report)
    if report["high"]["faithfulness"] < 0.95 and not deployed_in_last_24h():
        alert("quality drop with no deploy -> suspect drift", report)
```

## 9. Feedback -> golden case (closing the loop)

```python
async def on_thumbs_down(request_id, reason, corrected_answer, reviewer):
    fb = await feedback.record(request_id, thumbs="down", reason=reason,
                               failure_category=categorise(reason))
    if reviewer.is_expert and corrected_answer:
        case = feedback_to_golden_case(fb, await answers.get(request_id))
        await golden.append("v_next", case)   # becomes a regression test next release
```

## 10. Graceful provider-outage degradation

```python
try:
    return await primary_llm.complete(**kw)
except ProviderError:
    if fallback_llm:
        return await fallback_llm.complete(**kw)   # chapter 11 adapter
    raise AiServiceError("model temporarily unavailable", error_code="provider_error",
                         retryable=True)            # never hang
```
