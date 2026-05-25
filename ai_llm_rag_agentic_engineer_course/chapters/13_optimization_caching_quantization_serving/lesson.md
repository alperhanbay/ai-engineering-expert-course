# Lesson: Optimization, Caching, Quantization, and Serving

## 1. Why Optimization Matters

A correct AI system that is too slow or too expensive may still fail in production. Optimization balances:

- quality;
- latency;
- throughput;
- cost;
- memory;
- reliability;
- operational complexity.

Do not optimize blindly. Start with measurement.

## 2. Latency Budget

Break request latency into components:

```text
API validation
auth
query rewriting
retrieval
reranking
LLM first token
LLM full response
guardrail validation
logging
```

This identifies where optimization matters.

## 3. Streaming

Streaming sends partial output as it is generated.

Benefits:

- faster perceived response;
- better user experience for long answers.

Risks:

- harder validation;
- harder citation handling;
- partial unsafe output;
- client complexity.

## 4. Batching

Batching groups requests to improve hardware utilization.

Useful for:

- embedding jobs;
- offline evaluation;
- model serving;
- reranking.

Risk:

- batching can increase per-request latency if not managed.

## 5. Prompt Caching

Prompt caching reuses repeated prompt prefixes or static instruction blocks when supported by a provider or serving stack.

Good candidates:

- system prompt;
- static policy text;
- repeated examples;
- stable tool instructions.

Bad candidates:

- user-specific private data;
- permission-dependent context;
- frequently changing policies.

## 6. KV-Cache

During autoregressive generation, transformer models reuse key-value attention states for previously processed tokens. This is called KV-cache.

Practical impact:

- speeds generation;
- uses memory;
- important for long context;
- affects serving capacity.

You do not directly manage KV-cache in most hosted APIs, but you should understand why serving systems care about it.

## 7. Quantization

Quantization stores model weights or activations with lower precision.

Benefits:

- lower memory usage;
- sometimes faster inference;
- cheaper serving.

Risks:

- quality degradation;
- calibration issues;
- hardware/runtime constraints.

Evaluate before and after quantization.

## 8. ONNX

ONNX provides a portable model format and runtime optimizations. It is often useful for smaller models such as classifiers, rerankers, or embedding models.

Use cases:

- low-latency routing classifier;
- PII classifier;
- intent classifier;
- small extraction model.

## 9. Serving Options

### Hosted API

Best when:

- fast product path;
- managed scaling;
- enterprise compliance from provider;
- no GPU operations team.

### vLLM

Useful for high-throughput open model serving with efficient memory management and OpenAI-compatible serving options.

### TGI

Hugging Face Text Generation Inference is useful for serving supported open models in HF ecosystems.

### Triton

NVIDIA Triton is useful for production inference serving across frameworks and GPU-optimized deployments.

## 10. Optimization Strategy

Order of operations:

1. measure baseline;
2. identify bottleneck;
3. choose one optimization;
4. evaluate quality and latency;
5. monitor in production;
6. document tradeoff.

## 11. Key Takeaway

Optimization is a system-level discipline. Faster is not better if quality, safety, or maintainability collapses.
## Numbered References

[1] OpenAI prompt caching: https://platform.openai.com/docs/guides/prompt-caching
[2] vLLM online serving: https://docs.vllm.ai/en/latest/serving/online_serving/
[3] vLLM OpenAI-compatible server: https://docs.vllm.ai/en/latest/serving/openai_compatible_server/
[4] Hugging Face TGI: https://huggingface.co/docs/text-generation-inference/main/en/index
[5] NVIDIA Triton: https://docs.nvidia.com/deeplearning/triton-inference-server/index.html
[6] Transformers quantization: https://huggingface.co/docs/transformers/quantization
[7] ONNX Runtime quantization: https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html
