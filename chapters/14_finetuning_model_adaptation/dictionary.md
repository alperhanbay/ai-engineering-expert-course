# Dictionary: Fine-Tuning and Model Adaptation

Use this dictionary at the end of the chapter. Add your own examples in `my_work/dictionary_notes.md`.

| Term | Working Definition | Why It Matters | Common Failure Mode | Mastery Check |
| --- | --- | --- | --- | --- |
| `RAG vs fine-tuning` | The decision between adding external knowledge at inference time and changing model behavior through training. | Choosing the wrong lever wastes time and can reduce quality. | The team fine-tunes to memorize frequently changing documents. | Write a decision memo based on failure type and eval evidence. |
| `LoRA` | Low-Rank Adaptation, a parameter-efficient fine-tuning method. | It adapts models with fewer trainable parameters than full fine-tuning. | Adapters overfit a small noisy dataset. | Evaluate before/after performance and safety regressions. |
| `QLoRA` | A memory-efficient LoRA variant using quantized base models. | It lowers fine-tuning memory requirements. | Quantized adaptation changes behavior in untested ways. | Test against a holdout set and document compute assumptions. |
| `synthetic data` | Data generated artificially, often by models or templates. | It can expand coverage but can also introduce label noise and bias. | Synthetic legal examples contain incorrect assumptions. | Review samples, deduplicate, and validate against human-written holdouts. |
| `preference tuning` | Training or optimizing using comparisons between outputs. | It can align style, helpfulness, or refusal behavior. | Preference labels are inconsistent across reviewers. | Define rubrics and measure inter-reviewer consistency. |
| `distillation` | Training a smaller model to approximate behavior of a larger model. | It can reduce latency or cost for narrow tasks. | The distilled model copies teacher errors. | Evaluate on independent ground-truth cases, not only teacher outputs. |
| `classifier` | A model or rule system assigning inputs to categories. | Classifiers can replace expensive LLM routing for stable narrow tasks. | The classifier routes unsafe requests into normal RAG. | Measure precision/recall by class and monitor drift. |
| `before/after eval` | Comparing metrics before and after a change. | It proves whether an adaptation improved the intended behavior. | A fine-tuned model is deployed based on anecdotal examples. | Run the same eval set against baseline and candidate. |

## Dictionary Assignment

For each term:

1. Write a one-sentence definition in your own words.
2. Write a concrete example from your capstone (or planned capstone).
3. Write one failure mode you would test against.
4. Write one metric, test, or review check that would catch the failure.
5. Link one source from `references_numbered.md`.

## References

[1] Hugging Face PEFT: https://huggingface.co/docs/transformers/peft
[2] PEFT LoRA guide: https://huggingface.co/docs/peft/developer_guides/lora
[3] Hugging Face TRL: https://huggingface.co/docs/trl/index
[4] Transformers quantization: https://huggingface.co/docs/transformers/quantization
[5] QLoRA paper: https://arxiv.org/abs/2305.14314
