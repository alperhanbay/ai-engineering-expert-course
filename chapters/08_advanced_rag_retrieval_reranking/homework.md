# Homework: Advanced RAG, Retrieval, and Reranking

Graded against `../../syllabus/evaluation_rubric.md`. Outputs under `my_work/`.

## Required

1. **Experiment harness.** Build `my_work/experiment.py` that runs a named
   configuration (baseline, +hybrid, +rerank, +rewrite) end-to-end over your
   chapter-06 labelled set and chapter-07 golden set, reporting Recall@5,
   NDCG@5, citation correctness, faithfulness proxy, and p95 latency. It must
   change one variable at a time.

2. **Reranking experiment.** Compare baseline vs at least one cross-encoder
   reranker. Report the deltas in `my_work/rerank_experiment.md`. Crucially,
   report faithfulness/citation-correctness alongside NDCG — show whether
   ranking gains came with answer-quality gains.

3. **Confidence-aware policy.** Implement a policy that reranks only when
   first-stage confidence is low (score gap below a threshold). Tune the
   threshold on your eval set. Report what fraction of queries get reranked and
   what fraction of the quality gain you keep.

4. **Query router.** Build a router over at least 3 routes (RAG /
   analytics-or-tool / refuse). Evaluate on a labelled set of queries with
   correct routes; produce a confusion matrix in `my_work/routing_eval.md`.
   Pay special attention to high-stakes mis-routes.

5. **Decision record.** Write `my_work/advanced_rag_decisions.md` stating which
   techniques you keep and which you reject, each justified by a measured
   delta. Rejections are as valuable as adoptions.

## Stretch

6. **Query rewriting safety.** Measure original-vs-rewritten retrieval on your
   labelled set. Identify any queries where the rewrite changed the meaning and
   hurt retrieval. Decide where rewriting should be disabled.

7. **Parent-child retrieval.** Implement child-chunk retrieval with parent
   expansion. Compare answer faithfulness vs flat chunking on cases that need
   surrounding context.

8. **Context compression risk test.** Build 10 cases where a small qualifier
   ("except for commercial vehicles") flips the answer. Measure how often
   compression drops the qualifier and produces a wrong answer.

## Acceptance

- Every adopted technique shows a measured gain over baseline that justifies
  its latency/cost.
- The reranking analysis reports faithfulness, not just ranking metrics.
- The router eval includes a confusion matrix and flags high-stakes mis-routes.
- At least one technique is rejected with evidence.
