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

<!-- HAND-AUTHORED: do not regenerate -->
## Extended Glossary

Additional terms used in this chapter, each with a concise definition and an authoritative source.

- **Fine-tuning** — further training a model to adapt its behaviour. Source: [OpenAI fine-tuning](https://platform.openai.com/docs/guides/fine-tuning)
- **PEFT** — parameter-efficient fine-tuning: train few added parameters. Source: [HF PEFT](https://huggingface.co/docs/peft)
- **LoRA** — low-rank adapters injected into attention layers. Source: [Hu et al., 2021](https://arxiv.org/abs/2106.09685)
- **QLoRA** — LoRA on a quantized base, fitting one GPU. Source: [Dettmers et al., 2023](https://arxiv.org/abs/2305.14314)
- **Adapter** — the small trainable, swappable, rollback-able artifact LoRA produces. Source: [HF PEFT](https://huggingface.co/docs/peft)
- **Synthetic data** — model/template-generated training data; review for noise/bias. Source: [HF synthetic data](https://huggingface.co/blog/synthetic-data-save-costs)
- **Preference tuning / DPO** — training from output comparisons. Source: [Rafailov et al., 2023](https://arxiv.org/abs/2305.18290)
- **RLHF** — reinforcement learning from human feedback. Source: [Ouyang et al., InstructGPT](https://arxiv.org/abs/2203.02155)
- **Distillation** — training a small model to mimic a larger one. Source: [Hinton et al., 2015](https://arxiv.org/abs/1503.02531)
- **Catastrophic forgetting** — adaptation degrading prior (incl. safety) behaviour. Source: [Kirkpatrick et al., 2017](https://arxiv.org/abs/1612.00796)
- **Held-out set** — data never seen in training; hash-check to prove no leakage. Source: [Google, Rules of ML](https://developers.google.com/machine-learning/guides/rules-of-ml)

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
