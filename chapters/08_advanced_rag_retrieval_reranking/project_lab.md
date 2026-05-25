# Project Lab: Advanced RAG, Retrieval, and Reranking

Advanced RAG is search engineering plus model orchestration under latency, cost, and safety constraints. This lab turns the chapter's projects into concrete, reviewable
deliverables. Pick one project and finish it end-to-end before starting another.
The "Acceptance Criteria" sections are the gate — not the existence of files.

## Project 1: Run a retrieval experiment suite comparing chunking, hybrid search, reranking, and query rewriting.

### Scenario

The capstone RAG service has acceptable Recall@20 but its answers cite the wrong passage about 18% of the time. You suspect first-stage retrieval is fine but ranking inside the top-k is poor. You need to decide whether to add a cross-encoder reranker.

### Inputs

- 100-query golden set with reference chunk ids and graded relevance (0/1/2)
- first-stage retriever returning top-50 candidates per query
- two reranker options: a hosted cross-encoder API and a local `bge-reranker`-class model

### Outputs / Artifacts

- `rerank_experiment.md`: baseline vs each reranker on NDCG@5, citation-correctness, p95 latency
- decision record selecting one option with cost/latency/quality justification

### Test Cases

- queries where the supporting chunk is ranked 1-3 by first stage (rerank should not regress)
- queries where it is ranked 10-20 (rerank should rescue it)
- queries with no supporting chunk in the corpus (no-answer path must still trigger)
- queries with adversarial near-duplicate distractors

### Metrics

- Recall@k before reranking; NDCG@5 and citation-correctness after
- p95 end-to-end `/ask` latency, decomposed by stage
- $ per 1k queries for each reranker option

### Failure Cases To Cover

- NDCG@5 rises but answer faithfulness falls — the reranker over-promotes off-topic chunks
- Latency budget consumed by reranking forces a smaller k and recall drops
- Reranker is applied to every query when 70% of queries don't need it

### Acceptance Criteria

- decision record cites measured deltas, not paper claims
- a confidence-aware policy is described (when to skip rerank), with the rule explicit
- the experiment is reproducible from the repo by a reviewer who only reads the README

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

## Project 2: Implement a confidence-aware reranking policy that reranks only selected requests.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `query rewrite`, `multi-query`, `hybrid search`, `reranking`, `cross-encoder`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `query rewrite`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_2_implementation/`
- `my_work/project_2_report.md` summarising results with numbers
- `my_work/project_2_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `query rewrite`
- an edge case driven by the failure mode of `multi-query`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `query rewrite` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Basic vector search often misses exact domain references and rare terms.
- Reranking improves precision but consumes latency budget.
- Advanced techniques can degrade quality if they are not evaluated against a baseline.
- silent degradation of `query routing` after a config change goes unnoticed

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

## Project 3: Design a query router that chooses RAG, SQL analytics, tool workflow, or safe refusal.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `query rewrite`, `multi-query`, `hybrid search`, `reranking`, `cross-encoder`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `query rewrite`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_3_implementation/`
- `my_work/project_3_report.md` summarising results with numbers
- `my_work/project_3_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `query rewrite`
- an edge case driven by the failure mode of `multi-query`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `query rewrite` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Basic vector search often misses exact domain references and rare terms.
- Reranking improves precision but consumes latency budget.
- Advanced techniques can degrade quality if they are not evaluated against a baseline.
- silent degradation of `query routing` after a config change goes unnoticed

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

[1] RAG Techniques GitHub: https://github.com/NirDiamant/RAG_Techniques
[2] Awesome RAG GitHub: https://github.com/coree/awesome-rag
[3] Qdrant vector concepts: https://qdrant.tech/documentation/concepts/vectors/
[4] Weaviate hybrid search: https://weaviate.io/developers/weaviate/search/hybrid
[5] FlashRAG paper: https://arxiv.org/abs/2405.13576
[6] RAGLAB paper: https://arxiv.org/abs/2408.11381
