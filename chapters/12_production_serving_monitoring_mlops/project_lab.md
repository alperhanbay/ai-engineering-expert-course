# Project Lab: Production Serving, Monitoring, and MLOps

Production AI is a lifecycle of observability, versioning, feedback, incident response, and continuous evaluation. This lab turns the chapter's projects into concrete, reviewable
deliverables. Pick one project and finish it end-to-end before starting another.
The "Acceptance Criteria" sections are the gate — not the existence of files.

## Project 1: Design observability for API, retrieval, generation, agent tools, evaluation, cost, and security.

### Scenario

The capstone has a working `/ask` endpoint. Now make it operable. You need observability that would let an on-call engineer answer 'is quality healthy right now?' — not just 'is the API up?' — plus a release manifest that ties every artifact (code, prompt, model, index, eval) to a version.

### Inputs

- the current RAG service (API + retriever + generator)
- the golden eval set from chapter 09 (or a stand-in 30-case set)
- a tracing backend (e.g. OpenTelemetry collector + any UI, or MLflow tracing) running locally
- a metrics scrape target (Prometheus or pushgateway) plus a dashboard tool

### Outputs / Artifacts

- `telemetry/spans.md` — list of spans emitted per `/ask` request: api, retrieve, rerank, generate, guardrail, tool, log
- `telemetry/metrics.md` — list of metrics with name, type, labels, alert threshold
- `runbooks/{hallucination,latency_spike,provider_outage,data_leakage,cost_spike}.md`
- `release_manifest.yaml` — schema: code_sha, prompt_id, model_id, embedding_model_id, index_version, eval_report_id
- `dashboards/overview.json` — exported dashboard with quality, latency, error, cost panels

### Test Cases

- induce a latency spike in retrieval — alert fires and the runbook leads to the right span
- swap to a worse prompt — golden-set quality drops; the metrics dashboard surfaces it before users complain
- bump the embedding model and forget to re-index — release manifest mismatch should block the release
- rollback drill: revert to last manifest in under 5 minutes

### Metrics

- request rate, error rate, p50/p95/p99 latency overall and per stage
- golden-set pass rate scored continuously (or per-deploy), with trend
- cost per 1k requests (estimated from token counts and provider prices)
- mean time to detect (MTTD) and mean time to rollback (MTTR) for the four drill scenarios

### Failure Cases To Cover

- Only the API is observable; retrieval and generation are black boxes
- An alert fires but the runbook says 'check the dashboard' with no specifics
- Code rollback restores the previous service but leaves the bad prompt active
- Cost dashboard double-counts cached prompt tokens
- Traces include raw user input that should be redacted under the PII policy

### Acceptance Criteria

- every span in the pipeline appears in at least one trace from a real `/ask` request
- the four drill scenarios are run and timed; MTTR for rollback is under 5 minutes
- the release manifest is enforced in CI (a missing field blocks deploy)
- runbooks are linked from the alerts that would page on-call

### Deliverables Layout

```
my_work/
  project_1_scope.md            # one paragraph + concept list
  project_1_implementation/      # code or design doc
  project_1_report.md            # results, numbers, plots
  project_1_decision_record.md   # alternatives + chosen approach + why
  project_1_tests/               # the test cases above, runnable or scripted
```

### Expected README Section

In your portfolio README, this project should appear under "Projects" with:
a one-sentence summary, the headline metric you measured, the main tradeoff
you made, and a link to the decision record. Avoid screenshots-only entries.

## Project 2: Write incident runbooks for hallucination, provider outage, latency spike, data leakage, and cost spike.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `observability`, `metric`, `trace`, `log`, `SLO`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `observability`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_2_implementation/`
- `my_work/project_2_report.md` summarising results with numbers
- `my_work/project_2_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `observability`
- an edge case driven by the failure mode of `metric`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `observability` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- AI quality can regress even when API uptime looks healthy.
- A bad release may come from prompt, model, index, data, or tool schema changes.
- Feedback is wasted unless it becomes labeled data and regression coverage.
- silent degradation of `drift` after a config change goes unnoticed

### Acceptance Criteria

- a reviewer can run or read the artifact and understand what was built without asking you
- every numeric claim is backed by a test, eval result, or measured run logged in the report
- at least one known limitation is named honestly (not a humblebrag)
- the artifact is wired into the capstone, not orphaned in `my_work/`

### Deliverables Layout

```
my_work/
  project_2_scope.md            # one paragraph + concept list
  project_2_implementation/      # code or design doc
  project_2_report.md            # results, numbers, plots
  project_2_decision_record.md   # alternatives + chosen approach + why
  project_2_tests/               # the test cases above, runnable or scripted
```

### Expected README Section

In your portfolio README, this project should appear under "Projects" with:
a one-sentence summary, the headline metric you measured, the main tradeoff
you made, and a link to the decision record. Avoid screenshots-only entries.

## Project 3: Build a version registry that connects releases to eval results and rollback artifacts.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `observability`, `metric`, `trace`, `log`, `SLO`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `observability`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_3_implementation/`
- `my_work/project_3_report.md` summarising results with numbers
- `my_work/project_3_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `observability`
- an edge case driven by the failure mode of `metric`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `observability` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- AI quality can regress even when API uptime looks healthy.
- A bad release may come from prompt, model, index, data, or tool schema changes.
- Feedback is wasted unless it becomes labeled data and regression coverage.
- silent degradation of `drift` after a config change goes unnoticed

### Acceptance Criteria

- a reviewer can run or read the artifact and understand what was built without asking you
- every numeric claim is backed by a test, eval result, or measured run logged in the report
- at least one known limitation is named honestly (not a humblebrag)
- the artifact is wired into the capstone, not orphaned in `my_work/`

### Deliverables Layout

```
my_work/
  project_3_scope.md            # one paragraph + concept list
  project_3_implementation/      # code or design doc
  project_3_report.md            # results, numbers, plots
  project_3_decision_record.md   # alternatives + chosen approach + why
  project_3_tests/               # the test cases above, runnable or scripted
```

### Expected README Section

In your portfolio README, this project should appear under "Projects" with:
a one-sentence summary, the headline metric you measured, the main tradeoff
you made, and a link to the decision record. Avoid screenshots-only entries.

## Review Rubric

| Dimension | Evidence that passes |
| --- | --- |
| Specificity | scenario, inputs, and outputs match what the artifact actually does |
| Measurement | metrics are numeric, named, and reproducible from the repo |
| Failure handling | at least three failure cases are exercised in tests |
| Tradeoff honesty | decision record names alternatives and a measured reason |
| Source backing | numbered references support every external claim |

## References

[1] MLflow tracking: https://www.mlflow.org/docs/latest/ml/tracking
[2] MLflow GenAI eval and monitoring: https://www.mlflow.org/docs/latest/genai/eval-monitor
[3] MLflow tracing: https://mlflow.org/docs/latest/genai/tracing/
[4] OpenTelemetry documentation: https://opentelemetry.io/docs/
[5] Prometheus documentation: https://prometheus.io/docs/
[6] Grafana documentation: https://grafana.com/docs/
