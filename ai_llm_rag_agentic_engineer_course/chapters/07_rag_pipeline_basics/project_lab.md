# Project Lab: RAG Pipeline Basics

A RAG pipeline is an evidence chain from source document to answer and citation. This lab turns the chapter's projects into concrete, reviewable
deliverables. Pick one project and finish it end-to-end before starting another.
The "Acceptance Criteria" sections are the gate — not the existence of files.

## Project 1: Build an end-to-end RAG pipeline with citations and request traces.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `ingestion`, `parsing`, `cleaning`, `chunking`, `metadata enrichment`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `ingestion`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_1_implementation/`
- `my_work/project_1_report.md` summarising results with numbers
- `my_work/project_1_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `ingestion`
- an edge case driven by the failure mode of `parsing`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `ingestion` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Bad parsing and chunking cause failures before the model is called.
- Citations are only useful when they point to actually supporting context.
- No-answer behavior must be designed, tested, and measured.
- silent degradation of `no-answer behavior` after a config change goes unnoticed

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

## Project 2: Create a chunk quality report with broken chunks, metadata gaps, and fixes.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `ingestion`, `parsing`, `cleaning`, `chunking`, `metadata enrichment`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `ingestion`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_2_implementation/`
- `my_work/project_2_report.md` summarising results with numbers
- `my_work/project_2_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `ingestion`
- an edge case driven by the failure mode of `parsing`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `ingestion` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Bad parsing and chunking cause failures before the model is called.
- Citations are only useful when they point to actually supporting context.
- No-answer behavior must be designed, tested, and measured.
- silent degradation of `no-answer behavior` after a config change goes unnoticed

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

## Project 3: Build a citation correctness test set with supported and unsupported questions.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `ingestion`, `parsing`, `cleaning`, `chunking`, `metadata enrichment`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `ingestion`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_3_implementation/`
- `my_work/project_3_report.md` summarising results with numbers
- `my_work/project_3_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `ingestion`
- an edge case driven by the failure mode of `parsing`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `ingestion` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Bad parsing and chunking cause failures before the model is called.
- Citations are only useful when they point to actually supporting context.
- No-answer behavior must be designed, tested, and measured.
- silent degradation of `no-answer behavior` after a config change goes unnoticed

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

[1] LangChain RAG guide: https://docs.langchain.com/oss/python/langchain/rag
[2] LlamaIndex RAG overview: https://developers.llamaindex.ai/python/framework/understanding/rag/
[3] Haystack pipelines: https://docs.haystack.deepset.ai/docs/pipelines
[4] OpenAI File Search: https://platform.openai.com/docs/guides/tools-file-search
[5] RAG Survey paper: https://arxiv.org/abs/2312.10997
