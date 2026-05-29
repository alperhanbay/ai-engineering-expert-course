# Master Plan: AI Engineering Expert Track

## Goal

This curriculum is not tied to one job post. It is a deep learning path for becoming an expert in production-grade LLM, RAG, and agentic AI engineering.

The course assumes that expertise means more than knowing tool names. You should be able to:

- explain the underlying concepts;
- implement working systems;
- evaluate quality with metrics;
- debug failures;
- reason about cost, latency, and reliability;
- secure the system;
- operate it in production;
- communicate tradeoffs clearly in system design discussions.

## Expert Profile

The target profile is:

**AI Engineer who can build production LLM systems end to end.**

This includes:

- backend engineering;
- data management;
- LLM and prompt engineering;
- retrieval and vector search;
- RAG architecture;
- agentic workflow design;
- evaluation and observability;
- serving and optimization;
- fine-tuning/model adaptation;
- safety, governance, and compliance.

## Course Structure

Each chapter is a mini-course:

| File | Purpose |
| --- | --- |
| `README.md` | Entry point and chapter scope |
| `lesson.md` | Detailed conceptual explanation + Mermaid diagram + Learning Objectives |
| `deep_dive.md` | Hand-authored expansion: extra diagrams, curated Further Reading |
| `examples.md` | Worked code examples and patterns |
| `homework.md` | Graded tasks with acceptance criteria |
| `quiz.md` | Multiple-choice and fill-in-the-blank questions |
| `question_bank.md` | Expanded MCQ + applied MCQ + scenarios + answer key |
| `project_lab.md` | Portfolio-grade project with concrete inputs/outputs/metrics |
| `projects.md` | Shorter alternative project briefs |
| `dictionary.md` | Glossary + hand-authored Extended Glossary with sources |
| `resources.md` | Curated official docs, GitHub repos, papers |
| `references_numbered.md` | `[1]`-style chapter-specific reference list |
| `my_work/` | Your answers, code, notes; chapter-specific worksheet README |

Beyond chapters, the repository contains:

- `syllabus/` — `master_plan.md` (this), `12_week_schedule.md`, `evaluation_rubric.md`, `progress_tracker.md`, `skill_mapping.md`, `papers_to_read.md`
- `resources/` — `source_map.md`, `official_sources.md`, `concept_glossary.md`
- `capstone/` — `README.md`, `deliverables_checklist.md`
- `interview_prep/` — `questions.md`, `mock_interview_plan.md`, `system_design_template.md`
- `supplementary/` — optional advanced labs (e.g. `05b_build_tiny_transformer/`)
- top-level `README.md`, `COURSE_MAP.md`, `QUALITY_CHECKS.md`, `INSTRUCTOR.md`, `ACADEMIC_INTEGRITY.md`, `OPEN_PROBLEMS.md`
- `tools/generate_expansion.py` and `tools/validate_course_quality.py` for maintainers

## Chapter Sequence

| Chapter | Topic | Outcome |
| ---: | --- | --- |
| 00 | Orientation and Expert Roadmap | Define your target skill map and capstone direction |
| 01 | Python Backend Foundations | Build maintainable Python services |
| 02 | SQL and Data Management | Model documents, metadata, logs, feedback, and evaluation data |
| 03 | FastAPI, REST, and Integration | Expose AI systems through stable APIs |
| 04 | Docker, Linux, Git, and CI/CD | Package, test, and deploy reproducible services |
| 05 | LLM Fundamentals and Prompting | Understand models, tokens, prompts, structured output, and context |
| 06 | Embeddings and Vector Search | Build and evaluate semantic search systems |
| 07 | RAG Pipeline Basics | Build end-to-end retrieval-augmented generation |
| 08 | Advanced RAG, Retrieval, and Reranking | Improve retrieval quality with hybrid search, reranking, routing, and experiments |
| 09 | LLM/RAG Evaluation | Build golden datasets, eval suites, and regression gates |
| 10 | Agentic AI, LangGraph, and Tool Use | Build stateful tool-using agents safely |
| 11 | Azure/OpenAI Foundry and Enterprise AI | Understand managed AI platforms and enterprise architecture |
| 12 | Production Serving, Monitoring, and MLOps | Operate AI systems with logs, metrics, traces, feedback, and incident response |
| 13 | Optimization, Caching, Quantization, and Serving | Optimize latency, cost, memory, and throughput |
| 14 | Fine-Tuning and Model Adaptation | Decide when to adapt models and how to evaluate them |
| 15 | Security, Guardrails, and Compliance | Design safe, auditable, permission-aware AI systems |
| 16 | Capstone, Portfolio, and Interview | Integrate everything into one production-style portfolio project |

## Learning Levels

### Level 1: Foundations

You can write a working AI backend service.

Required evidence:

- typed Python service;
- FastAPI endpoints;
- SQL schema;
- Docker Compose stack;
- basic LLM API call;
- simple vector search;
- basic RAG answer.

### Level 2: Applied AI Engineering

You can build a useful RAG or agentic system with evaluation.

Required evidence:

- document ingestion;
- chunking strategy;
- vector DB with metadata filtering;
- citation-aware RAG;
- evaluation dataset;
- RAGAS/DeepEval or equivalent tests;
- LangGraph-style agent workflow;
- logging and feedback capture.

### Level 3: Production AI Engineering

You can make engineering decisions under real constraints.

Required evidence:

- hybrid retrieval and reranking experiments;
- latency and cost budget;
- monitoring dashboard design;
- incident response runbook;
- rollback strategy;
- security controls;
- audit log;
- human review workflow.

### Level 4: Expert Track

You can reason about the field, compare tools, read papers, and design robust systems without depending on a single framework.

Required evidence:

- framework comparison;
- vector index tradeoff analysis;
- RAG failure taxonomy;
- domain-specific evaluation rubric;
- tool permission model;
- fine-tuning decision memo;
- production architecture document.

## Capstone

Build a **Production-Style AI Knowledge and Workflow Assistant**.

It should support:

- document ingestion;
- parsing and cleaning;
- chunking;
- metadata enrichment;
- embedding generation;
- vector indexing;
- hybrid retrieval;
- reranking;
- grounded answer generation with citations;
- agentic workflow with tool use;
- evaluation and regression testing;
- feedback loop;
- monitoring and tracing design;
- security and audit controls.

## Success Criteria

You are ready when you can answer these questions with implementation evidence:

- How does your RAG pipeline work end to end?
- How did you choose chunk size and overlap?
- How do you measure retrieval quality?
- Why did you choose your vector database?
- How do you prevent cross-tenant data leakage?
- What happens when the LLM provider fails?
- How do you detect hallucinations?
- How do you evaluate an agent, not just a final answer?
- How do you reduce latency without destroying answer quality?
- How do you decide between RAG, fine-tuning, and smaller classifiers?
- How do you roll back a bad prompt, model, or index release?

