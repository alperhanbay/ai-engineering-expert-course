# Lesson: Capstone, Portfolio, and Expert Interview Readiness

## 1. Purpose of the Capstone

The capstone proves that you can integrate the whole field:

- backend engineering;
- SQL data modeling;
- API design;
- Docker/CI;
- LLM prompting;
- embeddings;
- vector search;
- RAG;
- advanced retrieval;
- evaluation;
- agents;
- production monitoring;
- optimization;
- adaptation decisions;
- security and compliance.

The goal is not a toy demo. The goal is a defensible production-style system.

## 2. Recommended Capstone

Build a **Production-Style AI Knowledge and Workflow Assistant**.

Choose one domain:

- legal;
- banking;
- insurance;
- enterprise policy;
- developer documentation;
- public compliance documents.

Use synthetic or public data unless you have explicit permission to use real private data.

## 3. Required System Capabilities

### API

- health endpoint;
- document upload;
- indexing job;
- ask endpoint;
- feedback endpoint;
- eval endpoint;
- agent run endpoint.

### Data

- documents;
- chunks;
- embeddings metadata;
- request logs;
- retrieved contexts;
- generated answers;
- feedback;
- eval cases;
- audit logs.

### RAG

- parsing;
- cleaning;
- chunking;
- metadata enrichment;
- embeddings;
- vector DB;
- hybrid retrieval;
- reranking;
- grounded generation;
- citations;
- no-answer behavior.

### Agent

- stateful workflow;
- tool schemas;
- permission checks;
- human approval;
- traces;
- tool evaluation.

### Evaluation

- golden dataset;
- retrieval metrics;
- generation metrics;
- human rubric;
- regression gate;
- failure analysis.

### Production

- Docker Compose;
- logging;
- metrics;
- tracing design;
- versioning;
- incident runbook;
- rollback strategy.

### Security

- tenant-aware retrieval;
- PII policy;
- prompt injection tests;
- audit logs;
- guardrail policy;
- tool permission model.

## 4. Portfolio README

Your README should explain:

- problem;
- users;
- architecture;
- how to run;
- data model;
- RAG pipeline;
- agent workflow;
- evaluation;
- monitoring;
- security;
- tradeoffs;
- limitations.

## 5. Interview Story

Use this structure:

```text
Problem:
  What user problem did you solve?

Constraints:
  Accuracy, latency, privacy, cost, compliance.

Architecture:
  API, data, retrieval, generation, agent, eval, monitoring.

Decisions:
  Chunking, vector DB, reranking, model, framework, safety.

Evaluation:
  Golden dataset, metrics, human review, regression gate.

Production:
  Logs, monitoring, rollback, security, incident response.

Tradeoffs:
  What did you choose and why?
```

## 6. Expert Interview Expectations

You should be ready to:

- draw the architecture;
- explain every component;
- justify every major decision;
- discuss alternatives;
- debug failure scenarios;
- discuss cost/latency;
- discuss safety/compliance;
- explain what you would do next.

## 7. Final Review Questions

Before calling the capstone complete:

- Can someone run it from documentation?
- Are evaluation results included?
- Are failures discussed honestly?
- Are security risks documented?
- Are tradeoffs explicit?
- Are sources cited?
- Are limitations clear?

## 8. Key Takeaway

Your portfolio should not claim expertise. It should demonstrate it through working artifacts, evaluation evidence, and clear engineering judgment.
## Numbered References

[1] OpenAI Cookbook: https://github.com/openai/openai-cookbook
[2] LangGraph GitHub: https://github.com/langchain-ai/langgraph
[3] LlamaIndex GitHub: https://github.com/run-llama/llama_index
[4] RAG Techniques GitHub: https://github.com/NirDiamant/RAG_Techniques
[5] DeepEval GitHub: https://github.com/confident-ai/deepeval
[6] RAGAS GitHub: https://github.com/explodinggradients/ragas
