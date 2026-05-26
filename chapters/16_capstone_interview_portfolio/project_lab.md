# Project Lab: Capstone, Portfolio, and Interview

A strong portfolio demonstrates working systems, measured quality, honest failure analysis, and defensible tradeoffs. This lab turns the chapter's projects into concrete, reviewable
deliverables. Pick one project and finish it end-to-end before starting another.
The "Acceptance Criteria" sections are the gate — not the existence of files.

## Project 1: Build the full capstone and document how to run, test, evaluate, and inspect it.

### Scenario

Tie the 16 prior chapters into a single shippable capstone artifact and the interview narrative that goes with it. The goal is not to add features; it is to make the system and the story defensible end-to-end.

### Inputs

- all artifacts from prior chapters (ingestion, RAG, agent, eval, security, observability)
- a chosen domain and a small, redistributable corpus or synthetic dataset
- the chapter 09 golden set with at least 100 cases
- a target audience for the portfolio (e.g. 'AI engineer at a regulated-industry company')

### Outputs / Artifacts

- runnable capstone repo with: setup, demo script, tests, eval suite, threat model, observability, release manifest
- `architecture_pack/` — API, data, RAG, agent, deployment, threat diagrams (each one page)
- `portfolio_README.md` — what it is, who it's for, how to run, results with numbers, limitations, references
- `interview_kit.md` — 5 STAR stories (failure, tradeoff, incident, collaboration, scope cut), 3 system design walkthroughs, 10 question/answer drills
- `demo.md` — repeatable demo: ingestion, supported answer, unsupported answer, eval run, one security case

### Test Cases

- a stranger can clone the repo and run the demo in under 15 minutes following the README
- the unsupported question case still refuses correctly during the demo
- the security case (e.g. injection in retrieved doc) is shown live and the guardrail blocks it
- the interview kit's STAR stories each name a measurable result

### Metrics

- golden-set pass rate, broken out by risk level
- p95 `/ask` latency under realistic load
- % of OWASP LLM Top 10 categories covered by at least one guardrail test
- time-to-run for the full demo (target under 15 minutes from `git clone`)

### Failure Cases To Cover

- Portfolio README shows only the happy path; eval and security cases are hidden
- STAR stories list tools but no measurable result or tradeoff
- System design walkthrough doesn't reach failure modes or rollback
- The architecture pack diagrams are decorative and don't match the implementation

### Acceptance Criteria

- demo runs end-to-end from a fresh clone, captured in a recording or transcript
- every numeric claim in `portfolio_README.md` traces to a committed eval or trace
- limitations are named explicitly — at least three honest gaps with planned next steps
- the interview kit is rehearsed at least once with a peer or on tape

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

## Project 2: Create an architecture pack with API, data, RAG, agent, deployment, and threat diagrams.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `capstone`, `architecture pack`, `evaluation report`, `demo script`, `system design`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `capstone`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_2_implementation/`
- `my_work/project_2_report.md` summarising results with numbers
- `my_work/project_2_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `capstone`
- an edge case driven by the failure mode of `architecture pack`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `capstone` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Many portfolios show only success paths and omit evaluation or failure cases.
- Interview answers fail when candidates cannot connect implementation decisions to metrics.
- Open-source quality requires runnable docs, source references, and transparent limitations.
- silent degradation of `portfolio README` after a config change goes unnoticed

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

## Project 3: Write a public portfolio README with limitations, tradeoffs, metrics, and source references.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `capstone`, `architecture pack`, `evaluation report`, `demo script`, `system design`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `capstone`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_3_implementation/`
- `my_work/project_3_report.md` summarising results with numbers
- `my_work/project_3_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `capstone`
- an edge case driven by the failure mode of `architecture pack`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `capstone` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Many portfolios show only success paths and omit evaluation or failure cases.
- Interview answers fail when candidates cannot connect implementation decisions to metrics.
- Open-source quality requires runnable docs, source references, and transparent limitations.
- silent degradation of `portfolio README` after a config change goes unnoticed

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

[1] OpenAI Cookbook: https://github.com/openai/openai-cookbook
[2] LangGraph GitHub: https://github.com/langchain-ai/langgraph
[3] LlamaIndex GitHub: https://github.com/run-llama/llama_index
[4] RAG Techniques GitHub: https://github.com/NirDiamant/RAG_Techniques
[5] DeepEval GitHub: https://github.com/confident-ai/deepeval
[6] RAGAS GitHub: https://github.com/explodinggradients/ragas
