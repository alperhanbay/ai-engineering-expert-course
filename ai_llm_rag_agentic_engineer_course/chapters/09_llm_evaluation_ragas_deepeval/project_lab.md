# Project Lab: LLM and RAG Evaluation

Evaluation is the control system for quality, safety, and release confidence. This lab turns the chapter's projects into concrete, reviewable
deliverables. Pick one project and finish it end-to-end before starting another.
The "Acceptance Criteria" sections are the gate — not the existence of files.

## Project 1: Create a 100-case golden dataset with expected answer, reference context, and risk level.

### Scenario

You are building the 100-case golden set the rest of the course will gate releases on. Each case must be reviewable by a domain expert and runnable through RAGAS and DeepEval.

### Inputs

- candidate questions sourced from real user logs (with PII removed) and curated by the team
- for each: expected answer, list of reference chunk ids, risk level (low/medium/high), failure category if known
- current RAG system under test (retriever + generator)

### Outputs / Artifacts

- `golden/v1.jsonl` — versioned dataset with schema validation
- `golden/README.md` — coverage table by risk level and failure category
- `run_eval.py` — script that produces per-case metrics + aggregate summary

### Test Cases

- supported question with a single clear source
- supported question requiring two sources to answer correctly
- unsupported question — system must refuse (no-answer behaviour)
- adversarial question attempting prompt injection through retrieved text
- ambiguous question — multiple acceptable answers; reviewer rubric must handle it

### Metrics

- Faithfulness, Answer Relevance, Context Precision, Context Recall (RAGAS)
- Custom citation-correctness (cited chunk actually supports the claim)
- Per-risk-level pass rate; high-risk failures gate release

### Failure Cases To Cover

- Aggregate score looks healthy but all failures concentrate in high-risk cases
- LLM-as-judge drifts from human review; calibration set is never refreshed
- Reference chunk ids become invalid after re-indexing

### Acceptance Criteria

- at least 100 cases across all risk levels with reviewer initials
- release rule is explicit: thresholds + manual review of high-risk failures
- the dataset is versioned and a migration plan exists for re-indexing events

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

## Project 2: Build a RAG evaluation runner that stores traces, metrics, failures, and release recommendation.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `golden dataset`, `faithfulness`, `answer relevance`, `context precision`, `context recall`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `golden dataset`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_2_implementation/`
- `my_work/project_2_report.md` summarising results with numbers
- `my_work/project_2_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `golden dataset`
- an edge case driven by the failure mode of `faithfulness`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `golden dataset` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Aggregate scores hide failure categories that matter to users.
- LLM-as-judge metrics need calibration against human review.
- Evaluation must cover retrieval, generation, citations, tools, and safety.
- silent degradation of `failure taxonomy` after a config change goes unnoticed

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

## Project 3: Design a human review workflow that turns expert feedback into new eval cases.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `golden dataset`, `faithfulness`, `answer relevance`, `context precision`, `context recall`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `golden dataset`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_3_implementation/`
- `my_work/project_3_report.md` summarising results with numbers
- `my_work/project_3_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `golden dataset`
- an edge case driven by the failure mode of `faithfulness`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `golden dataset` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Aggregate scores hide failure categories that matter to users.
- LLM-as-judge metrics need calibration against human review.
- Evaluation must cover retrieval, generation, citations, tools, and safety.
- silent degradation of `failure taxonomy` after a config change goes unnoticed

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

[1] RAGAS metrics: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/
[2] RAGAS GitHub: https://github.com/explodinggradients/ragas
[3] DeepEval documentation: https://deepeval.com/docs/introduction
[4] DeepEval GitHub: https://github.com/confident-ai/deepeval
[5] LangSmith evaluation concepts: https://docs.langchain.com/langsmith/evaluation-concepts
[6] RAGAS paper: https://arxiv.org/abs/2309.15217
[7] ARES paper: https://arxiv.org/abs/2311.09476
