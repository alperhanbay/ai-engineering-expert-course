# Lesson: Fine-Tuning and Model Adaptation

## 1. What Model Adaptation Means

Model adaptation is the process of changing model behavior for a task or domain.

Main options:

- prompt engineering;
- RAG;
- smaller task-specific classifiers;
- fine-tuning;
- LoRA/QLoRA;
- preference tuning;
- distillation;
- tool use;
- evaluation and guardrails.

Fine-tuning is only one option.

## 2. RAG vs Fine-Tuning

Use RAG when the model needs access to external or changing knowledge.

Use fine-tuning when you need to change behavior, style, format, classification ability, or task-specific patterns that cannot be solved reliably with prompting.

Important distinction:

```text
RAG adds knowledge at inference time.
Fine-tuning changes model behavior through training.
```

Fine-tuning should not be used as a substitute for a database of facts that changes frequently.

## 3. When Fine-Tuning May Help

Fine-tuning may help when:

- output format is repeatedly wrong despite schema/prompting;
- domain-specific style is required;
- classification labels are subtle;
- tool selection patterns are stable;
- small model needs to perform a narrow task;
- latency/cost requires a smaller adapted model.

## 4. When Fine-Tuning Is the Wrong First Step

Do not start with fine-tuning when:

- retrieval is broken;
- evaluation dataset does not exist;
- task requirements are unclear;
- data quality is poor;
- the issue is missing external knowledge;
- safety behavior is not defined;
- you cannot measure improvement.

## 5. LoRA and QLoRA

### LoRA

LoRA adds trainable low-rank adapter matrices instead of updating all model weights. This reduces training cost and storage.

### QLoRA

QLoRA applies LoRA-style adaptation on a quantized base model to reduce memory requirements.

Benefits:

- lower compute;
- lower memory;
- easier experimentation.

Risks:

- still needs high-quality data;
- can overfit;
- can degrade safety or general behavior;
- requires evaluation.

## 6. Synthetic Data

Synthetic data is generated rather than collected from real users or experts.

It can help when:

- real data is scarce;
- you need edge cases;
- you need controlled labels.

Risks:

- generated errors become training data;
- lack of diversity;
- label noise;
- bias amplification;
- unrealistic examples.

Mitigation:

- human review sample;
- deduplication;
- clear generation prompts;
- source attribution;
- holdout set from human-written data.

## 7. Preference Tuning

Preference tuning uses comparisons such as "answer A is better than answer B."

Useful for:

- style;
- helpfulness;
- refusal behavior;
- domain-specific quality preference.

It requires reliable preference labels.

## 8. Distillation

Distillation transfers behavior from a larger model to a smaller model.

Use cases:

- low-latency classifier;
- cheaper extraction model;
- routing model;
- domain-specific assistant with narrow scope.

Again, evaluation is required.

## 9. Adaptation Decision Framework

Ask:

1. Is the problem missing knowledge or wrong behavior?
2. Is retrieval already strong?
3. Is the prompt already tested?
4. Is there a golden dataset?
5. Is there enough high-quality labeled data?
6. What is the target improvement?
7. What could regress?
8. How will rollback work?

## 10. Key Takeaway

Fine-tuning is a powerful tool, but expert AI engineers treat it as a decision, not a reflex.
## Numbered References

[1] Hugging Face PEFT: https://huggingface.co/docs/transformers/peft
[2] PEFT LoRA guide: https://huggingface.co/docs/peft/developer_guides/lora
[3] Hugging Face TRL: https://huggingface.co/docs/trl/index
[4] Transformers quantization: https://huggingface.co/docs/transformers/quantization
[5] QLoRA paper: https://arxiv.org/abs/2305.14314
