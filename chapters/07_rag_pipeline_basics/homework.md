# Homework: RAG Pipeline Basics

Graded against `../../syllabus/evaluation_rubric.md`. Outputs under `my_work/`.

## Required

1. **Ingestion pipeline.** Build `ingest.py`: load → parse → clean → chunk →
   enrich metadata → embed → index, over a small redistributable corpus
   (10–30 docs, e.g. open standards or a project's docs). It must be
   idempotent: re-running on the same corpus does not change the chunk or
   vector count.

2. **Chunk quality review.** Sample ~30 chunks and review them in
   `my_work/chunk_quality.md` for: clauses cut mid-sentence, mangled tables,
   missing page/section metadata, boilerplate pollution. Name at least 3
   concrete fixes to the pipeline.

3. **Ask pipeline.** Build `ask.py`: filtered retrieval → prompt build →
   structured generation → citation validation → no-answer path → logging.
   Output JSON with `[doc:page]` citations and a `request_id`.

4. **No-answer test.** Write 5 questions the corpus cannot answer. All must
   return the exact no-answer JSON. Record results in `my_work/no_answer.md`.

5. **Citation correctness mini-eval.** Write 12 supported questions, each with
   the known supporting chunk id. Measure how often the answer cites the
   *right* chunk (not just any chunk). Report citation-correctness rate in
   `my_work/rag_report.md`.

6. **Chain logging.** For every `/ask`, log retrieved chunk ids + scores,
   chunks passed to generation, prompt/model/index versions, answer, cited
   ids, latency per stage. Demonstrate that you can reconstruct one request
   end-to-end from logs alone.

## Stretch

7. **Chunking experiment.** Compare fixed-size vs recursive vs section-aware
   chunking on the citation-correctness eval. Report which wins and why, with
   the retrieval-metric deltas.

8. **Parse-quality gate.** Add a check that flags documents whose extraction
   produced suspiciously little text or a bad table-to-text ratio. Run it over
   the corpus and report flagged documents.

9. **Injection probe.** Insert a document containing "ignore previous
   instructions…" into the corpus. Verify your pipeline ignores the injected
   instruction and still answers (or refuses) correctly.

10. **No-framework RAG (strongly recommended).** Before (or instead of)
    the LangChain/LlamaIndex version in task 3, build the same RAG without
    any framework — see `supplementary/07_no_framework_rag/`. Raw HTTP,
    numpy cosine, f-string prompt, structured-output JSON, citation
    validation. ~150 lines. Commit your own `minimal_rag.py` and the
    notes/comparison files in that README's checklist. This is the single
    biggest first-principles win in this chapter.

## Acceptance

- Re-running ingestion does not change the vector count (idempotent).
- All 5 unanswerable questions refuse.
- Citation-correctness rate is measured (not just citation presence).
- A single request can be reconstructed entirely from logs.
