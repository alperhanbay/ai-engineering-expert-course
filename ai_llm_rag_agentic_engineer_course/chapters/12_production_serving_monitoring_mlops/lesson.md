# Lesson: Production Serving, Monitoring, and MLOps

## 1. What Production Means

Production AI means users depend on the system. You must manage:

- uptime;
- latency;
- correctness;
- cost;
- privacy;
- security;
- model/provider failures;
- changing data;
- quality regressions.

Production readiness is not a checkbox. It is an operating model.

## 2. Observability Layers

| Layer | Signals |
| --- | --- |
| API | status codes, latency, request rate |
| retrieval | top-k scores, recall estimates, empty retrievals |
| generation | tokens, latency, model errors, refusals |
| agent | tool calls, loops, approvals, failures |
| evaluation | scores, regressions, failed cases |
| feedback | ratings, human review, complaints |
| security | blocked requests, access denials, PII events |

## 3. Logging

Logs should be structured and queryable.

Minimum fields:

- timestamp;
- request ID;
- user ID or anonymized ID;
- tenant ID;
- endpoint;
- model version;
- prompt version;
- index version;
- latency;
- error type;
- retrieved chunk IDs;
- safety flags.

Do not log sensitive content unless policy allows it.

## 4. Tracing

Traces show a full request path:

```text
API request
  -> auth
  -> query rewrite
  -> vector search
  -> reranking
  -> LLM call
  -> guardrail validation
  -> response
```

Tracing is essential for latency and failure debugging.

## 5. Metrics

Important metrics:

- p50/p95/p99 latency;
- request rate;
- error rate;
- timeout rate;
- token usage;
- cost per request;
- retrieval empty rate;
- no-answer rate;
- faithfulness score;
- human rejection rate;
- tool failure rate.

## 6. Versioning

Version:

- code;
- model;
- prompt;
- embedding model;
- index;
- dataset;
- evaluator;
- tool schema.

AI regression can come from any of these.

## 7. Feedback Loop

Feedback should flow into:

```text
user/human feedback
  -> labeling
  -> failure categories
  -> golden dataset
  -> evaluation suite
  -> system improvement
```

Do not let feedback sit unused in a database.

## 8. Incident Response

Common AI incidents:

- hallucinated answer in high-risk domain;
- cross-tenant data leakage;
- model provider outage;
- cost spike;
- latency spike;
- retrieval index stale;
- prompt regression;
- unsafe agent action.

Incident response should include:

- detection;
- severity;
- containment;
- rollback;
- root cause analysis;
- postmortem;
- prevention item.

## 9. MLOps vs LLMOps

Traditional MLOps focuses on datasets, model training, deployment, monitoring, and drift. LLMOps/GenAIOps extends this with:

- prompt management;
- retrieval management;
- evaluation datasets;
- traces;
- tool calls;
- human feedback;
- safety policies;
- cost monitoring.

## 10. Key Takeaway

Production AI is a lifecycle. If you cannot observe, evaluate, and roll back your system, you do not control it.
## Numbered References

[1] MLflow tracking: https://www.mlflow.org/docs/latest/ml/tracking
[2] MLflow GenAI eval and monitoring: https://www.mlflow.org/docs/latest/genai/eval-monitor
[3] MLflow tracing: https://mlflow.org/docs/latest/genai/tracing/
[4] OpenTelemetry documentation: https://opentelemetry.io/docs/
[5] Prometheus documentation: https://prometheus.io/docs/
[6] Grafana documentation: https://grafana.com/docs/
