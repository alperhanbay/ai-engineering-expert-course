# Project Lab: Python Backend Foundations

Production AI work requires maintainable Python services, not notebook-only scripts. This lab turns the chapter's projects into concrete, reviewable
deliverables. Pick one project and finish it end-to-end before starting another.
The "Acceptance Criteria" sections are the gate — not the existence of files.

## Project 1: Build a typed AI service skeleton with fake LLM, fake retriever, and tests.

### Scenario

Stand up the Python service skeleton the rest of the course will plug into. The goal isn't a framework demo; it's an inspectable structure with provider adapters, a service layer, and tests that can run without any real model or vector database.

### Inputs

- Python 3.11+ project with `pyproject.toml`, pinned dependencies, and a virtual env
- a tiny in-repo corpus (3 short markdown files) used as 'documents'
- fake/stub implementations of: LLM provider, embedding provider, vector store, document repo

### Outputs / Artifacts

- package layout: `src/<pkg>/{api,services,providers,repositories,models,config,logging}/`
- Protocol or ABC for each provider so a fake can be swapped in for tests
- service-layer function `answer(question, tenant_id) -> AnswerDTO` that uses the providers
- `tests/` covering: schema validation, service happy path, missing-tenant error, provider failure
- structured logging (JSON) including request_id, tenant_id, model_id, prompt_hash, latency_ms

### Test Cases

- happy path with fake providers — returns a valid AnswerDTO
- invalid request (missing tenant_id) — fails validation with a 4xx-style error contract
- provider raises — service returns a typed error, logs include the cause
- concurrent calls — request_id appears unique per call in logs

### Metrics

- pytest pass rate (target 100% on the seed suite)
- mypy/pyright clean on the public service interface
- test runtime under 5 seconds (no real network calls)

### Failure Cases To Cover

- Provider call buried inside an API route — service is untestable without HTTP
- Errors are caught and turned into HTTP 500 with no detail in logs
- Logging mixes free-text and JSON, breaking log parsers
- A test passes because it accidentally hits a real provider via leaked env vars

### Acceptance Criteria

- the service can be exercised by tests without any network call
- swapping a real provider in is a config change, not a code change
- structured logs are parseable and include the required fields
- the package is importable as `from <pkg>.services import answer` with no relative-path tricks

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

## Project 2: Create a provider adapter interface for LLM, embedding, and vector store calls.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `package layout`, `type hints`, `Pydantic`, `service layer`, `repository`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `package layout`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_2_implementation/`
- `my_work/project_2_report.md` summarising results with numbers
- `my_work/project_2_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `package layout`
- an edge case driven by the failure mode of `type hints`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `package layout` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Model provider logic often leaks into routes and makes systems hard to test.
- Untyped request and response objects make downstream failures harder to debug.
- Notebook prototypes usually lack error contracts, dependency boundaries, and logs.
- silent degradation of `structured logging` after a config change goes unnoticed

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

## Project 3: Implement structured logging with request IDs and model/prompt/index metadata.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `package layout`, `type hints`, `Pydantic`, `service layer`, `repository`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `package layout`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_3_implementation/`
- `my_work/project_3_report.md` summarising results with numbers
- `my_work/project_3_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `package layout`
- an edge case driven by the failure mode of `type hints`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `package layout` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Model provider logic often leaks into routes and makes systems hard to test.
- Untyped request and response objects make downstream failures harder to debug.
- Notebook prototypes usually lack error contracts, dependency boundaries, and logs.
- silent degradation of `structured logging` after a config change goes unnoticed

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

[1] Python typing: https://docs.python.org/3/library/typing.html
[2] Python logging: https://docs.python.org/3/library/logging.html
[3] Pydantic documentation: https://docs.pydantic.dev/
[4] pytest documentation: https://docs.pytest.org/
[5] FastAPI documentation: https://fastapi.tiangolo.com/
