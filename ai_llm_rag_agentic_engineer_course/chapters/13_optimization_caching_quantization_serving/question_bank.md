# Expanded Question Bank: Optimization, Caching, Quantization, and Serving

## How To Use This Bank

Answer without looking at the answer key. For every wrong answer, write one sentence explaining the concept in your own words and one sentence explaining how it appears in a production AI system.


## Multiple Choice

1. A teammate asks you to define `latency budget` in one sentence. Which is closest?
   - A. Processing multiple items together for efficiency.
   - B. Reusing repeated prompt prefixes when supported by provider or serving stack.
   - C. A target allocation of request time across components.
   - D. Sending partial model output to the client as it is generated.

2. Pick the description of `streaming` you would put in a `dictionary.md` entry.
   - A. Reusing repeated prompt prefixes when supported by provider or serving stack.
   - B. Sending partial model output to the client as it is generated.
   - C. A target allocation of request time across components.
   - D. Processing multiple items together for efficiency.

3. Which sentence is the best working definition of `batching`?
   - A. Processing multiple items together for efficiency.
   - B. A target allocation of request time across components.
   - C. Sending partial model output to the client as it is generated.
   - D. Reusing repeated prompt prefixes when supported by provider or serving stack.

4. In production AI work, what is the primary role of `prompt caching`?
   - A. A target allocation of request time across components.
   - B. Sending partial model output to the client as it is generated.
   - C. Processing multiple items together for efficiency.
   - D. Reusing repeated prompt prefixes when supported by provider or serving stack.

5. A teammate asks you to define `KV-cache` in one sentence. Which is closest?
   - A. Sending partial model output to the client as it is generated.
   - B. Processing multiple items together for efficiency.
   - C. Cached transformer key/value attention states used during generation.
   - D. A target allocation of request time across components.

6. Pick the description of `quantization` you would put in a `dictionary.md` entry.
   - A. Processing multiple items together for efficiency.
   - B. Reducing numeric precision of model weights or activations.
   - C. A target allocation of request time across components.
   - D. Sending partial model output to the client as it is generated.

7. Which sentence is the best working definition of `ONNX`?
   - A. An open model format and runtime ecosystem for optimized inference.
   - B. A target allocation of request time across components.
   - C. Sending partial model output to the client as it is generated.
   - D. Processing multiple items together for efficiency.

8. In production AI work, what is the primary role of `vLLM`?
   - A. A target allocation of request time across components.
   - B. Sending partial model output to the client as it is generated.
   - C. Processing multiple items together for efficiency.
   - D. An open-source LLM serving engine focused on high-throughput inference.

9. A teammate asks you to define `TGI` in one sentence. Which is closest?
   - A. Sending partial model output to the client as it is generated.
   - B. Processing multiple items together for efficiency.
   - C. Hugging Face Text Generation Inference server.
   - D. A target allocation of request time across components.

10. Pick the description of `Triton` you would put in a `dictionary.md` entry.
   - A. Processing multiple items together for efficiency.
   - B. NVIDIA Triton Inference Server for production model serving.
   - C. A target allocation of request time across components.
   - D. Sending partial model output to the client as it is generated.


## Applied Multiple Choice

1. Applied case: Streaming improves perceived latency but complicates validation and citations.
   - A. Set up a controlled experiment isolating `latency budget`, capture before/after numbers, and write the result to a decision record.
   - B. Assume the largest available model will mask the underlying weakness in `latency budget` so no system change is needed.
   - C. Skip the rollback plan; staging is close enough to production.
   - D. Hard-code the new behaviour for the first failing case and call it a fix.

2. Applied case: Caching can leak data if keys ignore tenant or permission context.
   - A. Skip the rollback plan; staging is close enough to production.
   - B. Hard-code the new behaviour for the first failing case and call it a fix.
   - C. Ship the change without measurement because the most recent demo looked good.
   - D. Add the work to the capstone as a reviewable artifact that exercises `streaming` end-to-end, with tests and a trace.

3. Applied case: Quantization and serving changes require before/after quality evaluation.
   - A. Ship the change without measurement because the most recent demo looked good.
   - B. Remove logging and evaluation to keep the diff small and merge faster.
   - C. Define explicit acceptance criteria, rollback steps, and a reviewer checklist tied to Optimization, Caching, Quantization, and Serving.
   - D. Hard-code the new behaviour for the first failing case and call it a fix.

4. Applied case: Instrument a RAG request and create a latency budget with p50/p95 measurements.
   - A. Assume the largest available model will mask the underlying weakness in `latency budget` so no system change is needed.
   - B. Compare at least two approaches against a labelled set covering `Triton`, then choose on measured quality, latency, cost, and risk.
   - C. Ship the change without measurement because the most recent demo looked good.
   - D. Remove logging and evaluation to keep the diff small and merge faster.

5. Applied case: Design a cache strategy with keys, TTLs, invalidation, and security risks.
   - A. Write a one-page design memo naming the assumption, the test that would falsify it, and the metric you'd watch in production.
   - B. Remove logging and evaluation to keep the diff small and merge faster.
   - C. Assume the largest available model will mask the underlying weakness in `latency budget` so no system change is needed.
   - D. Skip the rollback plan; staging is close enough to production.

6. Applied case: Compare hosted API, vLLM, TGI, and Triton using a decision matrix.
   - A. Assume the largest available model will mask the underlying weakness in `latency budget` so no system change is needed.
   - B. Skip the rollback plan; staging is close enough to production.
   - C. Hard-code the new behaviour for the first failing case and call it a fix.
   - D. Set up a controlled experiment isolating `latency budget`, capture before/after numbers, and write the result to a decision record.


## Fill In The Blanks

1. To handle situations where it guides optimization choices and prevents blind tuning, the engineering tool you reach for is ________ (watch for: Reranking is added without knowing where p95 latency is spent.).
2. ________ is best summarised as: Sending partial model output to the client as it is generated. Verification step: Design streaming boundaries and specify how citations and errors are emitted.
3. On a system review, you find batching increases user-facing latency unexpectedly — the underlying chapter concept is ________.
4. It can reduce latency and cost for stable instructions or schemas. A common failure looks like: Private context is cached without tenant-aware boundaries. The concept is ________.
5. Given the production failure "High concurrency exhausts memory due to long prompts.", the concept being misused is ________.
6. To handle situations where it lowers memory and can improve deployment economics, the engineering tool you reach for is ________ (watch for: Quantization degrades faithfulness on edge cases.).
7. ________ is best summarised as: An open model format and runtime ecosystem for optimized inference. Verification step: Export or evaluate a small model runtime where latency matters.
8. On a system review, you find the team self-hosts without monitoring GPU memory or throughput — the underlying chapter concept is ________.
9. It provides an open-model serving path in the Hugging Face ecosystem. A common failure looks like: Unsupported model/runtime settings cause deployment surprises. The concept is ________.
10. Given the production failure "A team uses Triton without the operational skills to maintain it.", the concept being misused is ________.

## Short Answer

1. Describe the smallest experiment that would tell you whether `latency budget` is correctly implemented in your system.
2. When would you intentionally *avoid* using `streaming`? Name a constraint or tradeoff.
3. What does a healthy log or trace look like for `batching`? List the fields you would expect.
4. Explain how `prompt caching` appears in the capstone, what artifact proves it, and what failure mode you would test.
5. If a reviewer asks 'why does `KV-cache` matter here?', what one-paragraph answer do you give? Include a metric.
6. Describe the smallest experiment that would tell you whether `quantization` is correctly implemented in your system.
7. When would you intentionally *avoid* using `ONNX`? Name a constraint or tradeoff.
8. What does a healthy log or trace look like for `vLLM`? List the fields you would expect.
9. Explain how `TGI` appears in the capstone, what artifact proves it, and what failure mode you would test.
10. If a reviewer asks 'why does `Triton` matter here?', what one-paragraph answer do you give? Include a metric.

## Scenario Questions

1. Postmortem prompt: Streaming improves perceived latency but complicates validation and citations. What regression test would prevent recurrence?
2. On-call triage: Caching can leak data if keys ignore tenant or permission context. Walk through the first three steps you would take.
3. Incident: Quantization and serving changes require before/after quality evaluation. What do you inspect first, and which metric would prove the fix?
4. A pull request modifies `quantization` and a downstream quality metric drops. What rollback, evaluation, and documentation do you require before merge?

## Practical Debug Questions

1. What log or trace fields would help you debug a failure in `latency budget` in this chapter's context?
2. What single metric would you watch in production when changing `quantization`?
3. You suspect `Triton` is degraded. Design the smallest experiment that would falsify or confirm it in under an hour.
4. For the failure 'Streaming improves perceived latency but complicates validation and citations.', sketch a rollback plan with a clear restore-point definition.
5. What artifact would you put in a portfolio README to prove competence with `latency budget`, `streaming`, `batching`?

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
9. C
10. B

### Applied Multiple Choice

1. A
2. D
3. C
4. B
5. A
6. D

### Fill In The Blanks

1. latency budget
2. streaming
3. batching
4. prompt caching
5. KV-cache
6. quantization
7. ONNX
8. vLLM
9. TGI
10. Triton

Short-answer, scenario, and debug questions should be graded against the rubric in `../../syllabus/evaluation_rubric.md`.

## References

[1] OpenAI prompt caching: https://platform.openai.com/docs/guides/prompt-caching
[2] vLLM online serving: https://docs.vllm.ai/en/latest/serving/online_serving/
[3] vLLM OpenAI-compatible server: https://docs.vllm.ai/en/latest/serving/openai_compatible_server/
[4] Hugging Face TGI: https://huggingface.co/docs/text-generation-inference/main/en/index
[5] NVIDIA Triton: https://docs.nvidia.com/deeplearning/triton-inference-server/index.html
[6] Transformers quantization: https://huggingface.co/docs/transformers/quantization
[7] ONNX Runtime quantization: https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html
