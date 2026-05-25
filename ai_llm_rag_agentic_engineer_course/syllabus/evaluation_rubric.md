# Evaluation Rubric

Use this rubric to measure whether you understand a topic at an expert-track level.

## Scoring Scale

| Score | Meaning |
| ---: | --- |
| 0 | I do not understand the topic yet |
| 1 | I can define it at a high level |
| 2 | I can run a basic example |
| 3 | I can integrate it into a project |
| 4 | I can evaluate, debug, and explain tradeoffs |
| 5 | I can design a production approach and teach the concept |

## Core Skill Rubric

| Skill | Level 3 evidence | Level 4 evidence | Level 5 evidence |
| --- | --- | --- | --- |
| Python backend | typed service with tests | clean boundaries and logs | replaceable providers and operational error model |
| SQL/data | schema for documents/logs/evals | indexes, audit, retention | data governance and incident queries |
| FastAPI | stable API contract | streaming/background jobs | versioned, secure, product-ready contract |
| Docker/CI | local stack | CI gates and release manifest | rollback-ready AI artifact versioning |
| LLM prompting | structured outputs | prompt tests and injection cases | prompt versioning and regression strategy |
| Vector search | vector DB with filters | retrieval metrics | index migration and multi-tenant strategy |
| RAG | grounded answer with citations | hybrid/reranked retrieval | failure taxonomy and production observability |
| Evaluation | golden dataset | automated eval + human rubric | release gate and failure-driven improvement loop |
| Agents | tool-using workflow | state, traces, permissions | human approval and agent-specific eval |
| Production | logs/metrics | incident runbooks | SLOs, rollback, cost and quality operations |
| Optimization | latency budget | caching/serving tradeoffs | quality-preserving performance strategy |
| Security | guardrail checklist | threat model and audit logs | compliance-ready layered controls |

## Expert Readiness Questions

You should be able to answer these clearly:

- How does RAG work end to end?
- How do chunking choices affect retrieval and generation?
- How do you measure retrieval quality?
- What is the difference between faithfulness and relevance?
- How do you evaluate an agent?
- Where should tool permissions be enforced?
- What is the difference between prompt caching and KV-cache?
- When would you use fine-tuning instead of RAG?
- How do you prevent cross-tenant retrieval?
- How do you roll back a bad prompt, model, or index release?

