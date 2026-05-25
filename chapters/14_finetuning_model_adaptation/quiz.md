# Quiz: Fine-Tuning and Model Adaptation

## Multiple Choice

1. What is the main difference between RAG and fine-tuning?
   - A. RAG adds external knowledge at inference time; fine-tuning changes model behavior through training
   - B. RAG always trains the model
   - C. Fine-tuning is only SQL
   - D. They are identical

2. When is fine-tuning a poor first step?
   - A. Retrieval is broken and no evaluation dataset exists
   - B. You have strong evaluation and high-quality labels
   - C. You have a narrow repeated task
   - D. You understand rollback

3. What does LoRA reduce?
   - A. The number of trainable parameters
   - B. The need for data quality
   - C. All hallucination automatically
   - D. All evaluation

4. What is a risk of synthetic data?
   - A. It may contain generated errors or bias
   - B. It always improves quality
   - C. It removes the need for validation
   - D. It cannot be duplicated

5. Distillation is often used to:
   - A. transfer behavior from a larger model to a smaller model
   - B. delete prompts
   - C. replace all databases
   - D. remove tests

## Fill in the Blanks

1. Fine-tuning should be evaluated before and ________ training.
2. QLoRA applies LoRA on a ________ base model.
3. Preference tuning uses comparisons between candidate ________.
4. Synthetic data should be checked for label noise and ________.
5. Adaptation decisions require a measurable target ________.

## Short Answer

1. Give three cases where RAG is better than fine-tuning.
2. Give three cases where a small classifier may be better than an LLM call.
3. Write a fine-tuning decision memo outline.

## Answer Key

### Multiple Choice

1. A
2. A
3. A
4. A
5. A

### Fill in the Blanks

1. after
2. quantized
3. outputs
4. bias
5. improvement

