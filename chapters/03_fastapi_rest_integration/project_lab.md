# Project Lab: FastAPI, REST, and Integration

The API contract is the product boundary between AI internals and real applications. This lab turns the chapter's projects into concrete, reviewable
deliverables. Pick one project and finish it end-to-end before starting another.
The "Acceptance Criteria" sections are the gate — not the existence of files.

## Project 1: Build an AI API with document ingestion, ask, feedback, eval, and agent endpoints.

### Scenario

Expose the service from chapter 01 as a typed HTTP API that real clients (a frontend, a CLI, another service) can consume without leaking implementation details. The contract is the product boundary — once it's public, you can't break it without coordination.

### Inputs

- the service-layer functions from chapter 01
- a Pydantic schema for each request/response body
- a fake authentication dependency that injects `tenant_id` and `role`

### Outputs / Artifacts

- endpoints: `POST /documents`, `POST /ask`, `POST /feedback`, `GET /eval/{run_id}`, `POST /agent/run`
- OpenAPI schema generated and committed (`openapi.json`)
- error contract: `{code, message, retryable, request_id}` for every non-2xx response
- a streaming `GET /ask/stream` variant that documents how citations and errors appear in the SSE stream
- `tests/api/` exercising the contract via FastAPI's TestClient

### Test Cases

- happy `POST /ask` — valid JSON in, valid JSON out, request_id in response and logs
- missing required field — 422 with the field name; no leak of stack trace
- wrong tenant — 403 with a typed error code, not 500
- long-running ingest — `POST /documents` returns 202 + job_id; `GET /jobs/{id}` reports state
- idempotency: re-POSTing the same document with the same idempotency key produces no duplicate
- streaming: first SSE event is a session id; partial answers arrive; final event includes citations

### Metrics

- OpenAPI schema validates against an external linter
- test pass rate on the contract suite (target 100%)
- p95 latency on `/ask` against fake providers under 200ms

### Failure Cases To Cover

- Error responses sometimes return text/plain and sometimes JSON
- Idempotency key is hashed but not scoped per tenant, allowing cross-tenant collisions
- Streaming endpoint emits guardrail-violating tokens before the guardrail runs
- OpenAPI lies (the live response doesn't match the declared schema)

### Acceptance Criteria

- every endpoint has a documented error contract and at least one negative-path test
- OpenAPI is committed and a CI step fails if it drifts from the implementation
- the streaming endpoint has an explicit cancellation and error-event spec

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

## Project 2: Design a streaming answer endpoint and document citation handling for partial output.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `REST`, `OpenAPI`, `request schema`, `response schema`, `error contract`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `REST`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_2_implementation/`
- `my_work/project_2_report.md` summarising results with numbers
- `my_work/project_2_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `REST`
- an edge case driven by the failure mode of `OpenAPI`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `REST` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- AI endpoints often hide all failures behind HTTP 500.
- Long document indexing jobs do not fit a single synchronous request.
- Clients should not depend on a specific model, vector database, or orchestration framework.
- silent degradation of `idempotency` after a config change goes unnoticed

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

## Project 3: Create a background indexing job API with job states and failure recovery.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `REST`, `OpenAPI`, `request schema`, `response schema`, `error contract`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `REST`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_3_implementation/`
- `my_work/project_3_report.md` summarising results with numbers
- `my_work/project_3_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `REST`
- an edge case driven by the failure mode of `OpenAPI`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `REST` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- AI endpoints often hide all failures behind HTTP 500.
- Long document indexing jobs do not fit a single synchronous request.
- Clients should not depend on a specific model, vector database, or orchestration framework.
- silent degradation of `idempotency` after a config change goes unnoticed

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

[1] FastAPI first steps: https://fastapi.tiangolo.com/tutorial/first-steps/
[2] FastAPI request body: https://fastapi.tiangolo.com/tutorial/body/
[3] FastAPI error handling: https://fastapi.tiangolo.com/tutorial/handling-errors/
[4] FastAPI testing: https://fastapi.tiangolo.com/tutorial/testing/
[5] OpenAPI Specification: https://spec.openapis.org/oas/latest.html
