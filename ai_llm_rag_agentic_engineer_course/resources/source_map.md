# Source Map

This file lists the primary sources used to expand the course. It intentionally separates official documentation, active GitHub repositories, surveys/papers, and security/operations standards. Always check the linked source before implementing production code because AI tooling changes quickly.

Last checked: 2026-05-25.

## Official API and Platform Documentation

| Area | Source | Use in course |
| --- | --- | --- |
| OpenAI platform overview | https://platform.openai.com/docs | LLM APIs, tools, structured outputs, embeddings, file search, responses |
| OpenAI Responses API | https://platform.openai.com/docs/api-reference/responses | stateful model responses, tools, agentic workflows |
| OpenAI Structured Outputs | https://platform.openai.com/docs/guides/structured-outputs | typed JSON outputs and schema reliability |
| OpenAI Embeddings | https://platform.openai.com/docs/guides/embeddings | embedding concepts and search use cases |
| OpenAI Prompt Caching | https://platform.openai.com/docs/guides/prompt-caching | latency and input-token cost optimization |
| OpenAI File Search | https://platform.openai.com/docs/guides/tools-file-search | hosted retrieval/vector-store patterns |
| FastAPI | https://fastapi.tiangolo.com/tutorial/first-steps/ | API foundations |
| FastAPI Docker deployment | https://fastapi.tiangolo.com/deployment/docker/ | containerized API deployment |
| Docker | https://docs.docker.com/ | containerization |
| GitHub Actions | https://docs.github.com/en/actions | CI/CD |
| PostgreSQL | https://www.postgresql.org/docs/ | SQL, indexes, transactions |
| pgvector | https://github.com/pgvector/pgvector | vector search inside PostgreSQL |

## RAG, Agent, and Framework Documentation

| Source | Link | Notes |
| --- | --- | --- |
| LangChain RAG guide | https://docs.langchain.com/oss/python/langchain/rag | RAG application structure |
| LangChain tools | https://docs.langchain.com/oss/python/langchain/tools | tool interfaces |
| LangGraph docs | https://docs.langchain.com/oss/python/langgraph/overview | stateful agent orchestration |
| LangGraph StateGraph reference | https://reference.langchain.com/python/langgraph/graph/state/StateGraph | graph/state API reference |
| LangGraph human-in-the-loop | https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/ | interrupts and approval flows |
| LlamaIndex RAG docs | https://developers.llamaindex.ai/python/framework/understanding/rag/ | indexing, retrieval, query engines |
| LlamaIndex evaluation docs | https://llamaindex.openml.io/python/framework/module_guides/evaluating/ | retrieval and response evaluation |
| Haystack docs | https://docs.haystack.deepset.ai/docs/pipelines | modular pipelines |
| Haystack evaluation | https://docs.haystack.deepset.ai/docs/evaluation | pipeline/component evaluation |
| Microsoft Foundry | https://learn.microsoft.com/en-us/azure/foundry/ | enterprise AI platform |
| Azure AI Foundry Agent Service | https://learn.microsoft.com/en-gb/azure/ai-foundry/agents/overview | managed agent platform |
| Microsoft Foundry evaluation | https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-generative-ai-app | evaluation workflows |

## Vector Search Documentation

| Source | Link | Notes |
| --- | --- | --- |
| Qdrant search docs | https://qdrant.tech/documentation/search/ | vector search, payloads, filters |
| Qdrant indexing docs | https://qdrant.tech/documentation/manage-data/indexing/ | payload indexes and filterable HNSW |
| Qdrant GitHub | https://github.com/qdrant/qdrant | Rust vector database, dense/sparse vectors, filtering |
| Milvus docs | https://milvus.io/docs/ | scalable vector database |
| Milvus GitHub | https://github.com/milvus-io/milvus | distributed vector database |
| Weaviate vector search | https://docs.weaviate.io/weaviate/concepts/search/vector-search | vector indexes and distance metrics |
| Weaviate hybrid search | https://weaviate.io/developers/weaviate/search/hybrid | BM25 + vector search |
| FAISS GitHub | https://github.com/facebookresearch/faiss | vector similarity search library |
| FAISS index guidelines | https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index | index selection |
| Chroma | https://docs.trychroma.com/ | local and application-focused vector database |

## Evaluation and Observability

| Source | Link | Notes |
| --- | --- | --- |
| RAGAS docs | https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/ | faithfulness, answer relevance, context metrics |
| RAGAS GitHub | https://github.com/explodinggradients/ragas | open-source RAG evaluation |
| DeepEval docs | https://deepeval.com/docs/introduction | LLM/RAG/agent testing |
| DeepEval GitHub | https://github.com/confident-ai/deepeval | pytest-like LLM evaluation framework |
| LangSmith evaluation | https://docs.langchain.com/langsmith/evaluation-concepts | traces, datasets, evaluators |
| MLflow GenAI eval | https://www.mlflow.org/docs/latest/genai/eval-monitor | evaluation and monitoring |
| MLflow tracing | https://mlflow.org/docs/latest/genai/tracing/ | traces and OpenTelemetry compatibility |
| OpenAI Evals GitHub | https://github.com/openai/evals | eval framework and benchmark registry |

## Serving, Optimization, and Fine-Tuning

| Source | Link | Notes |
| --- | --- | --- |
| vLLM serving | https://docs.vllm.ai/en/latest/serving/online_serving/ | high-throughput LLM serving |
| vLLM OpenAI-compatible server | https://docs.vllm.ai/en/latest/serving/openai_compatible_server/ | API compatibility |
| Hugging Face TGI | https://huggingface.co/docs/text-generation-inference/main/en/index | text-generation serving |
| NVIDIA Triton | https://docs.nvidia.com/deeplearning/triton-inference-server/index.html | inference server |
| Hugging Face Transformers quantization | https://huggingface.co/docs/transformers/quantization | model quantization |
| Hugging Face PEFT | https://huggingface.co/docs/transformers/peft | parameter-efficient fine-tuning |
| Hugging Face PEFT LoRA | https://huggingface.co/docs/peft/developer_guides/lora | LoRA and QLoRA |
| Hugging Face TRL | https://huggingface.co/docs/trl/index | SFT, DPO, preference tuning |
| ONNX Runtime quantization | https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html | INT8 quantization |

## Security, Safety, and Governance

| Source | Link | Notes |
| --- | --- | --- |
| OWASP Top 10 for LLM Applications | https://owasp.org/www-project-top-10-for-large-language-model-applications/ | LLM security risks |
| OWASP LLM Top 10 2025 PDF | https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf | current LLM risk list |
| NIST AI RMF | https://www.nist.gov/itl/ai-risk-management-framework | AI risk management |
| Microsoft Responsible AI | https://www.microsoft.com/en-us/ai/principles-and-approach/ | responsible AI principles |
| Azure OpenAI Responsible AI | https://learn.microsoft.com/en-us/legal/cognitive-services/openai/overview | Azure OpenAI responsible AI guidance |

## High-Signal GitHub Repositories

| Repository | Link | Why it matters |
| --- | --- | --- |
| OpenAI Cookbook | https://github.com/openai/openai-cookbook | practical API, embeddings, RAG, tool examples |
| OpenAI Agents SDK | https://github.com/openai/openai-agents-python | multi-agent workflows, tools, guardrails, handoffs |
| LangGraph | https://github.com/langchain-ai/langgraph | stateful graph-based agent orchestration |
| LangChain | https://github.com/langchain-ai/langchain | integrations and LLM app framework |
| LangGraph 101 | https://github.com/langchain-ai/langgraph-101 | structured LangGraph learning notebooks |
| LangChain Context Engineering | https://github.com/langchain-ai/context_engineering | context selection, compression, isolation |
| LlamaIndex | https://github.com/run-llama/llama_index | indexing, RAG, data connectors, workflows |
| Haystack | https://github.com/deepset-ai/haystack | modular production-oriented RAG/agent pipelines |
| RAG Techniques | https://github.com/NirDiamant/RAG_Techniques | hands-on advanced RAG techniques |
| RAG Survey | https://github.com/Tongji-KGLLM/RAG-Survey | RAG taxonomy and survey material |
| Awesome RAG | https://github.com/coree/awesome-rag | curated RAG papers/resources |
| Awesome LLM RAG | https://github.com/jxzhangjhu/Awesome-LLM-RAG | advanced RAG papers and taxonomy |
| Awesome RAG Production | https://github.com/Yigtwxx/Awesome-RAG-Production | production-oriented RAG tools and practices |
| Awesome RAG by liunian-Jay | https://github.com/liunian-Jay/Awesome-RAG | broad RAG paper/code collection |
| Awesome AI Eval | https://github.com/Vvkmnn/awesome-ai-eval | evaluation tools and reliability resources |
| Awesome AI Agents | https://github.com/slavakurilyak/awesome-ai-agents | agentic AI resource collection |
| Semantic Kernel | https://github.com/microsoft/semantic-kernel | Microsoft agent/orchestration SDK history and migration context |
| AutoGen | https://github.com/microsoft/autogen | multi-agent framework |
| CrewAI | https://github.com/crewAIInc/crewAI | role-based multi-agent workflows |
| Qdrant | https://github.com/qdrant/qdrant | production vector search engine |
| Milvus | https://github.com/milvus-io/milvus | distributed vector database |
| Weaviate | https://github.com/weaviate/weaviate | vector database with hybrid search |
| FAISS | https://github.com/facebookresearch/faiss | high-performance vector similarity search |
| DeepEval | https://github.com/confident-ai/deepeval | LLM evaluation |
| RAGAS | https://github.com/explodinggradients/ragas | RAG evaluation |

## Papers and Surveys

| Topic | Source |
| --- | --- |
| RAG survey | https://arxiv.org/abs/2312.10997 |
| RAGAS paper | https://arxiv.org/abs/2309.15217 |
| ARES RAG evaluation | https://arxiv.org/abs/2311.09476 |
| Graph RAG survey | https://arxiv.org/abs/2408.08921 |
| FlashRAG toolkit | https://arxiv.org/abs/2405.13576 |
| RAGLAB | https://arxiv.org/abs/2408.11381 |
| QLoRA | https://arxiv.org/abs/2305.14314 |

## Reliability Rule

For this course:

- Official docs are used for current API behavior.
- GitHub repositories are used for ecosystem orientation and implementation examples.
- Papers are used for concepts, taxonomy, and research direction.
- Blog posts and Reddit discussions are not used as authoritative facts unless they point to primary sources.
