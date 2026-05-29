# Homework: Embeddings and Vector Search

Graded against `../../syllabus/evaluation_rubric.md`. Outputs under `my_work/`.

## Required

1. **Labelled retrieval set.** Build `my_work/retrieval_set.jsonl`: at least 50
   queries, each with `{query, relevant_chunk_ids: [...], type}` where `type`
   distinguishes paraphrase, exact-term, and no-answer queries. Include at
   least 5 "no relevant chunk exists" cases.

2. **Verify the distance metric.** For your chosen embedding model, confirm
   whether outputs are normalised and document in `my_work/metric.md` which
   metric (cosine / dot / L2) is correct and why. Add an assertion to your
   ingestion code.

3. **Retrieval benchmark.** Build `my_work/bench.py` comparing dense-only vs
   hybrid (RRF) on Recall@1, Recall@5, MRR, and p95 latency — measured at the
   same k you pass to generation. Output `bench_results.csv`.

4. **Benchmark report.** Write `my_work/bench_report.md` recommending one
   configuration with the measured deltas and the tradeoffs. Break results out
   by query `type` (where does each method win?).

5. **Cross-tenant isolation test.** Seed chunks for two tenants. Prove, with a
   filtered-search test, that a tenant-A query never returns a tenant-B chunk.
   The test must use pre-filtering (filter during search), not post-filtering.

6. **Index migration plan.** Write `my_work/migration_plan.md` for switching
   embedding models, using dual index + eval gate + config flip + rollback
   window. Name the artifacts and the cutover trigger.

## Stretch

7. **ANN parameter sweep.** For HNSW, sweep `ef_search` over {16, 32, 64, 128,
   256} and plot Recall@5 vs p95 latency. Identify the knee of the curve and
   recommend a value.

8. **Filtered-recall measurement.** Measure Recall@5 with and without your real
   metadata filters applied. Quantify the recall loss under filtering and
   propose a mitigation if it's large.

9. **Embedding model bake-off.** Add a second embedding model to the benchmark
   (ideally a domain-tuned or multilingual one). Report which wins on your
   domain and whether the storage/cost difference justifies it.

10. **Karpathy-style geometry lab (recommended).** Complete
    `supplementary/06_embedding_geometry/` — embed the provided sentences
    locally with `sentence-transformers`, inspect the pairwise cosine
    matrix, and produce a t-SNE projection. Commit `notes.md` answering
    the three questions in its README. *This is the single most useful
    thing to do alongside this chapter.*

## Acceptance

- Recall is measured at the production k, not an inflated k.
- The cross-tenant test passes and uses pre-filtering.
- The benchmark report recommends a config with numbers, not vibes.
- The migration plan has a tested rollback step (or a clear simulation of it).
