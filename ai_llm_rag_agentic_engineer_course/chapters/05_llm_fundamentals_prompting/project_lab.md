# Project Lab: LLM Fundamentals and Prompting

Prompting is interface design between instructions, data, tools, schemas, and model behavior. This lab turns the chapter's projects into concrete, reviewable
deliverables. Pick one project and finish it end-to-end before starting another.
The "Acceptance Criteria" sections are the gate — not the existence of files.

## Project 1: Build a prompt registry with versioning, test cases, scores, and known failures.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `token`, `context window`, `attention`, `system prompt`, `few-shot`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `token`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_1_implementation/`
- `my_work/project_1_report.md` summarising results with numbers
- `my_work/project_1_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `token`
- an edge case driven by the failure mode of `context window`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `token` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Longer prompts can increase cost and degrade focus if context is noisy.
- Structured output is still a contract that needs validation and failure handling.
- Prompt injection can arrive through user input, retrieved documents, or tool output.
- silent degradation of `prompt injection` after a config change goes unnoticed

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

## Project 2: Create a structured extraction task with schema validation and no-answer behavior.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `token`, `context window`, `attention`, `system prompt`, `few-shot`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `token`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_2_implementation/`
- `my_work/project_2_report.md` summarising results with numbers
- `my_work/project_2_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `token`
- an edge case driven by the failure mode of `context window`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `token` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Longer prompts can increase cost and degrade focus if context is noisy.
- Structured output is still a contract that needs validation and failure handling.
- Prompt injection can arrive through user input, retrieved documents, or tool output.
- silent degradation of `prompt injection` after a config change goes unnoticed

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

## Project 3: Build a prompt-injection test set for RAG context and tool outputs.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `token`, `context window`, `attention`, `system prompt`, `few-shot`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `token`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_3_implementation/`
- `my_work/project_3_report.md` summarising results with numbers
- `my_work/project_3_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `token`
- an edge case driven by the failure mode of `context window`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `token` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Longer prompts can increase cost and degrade focus if context is noisy.
- Structured output is still a contract that needs validation and failure handling.
- Prompt injection can arrive through user input, retrieved documents, or tool output.
- silent degradation of `prompt injection` after a config change goes unnoticed

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

[1] OpenAI platform documentation: https://platform.openai.com/docs
[2] OpenAI structured outputs: https://platform.openai.com/docs/guides/structured-outputs
[3] OpenAI embeddings guide: https://platform.openai.com/docs/guides/embeddings
[4] OpenAI prompt caching: https://platform.openai.com/docs/guides/prompt-caching
[5] OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
