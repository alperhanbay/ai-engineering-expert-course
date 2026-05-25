# Expanded Question Bank: Fine-Tuning and Model Adaptation

## How To Use This Bank

Answer without looking at the answer key. For every wrong answer, write one sentence explaining the concept in your own words and one sentence explaining how it appears in a production AI system.


## Multiple Choice

1. Which sentence is the best working definition of `RAG vs fine-tuning`?
   - A. The decision between adding external knowledge at inference time and changing model behavior through training.
   - B. Low-Rank Adaptation, a parameter-efficient fine-tuning method.
   - C. A memory-efficient LoRA variant using quantized base models.
   - D. Data generated artificially, often by models or templates.

2. In production AI work, what is the primary role of `LoRA`?
   - A. The decision between adding external knowledge at inference time and changing model behavior through training.
   - B. A memory-efficient LoRA variant using quantized base models.
   - C. Data generated artificially, often by models or templates.
   - D. Low-Rank Adaptation, a parameter-efficient fine-tuning method.

3. A teammate asks you to define `QLoRA` in one sentence. Which is closest?
   - A. Low-Rank Adaptation, a parameter-efficient fine-tuning method.
   - B. Data generated artificially, often by models or templates.
   - C. A memory-efficient LoRA variant using quantized base models.
   - D. The decision between adding external knowledge at inference time and changing model behavior through training.

4. Pick the description of `synthetic data` you would put in a `dictionary.md` entry.
   - A. A memory-efficient LoRA variant using quantized base models.
   - B. Data generated artificially, often by models or templates.
   - C. The decision between adding external knowledge at inference time and changing model behavior through training.
   - D. Low-Rank Adaptation, a parameter-efficient fine-tuning method.

5. Which sentence is the best working definition of `preference tuning`?
   - A. Training or optimizing using comparisons between outputs.
   - B. The decision between adding external knowledge at inference time and changing model behavior through training.
   - C. Low-Rank Adaptation, a parameter-efficient fine-tuning method.
   - D. A memory-efficient LoRA variant using quantized base models.

6. In production AI work, what is the primary role of `distillation`?
   - A. The decision between adding external knowledge at inference time and changing model behavior through training.
   - B. Low-Rank Adaptation, a parameter-efficient fine-tuning method.
   - C. A memory-efficient LoRA variant using quantized base models.
   - D. Training a smaller model to approximate behavior of a larger model.

7. A teammate asks you to define `classifier` in one sentence. Which is closest?
   - A. Low-Rank Adaptation, a parameter-efficient fine-tuning method.
   - B. A memory-efficient LoRA variant using quantized base models.
   - C. A model or rule system assigning inputs to categories.
   - D. The decision between adding external knowledge at inference time and changing model behavior through training.

8. Pick the description of `before/after eval` you would put in a `dictionary.md` entry.
   - A. A memory-efficient LoRA variant using quantized base models.
   - B. Comparing metrics before and after a change.
   - C. The decision between adding external knowledge at inference time and changing model behavior through training.
   - D. Low-Rank Adaptation, a parameter-efficient fine-tuning method.


## Applied Multiple Choice

1. Applied case: Teams often fine-tune before fixing retrieval, prompts, or evaluation.
   - A. Assume the largest available model will mask the underlying weakness in `RAG vs fine-tuning` so no system change is needed.
   - B. Skip the rollback plan; staging is close enough to production.
   - C. Set up a controlled experiment isolating `RAG vs fine-tuning`, capture before/after numbers, and write the result to a decision record.
   - D. Remove logging and evaluation to keep the diff small and merge faster.

2. Applied case: Synthetic data can encode wrong labels and unrealistic patterns.
   - A. Hard-code the new behaviour for the first failing case and call it a fix.
   - B. Add the work to the capstone as a reviewable artifact that exercises `LoRA` end-to-end, with tests and a trace.
   - C. Assume the largest available model will mask the underlying weakness in `RAG vs fine-tuning` so no system change is needed.
   - D. Skip the rollback plan; staging is close enough to production.

3. Applied case: Adapted models can regress safety, formatting, or general behavior.
   - A. Define explicit acceptance criteria, rollback steps, and a reviewer checklist tied to Fine-Tuning and Model Adaptation.
   - B. Skip the rollback plan; staging is close enough to production.
   - C. Hard-code the new behaviour for the first failing case and call it a fix.
   - D. Ship the change without measurement because the most recent demo looked good.

4. Applied case: Write a model adaptation decision memo for a capstone weakness.
   - A. Hard-code the new behaviour for the first failing case and call it a fix.
   - B. Ship the change without measurement because the most recent demo looked good.
   - C. Remove logging and evaluation to keep the diff small and merge faster.
   - D. Compare at least two approaches against a labelled set covering `before/after eval`, then choose on measured quality, latency, cost, and risk.

5. Applied case: Build a small intent classifier and compare it with an LLM router.
   - A. Remove logging and evaluation to keep the diff small and merge faster.
   - B. Assume the largest available model will mask the underlying weakness in `RAG vs fine-tuning` so no system change is needed.
   - C. Write a one-page design memo naming the assumption, the test that would falsify it, and the metric you'd watch in production.
   - D. Ship the change without measurement because the most recent demo looked good.

6. Applied case: Create a synthetic data quality review with deduplication, label checks, and human review sampling.
   - A. Skip the rollback plan; staging is close enough to production.
   - B. Set up a controlled experiment isolating `RAG vs fine-tuning`, capture before/after numbers, and write the result to a decision record.
   - C. Remove logging and evaluation to keep the diff small and merge faster.
   - D. Assume the largest available model will mask the underlying weakness in `RAG vs fine-tuning` so no system change is needed.


## Fill In The Blanks

1. Given the production failure "The team fine-tunes to memorize frequently changing documents.", the concept being misused is ________.
2. To handle situations where it adapts models with fewer trainable parameters than full fine-tuning, the engineering tool you reach for is ________ (watch for: Adapters overfit a small noisy dataset.).
3. ________ is best summarised as: A memory-efficient LoRA variant using quantized base models. Verification step: Test against a holdout set and document compute assumptions.
4. On a system review, you find synthetic legal examples contain incorrect assumptions — the underlying chapter concept is ________.
5. It can align style, helpfulness, or refusal behavior. A common failure looks like: Preference labels are inconsistent across reviewers. The concept is ________.
6. Given the production failure "The distilled model copies teacher errors.", the concept being misused is ________.
7. To handle situations where classifiers can replace expensive LLM routing for stable narrow tasks, the engineering tool you reach for is ________ (watch for: The classifier routes unsafe requests into normal RAG.).
8. ________ is best summarised as: Comparing metrics before and after a change. Verification step: Run the same eval set against baseline and candidate.

## Short Answer

1. If a reviewer asks 'why does `RAG vs fine-tuning` matter here?', what one-paragraph answer do you give? Include a metric.
2. Describe the smallest experiment that would tell you whether `LoRA` is correctly implemented in your system.
3. When would you intentionally *avoid* using `QLoRA`? Name a constraint or tradeoff.
4. What does a healthy log or trace look like for `synthetic data`? List the fields you would expect.
5. Explain how `preference tuning` appears in the capstone, what artifact proves it, and what failure mode you would test.
6. If a reviewer asks 'why does `distillation` matter here?', what one-paragraph answer do you give? Include a metric.
7. Describe the smallest experiment that would tell you whether `classifier` is correctly implemented in your system.
8. When would you intentionally *avoid* using `before/after eval`? Name a constraint or tradeoff.

## Scenario Questions

1. Incident: Teams often fine-tune before fixing retrieval, prompts, or evaluation. What do you inspect first, and which metric would prove the fix?
2. Design review: Synthetic data can encode wrong labels and unrealistic patterns. Which artifact would you require before approving?
3. Postmortem prompt: Adapted models can regress safety, formatting, or general behavior. What regression test would prevent recurrence?
4. A teammate proposes a major change to `synthetic data` with no experiment. Which artifact do you ask for before approving?

## Practical Debug Questions

1. What log or trace fields would help you debug a failure in `RAG vs fine-tuning` in this chapter's context?
2. What single metric would you watch in production when changing `preference tuning`?
3. You suspect `before/after eval` is degraded. Design the smallest experiment that would falsify or confirm it in under an hour.
4. For the failure 'Teams often fine-tune before fixing retrieval, prompts, or evaluation.', sketch a rollback plan with a clear restore-point definition.
5. What artifact would you put in a portfolio README to prove competence with `RAG vs fine-tuning`, `LoRA`, `QLoRA`?

## Answer Key

### Multiple Choice

1. A
2. D
3. C
4. B
5. A
6. D
7. C
8. B

### Applied Multiple Choice

1. C
2. B
3. A
4. D
5. C
6. B

### Fill In The Blanks

1. RAG vs fine-tuning
2. LoRA
3. QLoRA
4. synthetic data
5. preference tuning
6. distillation
7. classifier
8. before/after eval

Short-answer, scenario, and debug questions should be graded against the rubric in `../../syllabus/evaluation_rubric.md`.

## References

[1] Hugging Face PEFT: https://huggingface.co/docs/transformers/peft
[2] PEFT LoRA guide: https://huggingface.co/docs/peft/developer_guides/lora
[3] Hugging Face TRL: https://huggingface.co/docs/trl/index
[4] Transformers quantization: https://huggingface.co/docs/transformers/quantization
[5] QLoRA paper: https://arxiv.org/abs/2305.14314
