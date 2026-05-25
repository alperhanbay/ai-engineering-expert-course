# Dictionary: LLM Fundamentals and Prompting

Use this dictionary at the end of the chapter. Add your own examples in `my_work/dictionary_notes.md`.

| Term | Working Definition | Why It Matters | Common Failure Mode | Mastery Check |
| --- | --- | --- | --- | --- |
| `token` | A model-processing unit produced by a tokenizer. | Tokens drive cost, latency, context limits, and chunking budgets. | A prompt exceeds the context window after adding retrieved chunks. | Estimate token budgets for system prompt, history, context, question, and answer. |
| `context window` | The maximum amount of token context a model can use in a request. | It limits how much instruction, history, retrieved data, and output can coexist. | The system truncates important citations without detecting it. | Track prompt length and define context packing rules. |
| `attention` | The transformer mechanism that relates tokens to other tokens in context. | It explains why irrelevant context can distract the model and why KV-cache matters. | The model uses irrelevant retrieved text because it was packed near the answer area. | Design context ordering and test noise sensitivity. |
| `system prompt` | High-priority instruction that defines behavior, policies, and output expectations. | It controls role, scope, refusal rules, citation policy, and safety constraints. | A document instruction overrides behavior because source data and instructions are mixed. | Separate trusted instructions from untrusted retrieved content. |
| `few-shot` | Providing examples in the prompt to shape behavior or output format. | It can improve consistency but consumes context and can bias outputs. | Examples teach the model a pattern that fails on edge cases. | Compare zero-shot, few-shot, and schema-guided variants with eval cases. |
| `structured output` | Model output constrained to a machine-readable schema. | It makes downstream parsing, tool calls, extraction, and evaluation safer. | The model returns free text where the API expects JSON. | Validate schema adherence and define fallback for parse failures. |
| `grounding` | Constraining answers to provided evidence or sources. | It is central to RAG correctness and citation trust. | The answer includes a correct-sounding claim not supported by retrieved context. | Require citations and evaluate faithfulness against context. |
| `prompt injection` | An attack or failure where untrusted text attempts to override trusted instructions. | RAG and tools introduce untrusted content into model context. | A retrieved document says to ignore policy and reveal private data. | Create adversarial tests and enforce permissions outside the model. |

## Dictionary Assignment

For each term:

1. Write a one-sentence definition in your own words.
2. Write a concrete example from your capstone (or planned capstone).
3. Write one failure mode you would test against.
4. Write one metric, test, or review check that would catch the failure.
5. Link one source from `references_numbered.md`.

## References

[1] OpenAI platform documentation: https://platform.openai.com/docs
[2] OpenAI structured outputs: https://platform.openai.com/docs/guides/structured-outputs
[3] OpenAI embeddings guide: https://platform.openai.com/docs/guides/embeddings
[4] OpenAI prompt caching: https://platform.openai.com/docs/guides/prompt-caching
[5] OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
