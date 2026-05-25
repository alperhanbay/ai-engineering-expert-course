# Project Lab: FastAPI, REST, and Integration

The API contract is the product boundary between AI internals and real applications. This lab turns the chapter's projects into concrete, reviewable
deliverables. Pick one project and finish it end-to-end before starting another.
The "Acceptance Criteria" sections are the gate — not the existence of files.

## Project 1: Build an AI API with document ingestion, ask, feedback, eval, and agent endpoints.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `REST`, `OpenAPI`, `request schema`, `response schema`, `error contract`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `REST`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_1_implementation/`
- `my_work/project_1_report.md` summarising results with numbers
- `my_work/project_1_decision_record.md` for the main tradeoff

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
