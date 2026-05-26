# Project Lab: Orientation and Expert Roadmap

Expert AI engineering is the discipline of turning model capability into reliable, observable, secure, and useful systems. This lab turns the chapter's projects into concrete, reviewable
deliverables. Pick one project and finish it end-to-end before starting another.
The "Acceptance Criteria" sections are the gate — not the existence of files.

## Project 1: Build a public-style learning roadmap with evidence checkpoints.

### Scenario

Before writing any code, plan the capstone as a public-style project. A reviewer should be able to read your roadmap and tell you what success looks like, what data you'll use, who the users are, and how you will know each chapter is finished.

### Inputs

- a one-paragraph capstone idea in a regulated or high-accuracy domain (legal, medical, finance, internal policy, etc.)
- the 17-chapter outline as a checklist
- a list of 3-5 realistic risks (data sensitivity, latency, factuality, cost, abuse)

### Outputs / Artifacts

- `my_work/capstone_proposal.md` — problem, users, data, success metrics, risks, non-goals
- `my_work/roadmap.md` — chapter-by-chapter evidence checkpoints (what artifact proves the chapter is done)
- `my_work/decision_log.md` — template with date, decision, alternatives, evidence, owner

### Test Cases

- ask a peer to read the proposal cold; they can answer 'what does success look like?' without you
- the roadmap names a concrete artifact per chapter, not 'understand X'
- the decision log has at least one entry already (e.g. 'why this domain?')
- risks are specific (e.g. 'hallucinated dosage') not generic ('safety')

### Metrics

- proposal length under 600 words but covers all required sections
- % of chapters with a named evidence artifact (target 100%)
- reviewer feedback turnaround time on the proposal (target under 48h)

### Failure Cases To Cover

- Proposal lists tools (LangGraph, Qdrant…) instead of users and outcomes
- Roadmap collapses to 'read everything then code at the end'
- Risks are copied from a generic template and don't relate to the chosen domain

### Acceptance Criteria

- a reader can list the users, the success metric, and the top risk without re-reading
- the roadmap names what artifact will exist in `my_work/` at the end of each chapter
- the decision log template is ready and the first decision is written into it

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

## Project 2: Write a capstone proposal with data, users, risks, and success metrics.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `AI engineering`, `system boundary`, `capstone`, `evidence portfolio`, `failure log`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `AI engineering`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_2_implementation/`
- `my_work/project_2_report.md` summarising results with numbers
- `my_work/project_2_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `AI engineering`
- an edge case driven by the failure mode of `system boundary`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `AI engineering` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Many learners collect tools without building an integrated system.
- Demos hide evaluation, security, latency, and rollback problems.
- A serious portfolio needs evidence, not only screenshots.
- silent degradation of `expert rubric` after a config change goes unnoticed

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

## Project 3: Create a decision log template and use it for the first five architecture choices.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `AI engineering`, `system boundary`, `capstone`, `evidence portfolio`, `failure log`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `AI engineering`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_3_implementation/`
- `my_work/project_3_report.md` summarising results with numbers
- `my_work/project_3_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `AI engineering`
- an edge case driven by the failure mode of `system boundary`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `AI engineering` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Many learners collect tools without building an integrated system.
- Demos hide evaluation, security, latency, and rollback problems.
- A serious portfolio needs evidence, not only screenshots.
- silent degradation of `expert rubric` after a config change goes unnoticed

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
[2] LangGraph overview: https://docs.langchain.com/oss/python/langgraph/overview
[3] LlamaIndex RAG overview: https://developers.llamaindex.ai/python/framework/understanding/rag/
[4] OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
