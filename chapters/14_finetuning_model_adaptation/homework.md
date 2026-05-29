# Homework: Fine-Tuning and Model Adaptation

Graded against `../../syllabus/evaluation_rubric.md`. Outputs under `my_work/`.

## Required

1. **Failure classification.** From your chapter-9 failure log, categorise at
   least 30 failures (retrieval / prompt / model-behaviour / data / safety).
   In `my_work/failure_classification.md`, state which are *not* fine-tuning
   problems and why.

2. **Adaptation decision memo.** Write `my_work/adaptation_decision.md` for one
   real weakness: failure evidence, cheaper levers tried (prompt, retrieval),
   the proposed adaptation OR the decision not to adapt, and per-risk-level
   success criteria including safety and regression checks. Make it approvable
   in one read.

3. **Small classifier vs LLM router.** Build a small intent classifier for your
   chapter-8 routing task and compare it against an LLM-classification call on
   accuracy, latency, and cost. Report in `my_work/classifier_vs_llm.md`.

4. **Before/after eval design.** Even if you don't train, design the exact
   before/after eval you *would* run: same golden set, fixed seed, per risk
   level, with target + safety + formatting + generality metrics. Put it in
   `my_work/before_after_plan.md`.

## Stretch

5. **QLoRA run.** If you have the hardware, fine-tune a small model with QLoRA
   on ~300 hand-curated examples for a behaviour failure (e.g. output
   formatting). Log hyperparameters, dataset hash, and a hash-checked held-out
   set. Run the before/after eval and report whether you'd ship it.

6. **Synthetic data review.** If you generate any training data, write
   `my_work/synthetic_data_review.md`: sample size, dedup rate, label-spotcheck
   pass rate against human ground truth. Show at least one wrong synthetic
   label you caught.

7. **Safety regression probe.** Run your chapter-15 injection cases against
   base vs adapted model. Show whether adaptation eroded safety.

## Acceptance

- The decision memo justifies the lever (or the decision not to adapt) with
  failure evidence and tried alternatives.
- The classifier comparison reports accuracy, latency, AND cost.
- The before/after plan includes safety and regression metrics, not just the
  target.
- If you trained: the held-out set is hash-verified as unseen.
