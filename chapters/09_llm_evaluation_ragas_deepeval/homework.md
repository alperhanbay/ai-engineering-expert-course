# Homework: LLM and RAG Evaluation

Graded against `../../syllabus/evaluation_rubric.md`. Outputs under `my_work/`.

## Required

1. **Golden dataset v1.** Build `my_work/golden/v1.jsonl` with at least 100
   cases across `low`/`medium`/`high` risk, including: unanswerable (must
   refuse), multi-source, ambiguous, and adversarial/injection cases. Each
   case has `question`, `expected_answer`, `reference_chunk_ids`, `risk_level`.
   Source questions from real-ish logs, not pure imagination.

2. **Eval runner.** Build `my_work/run_eval.py` that, for a config, computes:
   retrieval metrics (Recall@k, MRR), the RAGAS quartet (faithfulness, answer
   relevance, context precision/recall), citation correctness, and no-answer
   accuracy — broken out by risk level. Store per-case results + traces.

3. **Calibration study.** Have a human (you, carefully, with a rubric) score
   ~50 cases. Compare to the LLM-judge scores. Report agreement in
   `my_work/calibration.md`. If agreement is poor, adjust the judge prompt and
   re-measure.

4. **Failure taxonomy.** Apply the taxonomy from `lesson.md` section 8 to all
   failing cases. Report counts per category in `my_work/failure_report.md`
   and name the top fix per category.

5. **Release gate.** Define and implement a gate (`my_work/gate.py`) with
   explicit per-risk-level thresholds and a manual-review rule for high-risk
   regressions. Demonstrate it passing on one config and failing on a
   deliberately worse one.

6. **Human review workflow.** Document the rubric and the process by which a
   reviewed failure becomes a new golden case in `my_work/review_workflow.md`.

## Stretch

7. **Held-out set.** Split your golden set into dev and held-out. Show that a
   prompt tuned on dev does *not* overfit by checking held-out performance.

8. **Judge robustness.** Test whether your LLM judge favours verbose answers:
   score a concise correct answer and a verbose correct answer; report any
   bias.

9. **Trend tracking.** Run the eval against two configs and store both runs.
   Produce a diff report showing per-risk-level deltas (the input to the gate).

## Acceptance

- Golden set has ≥100 cases spanning all risk levels and the hard categories.
- The gate blocks a config that regresses high-risk cases even if the average
  improves.
- Calibration agreement between judge and human is measured and reported.
- Failures are categorised, not lumped as "hallucination."
