# Dictionary: Optimization, Caching, Quantization, and Serving

Use this dictionary at the end of the chapter. Add your own examples in `my_work/dictionary_notes.md`.

| Term | Working Definition | Why It Matters | Common Failure Mode | Mastery Check |
| --- | --- | --- | --- | --- |
| `latency budget` | A target allocation of request time across components. | It guides optimization choices and prevents blind tuning. | Reranking is added without knowing where p95 latency is spent. | Measure component latency and set per-stage targets. |
| `streaming` | Sending partial model output to the client as it is generated. | It improves perceived latency but complicates safety, citations, and validation. | Unsafe text is streamed before guardrails run. | Design streaming boundaries and specify how citations and errors are emitted. |
| `batching` | Processing multiple items together for efficiency. | It improves throughput for embeddings, evals, and serving. | Batching increases user-facing latency unexpectedly. | Separate offline batching from interactive request paths. |
| `prompt caching` | Reusing repeated prompt prefixes when supported by provider or serving stack. | It can reduce latency and cost for stable instructions or schemas. | Private context is cached without tenant-aware boundaries. | Cache only safe repeated prefixes and monitor cache hit rates. |
| `KV-cache` | Cached transformer key/value attention states used during generation. | It affects serving throughput, memory, and long-context performance. | High concurrency exhausts memory due to long prompts. | Understand serving memory constraints and context length tradeoffs. |
| `quantization` | Reducing numeric precision of model weights or activations. | It lowers memory and can improve deployment economics. | Quantization degrades faithfulness on edge cases. | Run before/after evals on task-specific datasets. |
| `ONNX` | An open model format and runtime ecosystem for optimized inference. | It is useful for smaller classifiers, rerankers, or embedding components. | A routing classifier is too slow as an LLM call. | Export or evaluate a small model runtime where latency matters. |
| `vLLM` | An open-source LLM serving engine focused on high-throughput inference. | It is a common option for serving open models. | The team self-hosts without monitoring GPU memory or throughput. | Compare serving metrics and operational burden against hosted APIs. |
| `TGI` | Hugging Face Text Generation Inference server. | It provides an open-model serving path in the Hugging Face ecosystem. | Unsupported model/runtime settings cause deployment surprises. | Verify model support, batching, streaming, and metrics. |
| `Triton` | NVIDIA Triton Inference Server for production model serving. | It supports optimized serving across model formats and GPU environments. | A team uses Triton without the operational skills to maintain it. | Use it when serving requirements and team expertise justify complexity. |

## Dictionary Assignment

For each term:

1. Write a one-sentence definition in your own words.
2. Write a concrete example from your capstone (or planned capstone).
3. Write one failure mode you would test against.
4. Write one metric, test, or review check that would catch the failure.
5. Link one source from `references_numbered.md`.

## References

[1] OpenAI prompt caching: https://platform.openai.com/docs/guides/prompt-caching
[2] vLLM online serving: https://docs.vllm.ai/en/latest/serving/online_serving/
[3] vLLM OpenAI-compatible server: https://docs.vllm.ai/en/latest/serving/openai_compatible_server/
[4] Hugging Face TGI: https://huggingface.co/docs/text-generation-inference/main/en/index
[5] NVIDIA Triton: https://docs.nvidia.com/deeplearning/triton-inference-server/index.html
[6] Transformers quantization: https://huggingface.co/docs/transformers/quantization
[7] ONNX Runtime quantization: https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html
