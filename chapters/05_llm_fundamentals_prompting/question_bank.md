# Expanded Question Bank: LLM Fundamentals and Prompting

## How To Use This Bank

Answer without looking at the answer key. For every wrong answer, write one sentence explaining the concept in your own words and one sentence explaining how it appears in a production AI system.


## Multiple Choice

1. A teammate asks you to define `token` in one sentence. Which is closest?
   - A. The transformer mechanism that relates tokens to other tokens in context.
   - B. High-priority instruction that defines behavior, policies, and output expectations.
   - C. A model-processing unit produced by a tokenizer.
   - D. The maximum amount of token context a model can use in a request.

2. Pick the description of `context window` you would put in a `dictionary.md` entry.
   - A. High-priority instruction that defines behavior, policies, and output expectations.
   - B. The maximum amount of token context a model can use in a request.
   - C. A model-processing unit produced by a tokenizer.
   - D. The transformer mechanism that relates tokens to other tokens in context.

3. Which sentence is the best working definition of `attention`?
   - A. The transformer mechanism that relates tokens to other tokens in context.
   - B. A model-processing unit produced by a tokenizer.
   - C. The maximum amount of token context a model can use in a request.
   - D. High-priority instruction that defines behavior, policies, and output expectations.

4. In production AI work, what is the primary role of `system prompt`?
   - A. A model-processing unit produced by a tokenizer.
   - B. The maximum amount of token context a model can use in a request.
   - C. The transformer mechanism that relates tokens to other tokens in context.
   - D. High-priority instruction that defines behavior, policies, and output expectations.

5. A teammate asks you to define `few-shot` in one sentence. Which is closest?
   - A. The maximum amount of token context a model can use in a request.
   - B. The transformer mechanism that relates tokens to other tokens in context.
   - C. Providing examples in the prompt to shape behavior or output format.
   - D. A model-processing unit produced by a tokenizer.

6. Pick the description of `structured output` you would put in a `dictionary.md` entry.
   - A. The transformer mechanism that relates tokens to other tokens in context.
   - B. Model output constrained to a machine-readable schema.
   - C. A model-processing unit produced by a tokenizer.
   - D. The maximum amount of token context a model can use in a request.

7. Which sentence is the best working definition of `grounding`?
   - A. Constraining answers to provided evidence or sources.
   - B. A model-processing unit produced by a tokenizer.
   - C. The maximum amount of token context a model can use in a request.
   - D. The transformer mechanism that relates tokens to other tokens in context.

8. In production AI work, what is the primary role of `prompt injection`?
   - A. A model-processing unit produced by a tokenizer.
   - B. The maximum amount of token context a model can use in a request.
   - C. The transformer mechanism that relates tokens to other tokens in context.
   - D. An attack or failure where untrusted text attempts to override trusted instructions.


## Applied Multiple Choice

1. Applied case: Longer prompts can increase cost and degrade focus if context is noisy.
   - A. Set up a controlled experiment isolating `token`, capture before/after numbers, and write the result to a decision record.
   - B. Remove logging and evaluation to keep the diff small and merge faster.
   - C. Assume the largest available model will mask the underlying weakness in `token` so no system change is needed.
   - D. Skip the rollback plan; staging is close enough to production.

2. Applied case: Structured output is still a contract that needs validation and failure handling.
   - A. Assume the largest available model will mask the underlying weakness in `token` so no system change is needed.
   - B. Skip the rollback plan; staging is close enough to production.
   - C. Hard-code the new behaviour for the first failing case and call it a fix.
   - D. Add the work to the capstone as a reviewable artifact that exercises `context window` end-to-end, with tests and a trace.

3. Applied case: Prompt injection can arrive through user input, retrieved documents, or tool output.
   - A. Hard-code the new behaviour for the first failing case and call it a fix.
   - B. Ship the change without measurement because the most recent demo looked good.
   - C. Define explicit acceptance criteria, rollback steps, and a reviewer checklist tied to LLM Fundamentals and Prompting.
   - D. Skip the rollback plan; staging is close enough to production.

4. Applied case: Build a prompt registry with versioning, test cases, scores, and known failures.
   - A. Remove logging and evaluation to keep the diff small and merge faster.
   - B. Compare at least two approaches against a labelled set covering `prompt injection`, then choose on measured quality, latency, cost, and risk.
   - C. Hard-code the new behaviour for the first failing case and call it a fix.
   - D. Ship the change without measurement because the most recent demo looked good.

5. Applied case: Create a structured extraction task with schema validation and no-answer behavior.
   - A. Write a one-page design memo naming the assumption, the test that would falsify it, and the metric you'd watch in production.
   - B. Ship the change without measurement because the most recent demo looked good.
   - C. Remove logging and evaluation to keep the diff small and merge faster.
   - D. Assume the largest available model will mask the underlying weakness in `token` so no system change is needed.

6. Applied case: Build a prompt-injection test set for RAG context and tool outputs.
   - A. Remove logging and evaluation to keep the diff small and merge faster.
   - B. Assume the largest available model will mask the underlying weakness in `token` so no system change is needed.
   - C. Skip the rollback plan; staging is close enough to production.
   - D. Set up a controlled experiment isolating `token`, capture before/after numbers, and write the result to a decision record.


## Fill In The Blanks

1. Given the production failure "A prompt exceeds the context window after adding retrieved chunks.", the concept being misused is ________.
2. To handle situations where it limits how much instruction, history, retrieved data, and output can coexist, the engineering tool you reach for is ________ (watch for: The system truncates important citations without detecting it.).
3. ________ is best summarised as: The transformer mechanism that relates tokens to other tokens in context. Verification step: Design context ordering and test noise sensitivity.
4. On a system review, you find a document instruction overrides behavior because source data and instructions are mixed — the underlying chapter concept is ________.
5. It can improve consistency but consumes context and can bias outputs. A common failure looks like: Examples teach the model a pattern that fails on edge cases. The concept is ________.
6. Given the production failure "The model returns free text where the API expects JSON.", the concept being misused is ________.
7. To handle situations where it is central to RAG correctness and citation trust, the engineering tool you reach for is ________ (watch for: The answer includes a correct-sounding claim not supported by retrieved context.).
8. ________ is best summarised as: An attack or failure where untrusted text attempts to override trusted instructions. Verification step: Create adversarial tests and enforce permissions outside the model.

## Short Answer

1. If a reviewer asks 'why does `token` matter here?', what one-paragraph answer do you give? Include a metric.
2. Describe the smallest experiment that would tell you whether `context window` is correctly implemented in your system.
3. When would you intentionally *avoid* using `attention`? Name a constraint or tradeoff.
4. What does a healthy log or trace look like for `system prompt`? List the fields you would expect.
5. Explain how `few-shot` appears in the capstone, what artifact proves it, and what failure mode you would test.
6. If a reviewer asks 'why does `structured output` matter here?', what one-paragraph answer do you give? Include a metric.
7. Describe the smallest experiment that would tell you whether `grounding` is correctly implemented in your system.
8. When would you intentionally *avoid* using `prompt injection`? Name a constraint or tradeoff.

## Scenario Questions

1. Postmortem prompt: Longer prompts can increase cost and degrade focus if context is noisy. What regression test would prevent recurrence?
2. On-call triage: Structured output is still a contract that needs validation and failure handling. Walk through the first three steps you would take.
3. Incident: Prompt injection can arrive through user input, retrieved documents, or tool output. What do you inspect first, and which metric would prove the fix?
4. An engineer disables `structured output` to mitigate latency. Quality drops the next day. What evidence reverses the decision?

## Practical Debug Questions

1. What log or trace fields would help you debug a failure in `token` in this chapter's context?
2. What single metric would you watch in production when changing `few-shot`?
3. You suspect `prompt injection` is degraded. Design the smallest experiment that would falsify or confirm it in under an hour.
4. For the failure 'Longer prompts can increase cost and degrade focus if context is noisy.', sketch a rollback plan with a clear restore-point definition.
5. What artifact would you put in a portfolio README to prove competence with `token`, `context window`, `attention`?

## Answer Key

### Multiple Choice

1. C
2. B
3. A
4. D
5. C
6. B
7. A
8. D

### Applied Multiple Choice

1. A
2. D
3. C
4. B
5. A
6. D

### Fill In The Blanks

1. token
2. context window
3. attention
4. system prompt
5. few-shot
6. structured output
7. grounding
8. prompt injection

Short-answer, scenario, and debug questions should be graded against the rubric in `../../syllabus/evaluation_rubric.md`.

## References

[1] OpenAI platform documentation: https://platform.openai.com/docs
[2] OpenAI structured outputs: https://platform.openai.com/docs/guides/structured-outputs
[3] OpenAI embeddings guide: https://platform.openai.com/docs/guides/embeddings
[4] OpenAI prompt caching: https://platform.openai.com/docs/guides/prompt-caching
[5] OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
