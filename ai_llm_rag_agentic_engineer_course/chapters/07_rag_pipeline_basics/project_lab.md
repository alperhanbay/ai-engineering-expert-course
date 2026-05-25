# Project Lab: RAG Pipeline Basics

A RAG pipeline is an evidence chain from source document to answer and citation. This lab turns the chapter's projects into concrete, reviewable
deliverables. Pick one project and finish it end-to-end before starting another.
The "Acceptance Criteria" sections are the gate — not the existence of files.

## Project 1: Build an end-to-end RAG pipeline with citations and request traces.

### Scenario

Build the first end-to-end RAG pipeline that the capstone will iterate on. Source documents should be a small public-domain corpus you can re-distribute (e.g. a few open standards PDFs or a project's docs). The pipeline must produce answers with citations and a clear 'no answer' path when the corpus doesn't support the question.

### Inputs

- 10-30 source documents (PDF, HTML, or Markdown) totalling roughly 200-500 pages
- 20 evaluation questions: 12 supported by the corpus, 5 unsupported, 3 ambiguous
- for supported questions: the reference document id and page/section that answers it
- one embedding model and one generator model, both named in config

### Outputs / Artifacts

- `ingest.py` — parse, clean, chunk, enrich, embed, index (idempotent)
- `ask.py` — retrieve top-k, build prompt, generate answer with `[doc:page]` citations, return JSON
- `rag_report.md` — per-question: answer, retrieved chunk ids, citation-correctness verdict
- `chunk_quality.md` — sample of 30 chunks reviewed for breakage and metadata completeness

### Test Cases

- supported question, answer in a single chunk — citation must point to that chunk
- supported question requiring 2 chunks — both should be cited
- unsupported question — system must respond 'no answer in sources' (not invent one)
- ambiguous question — system must either ask a clarifying question or list both interpretations
- table-heavy page — parser must not destroy column alignment in the cited chunk

### Metrics

- answer correctness (manual rubric on the 20 questions)
- citation correctness: cited chunk actually supports the claim (yes/partial/no)
- no-answer accuracy on the 5 unsupported questions (target 100%)
- p95 latency for `/ask` end-to-end

### Failure Cases To Cover

- Citations point to chunks that mention the keyword but don't support the claim
- PDF parser swallows section headers, so cited 'page' is misleading
- Chunks too small: the answer is split across boundaries and retrieval misses one side
- On unsupported questions, the model produces a confident wrong answer
- Re-ingesting documents creates duplicate vectors instead of updating in place

### Acceptance Criteria

- all 5 unsupported-question cases produce a refusal
- at least 80% of supported answers have a citation a reviewer can verify
- the chunk quality review names at least 3 concrete fixes for the ingestion pipeline
- re-running `ingest.py` on the same corpus does not change the vector count

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
