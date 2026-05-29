# Dictionary: Production Serving, Monitoring, and MLOps

Use this dictionary at the end of the chapter. Add your own examples in `my_work/dictionary_notes.md`.

| Term | Working Definition | Why It Matters | Common Failure Mode | Mastery Check |
| --- | --- | --- | --- | --- |
| `observability` | The ability to understand system behavior through logs, metrics, and traces. | AI failures require visibility into retrieval, generation, tools, and safety checks. | Only final answers are logged, so failures cannot be traced. | Capture spans and metrics for every major pipeline stage. |
| `metric` | A numeric measurement of system behavior or quality. | Metrics turn performance and quality into trackable signals. | The team debates quality without data. | Define latency, error, retrieval, generation, safety, and cost metrics. |
| `trace` | A recorded execution path with spans, inputs, outputs, and timings. | Traces reveal latency, state transitions, tool calls, and failures. | A bad answer cannot be debugged because intermediate retrieval is missing. | Trace API, retrieval, reranking, LLM, guardrail, and tool spans. |
| `log` | A recorded event emitted by a system. | Logs support debugging, audit, analytics, and incident response. | Logs include sensitive raw prompts without policy approval. | Use structured logs and apply data minimization. |
| `SLO` | Service Level Objective, a target for reliability or performance. | SLOs align engineering work with user expectations. | Latency is optimized without a clear target. | Set p95 latency, uptime, and quality objectives where appropriate. |
| `incident` | An event where system behavior harms reliability, safety, cost, or users. | AI incidents can involve quality and policy failures, not only outages. | A hallucinated legal answer is treated as a normal bug. | Define severity, containment, rollback, and postmortem process. |
| `rollback` | Returning a system or artifact to a previous known-good version. | AI rollback may involve code, prompt, model, index, or data. | Code is rolled back but the bad prompt remains active. | Track release manifests for all AI artifacts. |
| `feedback loop` | A process that turns user or expert feedback into improvements and regression tests. | It keeps production learning connected to development. | Feedback is stored but never labeled or reviewed. | Categorize feedback and promote cases into eval datasets. |
| `drift` | A change in data, user behavior, or model behavior over time. | Drift can reduce quality without any code change. | New document types lower retrieval quality silently. | Monitor distributions, failure rates, and eval performance over time. |

<!-- HAND-AUTHORED: do not regenerate -->
## Extended Glossary

Additional terms used in this chapter, each with a concise definition and an authoritative source.

- **Observability** — understanding system behaviour from logs, metrics, and traces. Source: [OpenTelemetry](https://opentelemetry.io/docs/)
- **Span / trace** — a timed unit of work / the connected path of spans for one request. Source: [OTel traces](https://opentelemetry.io/docs/concepts/signals/traces/)
- **Metric (counter/gauge/histogram)** — numeric measurements over time. Source: [Prometheus metric types](https://prometheus.io/docs/concepts/metric_types/)
- **SLI / SLO** — service level indicator / objective. Source: [SRE Book — SLOs](https://sre.google/sre-book/service-level-objectives/)
- **Error budget** — the allowed unreliability under an SLO. Source: [SRE Book — error budgets](https://sre.google/sre-book/embracing-risk/)
- **Incident / runbook** — a harmful event / the documented response procedure. Source: [SRE Book — managing incidents](https://sre.google/sre-book/managing-incidents/)
- **Release manifest** — record tying a release to code/prompt/model/index/eval for complete rollback. Source: [MLflow Model Registry](https://mlflow.org/docs/latest/model-registry.html)
- **Drift** — quality degradation with no code change (input/corpus/model/world). Source: [Google, Rules of ML](https://developers.google.com/machine-learning/guides/rules-of-ml)
- **Feedback loop** — turning production feedback into labels/regression cases. Source: [MLflow eval & monitor](https://www.mlflow.org/docs/latest/genai/eval-monitor)
- **MTTD / MTTR** — mean time to detect / to recover. Source: [SRE Book](https://sre.google/sre-book/)

## Dictionary Assignment

For each term:

1. Write a one-sentence definition in your own words.
2. Write a concrete example from your capstone (or planned capstone).
3. Write one failure mode you would test against.
4. Write one metric, test, or review check that would catch the failure.
5. Link one source from `references_numbered.md`.

## References

[1] MLflow tracking: https://www.mlflow.org/docs/latest/ml/tracking
[2] MLflow GenAI eval and monitoring: https://www.mlflow.org/docs/latest/genai/eval-monitor
[3] MLflow tracing: https://mlflow.org/docs/latest/genai/tracing/
[4] OpenTelemetry documentation: https://opentelemetry.io/docs/
[5] Prometheus documentation: https://prometheus.io/docs/
[6] Grafana documentation: https://grafana.com/docs/
