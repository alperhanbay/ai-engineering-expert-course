# AI Engineering Expert Course

This course is designed to make you strong in the field itself, not just ready for one specific job post.

The target profile is:

**Production-grade LLM, RAG, and Agentic AI Engineer**

That means you should be able to design, build, evaluate, operate, secure, and explain AI systems that use real data, real users, real latency constraints, real safety requirements, and real production feedback loops.

## What Changed

The course is now structured as an expert-track curriculum. Each chapter is treated as a standalone mini-course with:

- `README.md` - chapter entry point
- `lesson.md` - detailed topic explanation
- `deep_dive.md` - expanded expert-track lesson with current engineering problems and numbered references
- `examples.md` - examples and patterns
- `homework.md` - practice tasks
- `quiz.md` - multiple-choice and fill-in-the-blank questions
- `question_bank.md` - larger mastery set with MCQs, fill-ins, scenarios, and debugging questions
- `projects.md` - chapter-level projects
- `project_lab.md` - detailed portfolio-grade project briefs with beginner, intermediate, and advanced requirements
- `dictionary.md` - end-of-chapter glossary and mastery checks
- `resources.md` - curated official docs, GitHub repositories, papers, and references
- `references_numbered.md` - chapter-specific `[1]`, `[2]` reference list for verification
- `my_work/` - your own work, notes, assignments, and solutions

## How To Use This Course

1. Start with `syllabus/master_plan.md`.
2. Read `resources/source_map.md` to understand the ecosystem.
3. For each chapter, read:
   - `README.md`
   - `lesson.md`
   - `deep_dive.md`
   - `examples.md`
   - `question_bank.md`
   - `quiz.md`
   - `project_lab.md`
   - `projects.md`
   - `dictionary.md`
   - `resources.md`
   - `references_numbered.md`
   - `homework.md`
4. Put your answers and implementation work into the chapter's `my_work/` folder.
5. Build the capstone incrementally instead of waiting until the end.

## Expert-Level Learning Outcomes

By the end, you should be able to:

- Explain LLM fundamentals: tokens, transformers, attention, context windows, embeddings, decoding, and model selection.
- Build backend services for AI applications using Python, FastAPI, SQL, Docker, Git, and CI/CD.
- Design document ingestion pipelines with parsing, cleaning, chunking, metadata enrichment, embedding, and indexing.
- Use vector search systems such as Qdrant, Milvus, Weaviate, FAISS, Chroma, or pgvector with a clear understanding of tradeoffs.
- Build naive, modular, advanced, hybrid, reranked, and agentic RAG systems.
- Evaluate RAG systems with retrieval metrics, generation metrics, RAGAS, DeepEval, golden datasets, human review, and regression gates.
- Build tool-using agents with explicit state, routing, permissions, memory policy, traces, retries, and human approval steps.
- Use Azure/OpenAI-style enterprise AI platforms while understanding vendor-neutral architecture.
- Operate AI systems with logging, tracing, monitoring, evals, feedback loops, incident response, and rollback.
- Optimize inference with streaming, batching, prompt caching, KV-cache concepts, quantization, ONNX, vLLM, TGI, and Triton.
- Decide when to use RAG, prompt engineering, fine-tuning, LoRA/QLoRA, distillation, or a smaller task-specific model.
- Design safety and compliance layers using OWASP LLM Top 10, NIST AI RMF, access control, audit logs, PII handling, and guardrails.

## Main Capstone

The capstone is a production-style AI knowledge assistant for a regulated or high-accuracy domain.

It must include:

- API service
- SQL metadata/logging
- document ingestion
- chunking experiments
- embeddings
- vector database
- hybrid retrieval
- reranking
- grounded answer generation with citations
- agent workflow with tools
- evaluation suite
- monitoring/logging design
- security/compliance controls
- deployment documentation
- interview-ready system design explanation

## Recommended Pace

- Standard expert track: 16-20 weeks, 8-12 hours per week
- Intensive track: 10-12 weeks, 15-20 hours per week
- Interview sprint after completion: 10 days of mock interviews and system design drills

## For University Use

This repository is structured to be teachable as a senior undergraduate or
graduate elective. The instructor materials are deliberate; they let another
faculty member pick the course up cold.

- [`INSTRUCTOR.md`](INSTRUCTOR.md) — pace, common student mistakes, answer-key locations
- [`syllabus/grading_scheme.md`](syllabus/grading_scheme.md) — suggested weights for a 14-16 week semester
- [`syllabus/papers_to_read.md`](syllabus/papers_to_read.md) — required reading: ~25 seminal papers mapped to chapters
- [`ACADEMIC_INTEGRITY.md`](ACADEMIC_INTEGRITY.md) — explicit AI-tool policy (permissive but disclosed)
- [`OPEN_PROBLEMS.md`](OPEN_PROBLEMS.md) — what the field doesn't know; for honest portfolio limitations
- [`COURSE_MAP.md`](COURSE_MAP.md) — prerequisite DAG + chapter index + capstone artifacts
- [`QUALITY_CHECKS.md`](QUALITY_CHECKS.md) — what the validator enforces

## Quick AI-tool policy

You may use AI assistants for drafting, generating boilerplate, and explaining
unfamiliar APIs. You may not submit AI-generated content you have not read and
understood. **Every** `my_work/` must include an `AI tool use` acknowledgement
section. See [`ACADEMIC_INTEGRITY.md`](ACADEMIC_INTEGRITY.md) for the full policy.

## Start Here

- [`syllabus/master_plan.md`](syllabus/master_plan.md)
- [`resources/source_map.md`](resources/source_map.md)
- [`chapters/00_orientation/lesson.md`](chapters/00_orientation/lesson.md)
