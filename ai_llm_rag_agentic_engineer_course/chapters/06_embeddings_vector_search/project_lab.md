# Project Lab: Embeddings and Vector Search

Retrieval quality starts with representation, indexing, filtering, and measurement. This lab turns the chapter's projects into concrete, reviewable
deliverables. Pick one project and finish it end-to-end before starting another.
The "Acceptance Criteria" sections are the gate — not the existence of files.

## Project 1: Benchmark vector-only, keyword-only, and hybrid retrieval on a labeled dataset.

### Scenario

You inherit a RAG service whose retriever runs on Qdrant. The team wants to know whether BM25, dense-only, or hybrid retrieval gives the best Recall@5 on the domain corpus, and whether a switch is worth the operational change.

### Inputs

- labeled retrieval set: 100 queries with at least one ground-truth chunk id per query
- corpus of ~5k chunks with `tenant_id`, `source`, `page`, `version` metadata
- two embedding models (e.g. a 768-dim and a 1024-dim) for comparison

### Outputs / Artifacts

- `bench_results.csv` with columns: strategy, recall@1, recall@5, mrr, p50_ms, p95_ms, index_build_s
- `bench_report.md` summarising recommendation, tradeoffs, and migration risk

### Test Cases

- exact-match query (rare domain term) — hybrid should beat dense-only
- paraphrased query — dense-only should beat BM25
- query with metadata filter (`tenant_id=A`) — must not return chunks from `tenant_id=B`
- empty/short query — system should not crash and should log a low-quality-input warning
- duplicate-chunk corpus — dedup logic should not let near-duplicates fill the top-k

### Metrics

- Recall@1, Recall@5, MRR on the labeled set
- p50 and p95 retrieval latency at k=10 under 10 concurrent queries
- index build time and on-disk size

### Failure Cases To Cover

- Recall@50 looks great but Recall@5 (the actual context budget) is mediocre
- Filtering happens after retrieval, exposing other-tenant chunks in logs
- Hybrid fusion weights are tuned by hand on the same set used to report results
- The benchmark uses cosine on vectors the embedding model expected to be normalised

### Acceptance Criteria

- the report names a single recommended strategy with measured deltas, not vibes
- the metadata-filter test passes for both single- and cross-tenant cases
- a rollback path exists (old index retained, traffic-switch via config flag)

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

## Project 2: Create a multi-tenant metadata filter lab and prove unauthorized chunks are never retrieved.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `embedding`, `cosine similarity`, `dot product`, `HNSW`, `IVF`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `embedding`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_2_implementation/`
- `my_work/project_2_report.md` summarising results with numbers
- `my_work/project_2_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `embedding`
- an edge case driven by the failure mode of `cosine similarity`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `embedding` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Popular embedding models may underperform on domain-specific terminology.
- Filtering after retrieval can create privacy risk and misleading metrics.
- Index migrations can silently break retrieval unless they are versioned and evaluated.
- silent degradation of `NDCG` after a config change goes unnoticed

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

## Project 3: Write an embedding migration plan with dual indexes, evaluation, and rollback.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `embedding`, `cosine similarity`, `dot product`, `HNSW`, `IVF`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `embedding`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_3_implementation/`
- `my_work/project_3_report.md` summarising results with numbers
- `my_work/project_3_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `embedding`
- an edge case driven by the failure mode of `cosine similarity`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `embedding` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Popular embedding models may underperform on domain-specific terminology.
- Filtering after retrieval can create privacy risk and misleading metrics.
- Index migrations can silently break retrieval unless they are versioned and evaluated.
- silent degradation of `NDCG` after a config change goes unnoticed

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

[1] Qdrant search documentation: https://qdrant.tech/documentation/search/
[2] Qdrant indexing documentation: https://qdrant.tech/documentation/manage-data/indexing/
[3] Milvus documentation: https://milvus.io/docs/
[4] Weaviate hybrid search: https://weaviate.io/developers/weaviate/search/hybrid
[5] FAISS index guidelines: https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index
[6] pgvector GitHub: https://github.com/pgvector/pgvector
