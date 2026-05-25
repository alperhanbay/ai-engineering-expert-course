# Lesson: Orientation and Expert Roadmap

## 1. What This Field Really Is

Modern AI engineering is the discipline of turning models into reliable systems. A production LLM application is not only a prompt and a model call. It is a software system with data ingestion, retrieval, orchestration, evaluation, security, monitoring, cost controls, incident response, and product integration.

An expert AI engineer should be comfortable at four layers:

1. **Model layer**: LLMs, embeddings, rerankers, classifiers, fine-tuned models, inference behavior.
2. **Data layer**: documents, metadata, SQL, vector stores, evaluation datasets, access rules.
3. **Application layer**: APIs, services, agents, workflows, tools, user experience.
4. **Operations layer**: logging, monitoring, evaluation, deployment, rollback, security, compliance.

The most important mindset shift is this:

> The model is only one component. The system is the product.

## 2. Core System Types

### LLM Application

An application that sends user input and context to a language model and returns generated text, JSON, code, or an action plan.

Examples:

- summarization tool;
- structured extraction system;
- chatbot;
- code assistant;
- document analysis assistant.

### RAG System

Retrieval-Augmented Generation combines search with generation. The system retrieves relevant external information and gives it to the model so that the answer can be grounded in sources.

Basic flow:

```text
user question
  -> retrieve relevant context
  -> build prompt
  -> generate answer
  -> return answer with citations
```

### Agentic System

An agentic system lets the model choose and call tools, maintain state, route tasks, and participate in workflows.

Examples:

- support agent that searches policy documents and opens a ticket;
- legal assistant that retrieves statutes and drafts a memo;
- banking risk workflow that queries data and creates a review task;
- insurance assistant that checks claim rules and asks for human approval.

## 3. The Expert Skill Map

### Foundations

You need software engineering fundamentals because LLM systems still fail like normal software:

- bad schemas;
- missing validation;
- broken API contracts;
- timeouts;
- dependency failures;
- untested edge cases;
- unclear logging.

### Retrieval

Retrieval is often the largest quality driver in RAG. If the correct context is not retrieved, the model cannot reliably answer. You need embeddings, vector databases, metadata filtering, hybrid search, reranking, and retrieval metrics.

### Evaluation

Without evaluation, every model or prompt change becomes guesswork. You need golden datasets, automated evaluation, human review, regression gates, and failure analysis.

### Agent Design

Agents are useful but risky. Tool calls can change real data, expose private information, or create business actions. Expert agent design requires explicit state, tool schemas, permission boundaries, retry policies, traces, and approval flows.

### Production Operations

Production AI systems require:

- request tracing;
- latency metrics;
- token/cost tracking;
- error monitoring;
- model/prompt/index versioning;
- incident response;
- rollback;
- safety monitoring.

## 4. What “Deep Learning Journey” Means Here

For each topic, you should learn at three levels:

### Conceptual Understanding

You can explain the idea without depending on a framework.

Example:

> A cross-encoder reranker scores a query and candidate document jointly. It is slower than a bi-encoder but can produce better relevance ranking because it attends over both texts together.

### Implementation Skill

You can build it in code.

Example:

> I can retrieve top 50 chunks using vector search, rerank them, pass the top 5 to the generator, and log which chunks were used.

### Production Judgment

You can defend tradeoffs.

Example:

> I would not rerank every request if p95 latency is strict and vector retrieval already meets recall targets. I would rerank only low-confidence or high-risk queries.

## 5. Your Evidence Portfolio

Every chapter should produce evidence:

- notes;
- code;
- diagrams;
- evaluation results;
- failure analysis;
- design decisions;
- interview answers.

Your `my_work/` folders are not optional. They are the proof that you are building expertise.

## 6. Capstone Direction

Choose one capstone domain:

- legal knowledge assistant;
- banking workflow assistant;
- insurance operations assistant;
- internal enterprise knowledge assistant;
- developer documentation assistant;
- healthcare-like assistant only with synthetic/non-sensitive data.

Do not start with real private data. Use synthetic or public data unless you have explicit permission and a secure environment.

## 7. How To Study Each Chapter

Use this order:

1. Read `lesson.md`.
2. Review `examples.md`.
3. Answer `quiz.md` without looking at the answer key.
4. Complete `homework.md`.
5. Build at least one item from `projects.md`.
6. Read sources in `resources.md`.
7. Write your own summary in `my_work/summary.md`.

## 8. Definition of Expertise

You are not aiming to memorize tool names. You are aiming to become someone who can design a system when the tools change.

An expert answer usually includes:

- definition;
- system role;
- implementation approach;
- metrics;
- failure modes;
- tradeoffs;
- security implications;
- production operations.
## Numbered References

[1] OpenAI platform documentation: https://platform.openai.com/docs
[2] LangGraph overview: https://docs.langchain.com/oss/python/langgraph/overview
[3] LlamaIndex RAG overview: https://developers.llamaindex.ai/python/framework/understanding/rag/
[4] OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
