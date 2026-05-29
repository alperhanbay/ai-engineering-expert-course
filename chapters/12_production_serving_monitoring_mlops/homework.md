# Homework: Production Serving, Monitoring, and MLOps

Graded against `../../syllabus/evaluation_rubric.md`. Outputs under `my_work/`.

## Required

1. **Span-per-stage tracing.** Instrument `/ask` with OpenTelemetry so every
   request emits spans for api → retrieve → rerank → generate → guardrail →
   tool. Show a real trace from one request in `my_work/trace_example.md`.

2. **Metrics surface.** Define and instrument metrics in
   `my_work/telemetry/metrics.md`: request rate, error rate by code, p50/p95/p99
   latency overall and per stage, *plus quality signals* — no-answer rate,
   refusal rate, citation rate, feedback score, per-release eval pass rate.

3. **SLOs.** Write `my_work/slos.md` with latency, availability, quality, and
   cost SLOs and the alert thresholds that protect each.

4. **Runbooks.** Write runbooks under `my_work/runbooks/` for: hallucination,
   provider outage, latency spike, data leakage, cost spike. Each has
   containment, attribution (find the cohort/version), and rollback steps.

5. **Release manifest + rollback drill.** Enforce a release manifest in CI.
   Run a timed rollback drill ("release N has a bad prompt; restore N-1") and
   record steps + time in `my_work/rollback_drill.md`. Target MTTR < 5 min.

6. **Feedback loop.** Implement capture → categorise → promote-to-golden.
   Demonstrate one thumbs-down becoming a new golden case in
   `my_work/feedback_loop.md`.

## Stretch

7. **Scheduled production eval.** Set up the golden set to run against the live
   system nightly; show how a drop with no deploy in the window flags drift.

8. **Cost dashboard.** Build a per-tenant, per-prompt-version token + cost
   metric. Simulate a token-heavy prompt change and show the cost metric
   catching it.

9. **Drift probe.** Introduce a new document type that parses poorly; show
   which quality signal (no-answer rate, recall) detects it first.

## Acceptance

- A dashboard answers "is quality healthy right now?", not just "is it up?"
- Following a runbook localises an injected failure to the right stage.
- The rollback drill restores the full manifest (not just code) in < 5 min.
- One real feedback item becomes a golden-set regression case.
