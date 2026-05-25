# Concept Glossary

## LLM and Prompting

| Concept | Short Meaning | Why It Matters |
| --- | --- | --- |
| LLM | Large language model | Core text generation and reasoning component |
| Transformer | Neural architecture behind modern LLMs | Explains attention, context, and KV-cache behavior |
| Token | Unit processed by a model | Drives cost, latency, and context limits |
| Context window | Maximum token context available to the model | Limits prompt, retrieved context, history, and output |
| System prompt | High-priority behavior instruction | Defines product behavior and boundaries |
| Few-shot prompting | Examples included in the prompt | Helps with format and task behavior |
| Structured output | Schema-constrained output | Enables reliable API integration |
| Grounding | Answering from provided sources | Reduces unsupported claims |
| Hallucination | Unsupported or false output | Major risk in high-accuracy domains |

## Retrieval and RAG

| Concept | Short Meaning | Why It Matters |
| --- | --- | --- |
| RAG | Retrieval-Augmented Generation | Adds external knowledge to generation |
| Embedding | Numeric representation of text/data | Enables semantic search |
| Vector database | Stores and searches vectors | Foundation for scalable retrieval |
| Chunking | Splitting documents into retrievable units | Strongly affects retrieval quality |
| Metadata filtering | Filtering by tenant, date, type, permission, etc. | Improves relevance and security |
| Hybrid search | Combining keyword and vector search | Helps with exact terms and semantic matches |
| Bi-encoder | Encodes query and document separately | Fast first-stage retrieval |
| Cross-encoder | Scores query and document jointly | More accurate reranking |
| Reranking | Reordering retrieved candidates | Improves context quality |
| Recall@k | Relevant item appears in top k | Measures retrieval coverage |
| MRR | Rank of first relevant item | Measures ranking quality |
| NDCG | Graded relevance ranking metric | Useful for search quality |

## Agentic AI

| Concept | Short Meaning | Why It Matters |
| --- | --- | --- |
| Agent | LLM system with tools, state, and workflow | Enables task execution beyond chat |
| Tool use | Calling APIs, functions, databases, or services | Connects model to real systems |
| Routing | Choosing the correct path/tool/pipeline | Improves correctness and efficiency |
| Memory | Selected historical or persistent context | Supports continuity but adds privacy risk |
| State graph | Graph-based workflow with state transitions | Makes complex agents controllable |
| Human approval | Human checkpoint for risky actions | Reduces harm and compliance risk |

## Evaluation

| Concept | Short Meaning | Why It Matters |
| --- | --- | --- |
| Golden dataset | Known test cases | Enables regression testing |
| Faithfulness | Answer is supported by context | Detects hallucination |
| Answer relevance | Answer addresses the question | Measures usefulness |
| Context precision | Retrieved context is relevant | Detects retrieval noise |
| Context recall | Required context was retrieved | Detects retrieval misses |
| Human-in-the-loop | Expert review process | Validates domain correctness |
| Regression eval | Quality check across changes | Protects releases |

## Production and Optimization

| Concept | Short Meaning | Why It Matters |
| --- | --- | --- |
| Model serving | Exposing model inference as a service | Required for production use |
| Monitoring | Live system health and quality tracking | Detects incidents and regressions |
| Logging | Structured event records | Enables debug and audit |
| Prompt caching | Reuse repeated prompt prefixes | Reduces cost/latency when supported |
| KV-cache | Reused attention states during generation | Critical for serving performance |
| Quantization | Lower-precision model representation | Reduces memory and sometimes latency |
| ONNX | Portable optimized model format | Useful for smaller models/classifiers |
| vLLM | High-throughput LLM serving stack | Open-model serving option |
| TGI | Hugging Face text generation server | Open-model serving option |
| Triton | NVIDIA inference server | Production GPU serving option |

## Security and Compliance

| Concept | Short Meaning | Why It Matters |
| --- | --- | --- |
| PII | Personally identifiable information | Must be protected |
| RBAC | Role-based access control | Controls who can access what |
| Audit log | Tamper-resistant record of actions | Supports compliance and investigations |
| Prompt injection | Untrusted input tries to override instructions | Major LLM application risk |
| Guardrail | System control for safety and policy | Reduces unsafe outputs/actions |
| Tenant isolation | Separation between organizations/users | Prevents data leakage |

