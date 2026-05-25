# Deep Dive: Fine-Tuning and Model Adaptation

## Thesis

Fine-tuning is a decision, not a reflex; use it only when the problem is behavior adaptation rather than missing knowledge. This file expands the chapter beyond the basic lesson and connects it to current practice, project work, and verifiable sources.

## Core Concepts

### `RAG vs fine-tuning`

The decision between adding external knowledge at inference time and changing model behavior through training. Choosing the wrong lever wastes time and can reduce quality.

Verification: Write a decision memo based on failure type and eval evidence.

### `LoRA`

Low-Rank Adaptation, a parameter-efficient fine-tuning method. It adapts models with fewer trainable parameters than full fine-tuning.

Verification: Evaluate before/after performance and safety regressions.

### `QLoRA`

A memory-efficient LoRA variant using quantized base models. It lowers fine-tuning memory requirements.

Verification: Test against a holdout set and document compute assumptions.

### `synthetic data`

Data generated artificially, often by models or templates. It can expand coverage but can also introduce label noise and bias.

Verification: Review samples, deduplicate, and validate against human-written holdouts.

### `preference tuning`

Training or optimizing using comparisons between outputs. It can align style, helpfulness, or refusal behavior.

Verification: Define rubrics and measure inter-reviewer consistency.

### `distillation`

Training a smaller model to approximate behavior of a larger model. It can reduce latency or cost for narrow tasks.

Verification: Evaluate on independent ground-truth cases, not only teacher outputs.

### `classifier`

A model or rule system assigning inputs to categories. Classifiers can replace expensive LLM routing for stable narrow tasks.

Verification: Measure precision/recall by class and monitor drift.

### `before/after eval`

Comparing metrics before and after a change. It proves whether an adaptation improved the intended behavior.

Verification: Run the same eval set against baseline and candidate.


## Implementation Blueprint

Build this chapter as part of the capstone, not as isolated reading. The implementation should produce one or more concrete artifacts: code, schema, benchmark, trace, rubric, threat model, release manifest, or architecture document.

Recommended workflow:

1. Define the exact problem this chapter solves in the capstone.
2. Identify the data or request path affected by `RAG vs fine-tuning`, `LoRA`, `QLoRA`, `synthetic data`, `preference tuning`, `distillation`, `classifier`, `before/after eval`.
3. Create a minimal artifact that can be reviewed.
4. Add failure cases before adding complexity.
5. Add measurements, logs, traces, or human review.
6. Document the decision with numbered references.

## Current Engineering Problems To Study

- Teams often fine-tune before fixing retrieval, prompts, or evaluation.
- Synthetic data can encode wrong labels and unrealistic patterns.
- Adapted models can regress safety, formatting, or general behavior.

## Production Failure Modes

Each failure below names the concept, the way it shows up in production, and the check that would have caught it earlier. Treat this section as the source for regression tests and runbook entries.

- `RAG vs fine-tuning` — failure: The team fine-tunes to memorize frequently changing documents. Mitigation check: Write a decision memo based on failure type and eval evidence.
- `LoRA` — failure: Adapters overfit a small noisy dataset. Mitigation check: Evaluate before/after performance and safety regressions.
- `QLoRA` — failure: Quantized adaptation changes behavior in untested ways. Mitigation check: Test against a holdout set and document compute assumptions.
- `synthetic data` — failure: Synthetic legal examples contain incorrect assumptions. Mitigation check: Review samples, deduplicate, and validate against human-written holdouts.
- `preference tuning` — failure: Preference labels are inconsistent across reviewers. Mitigation check: Define rubrics and measure inter-reviewer consistency.
- `distillation` — failure: The distilled model copies teacher errors. Mitigation check: Evaluate on independent ground-truth cases, not only teacher outputs.
- `classifier` — failure: The classifier routes unsafe requests into normal RAG. Mitigation check: Measure precision/recall by class and monitor drift.
- `before/after eval` — failure: A fine-tuned model is deployed based on anecdotal examples. Mitigation check: Run the same eval set against baseline and candidate.

## Project Directions

- Write a model adaptation decision memo for a capstone weakness.
- Build a small intent classifier and compare it with an LLM router.
- Create a synthetic data quality review with deduplication, label checks, and human review sampling.

## Verification Artifacts

- A short concept summary with citations.
- A capstone artifact that uses at least three chapter concepts.
- A test, metric, evaluation, or review checklist.
- A failure analysis table.
- A decision record comparing at least two alternatives.
- A reference section using `[1]`, `[2]` style citations.

## How This Chapter Connects To The Capstone

In the capstone, this chapter should leave a visible artifact. Examples include a module, schema, benchmark, design memo, evaluation result, threat model, release manifest, or demo step. Do not mark the chapter complete until the artifact is connected to the capstone.

## References

[1] Hugging Face PEFT: https://huggingface.co/docs/transformers/peft
[2] PEFT LoRA guide: https://huggingface.co/docs/peft/developer_guides/lora
[3] Hugging Face TRL: https://huggingface.co/docs/trl/index
[4] Transformers quantization: https://huggingface.co/docs/transformers/quantization
[5] QLoRA paper: https://arxiv.org/abs/2305.14314
