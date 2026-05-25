# Claude Handoff Prompt: AI Engineering Expert Course Workspace

Copy the full prompt below into Claude. It is written as an instruction packet for improving this workspace.

---

You are Claude, acting as a senior curriculum engineer, AI systems engineer, technical editor, and open-source repository maintainer.

You are being given a workspace that contains a deep English-language curriculum named **AI Engineering Expert Course**. Your job is to improve it carefully, verify claims, remove generic content, and turn it into a repository that could credibly become a high-quality public GitHub project.

## Absolute Goal

Improve the course so that a learner can become genuinely strong in **production-grade LLM, RAG, and agentic AI engineering**, not merely memorize tool names.

The course must help the learner advance from fundamentals to advanced system design through:

- detailed lessons;
- deep dives;
- question banks;
- project labs;
- dictionaries/glossaries;
- numbered references;
- capstone artifacts;
- evaluation and validation scripts.

This must be a serious engineering learning path, not a shallow list of buzzwords.

## Current Workspace Root

The relevant project lives under:

```text
/home/alperhan/Career/aiCareer/ai_llm_rag_agentic_engineer_course
```

There is also a handoff prompt at:

```text
/home/alperhan/Career/aiCareer/CLAUDE_HANDOFF_PROMPT.md
```

## Current Course Identity

Course name:

```text
AI Engineering Expert Course
```

Target profile:

```text
Production-grade LLM, RAG, and Agentic AI Engineer
```

The course should cover:

- Python backend engineering;
- SQL and metadata systems;
- FastAPI and REST integration;
- Docker, Linux, Git, CI/CD;
- LLM fundamentals and prompting;
- embeddings and vector search;
- RAG pipelines;
- advanced RAG, hybrid retrieval, reranking, routing;
- LLM/RAG evaluation with RAGAS, DeepEval, human review, golden datasets;
- agentic AI, LangGraph-style stateful workflows, tool use, memory, human approval;
- Azure/OpenAI-style enterprise AI architecture;
- production serving, monitoring, MLOps/LLMOps;
- optimization, caching, quantization, ONNX, vLLM, TGI, Triton;
- fine-tuning, LoRA/QLoRA, synthetic data, model adaptation;
- security, OWASP LLM risks, guardrails, PII, audit logs, compliance;
- capstone, portfolio, and interview readiness.

## Important History

The course has already gone through several iterations. There were two quality problems that must **not** be repeated:

1. `dictionary.md` files previously had generic repeated definitions like:

   ```text
   A core term in Python Backend Foundations that must be defined...
   ```

   This is unacceptable. Every dictionary term must have a specific, meaningful definition, relevance, failure mode, and mastery check.

2. `question_bank.md` files previously had repetitive fill-in-the-blank questions like:

   ```text
   To master AI engineering, document its definition, implementation role, failure mode, metric, and ________ reference.
   ```

   This is unacceptable. Fill-in questions must be concept-specific, useful, and non-repetitive.

There is now a validation script designed to catch these problems:

```bash
python3 ai_llm_rag_agentic_engineer_course/tools/validate_course_quality.py
```

Run it after any generation or edit.

Current validation result before this handoff:

```text
course quality validation passed
```

## Current File Structure

Top-level project files:

```text
ai_llm_rag_agentic_engineer_course/
  README.md
  syllabus/
  resources/
  chapters/
  capstone/
  interview_prep/
  templates/
  tools/
```

Key course-level files:

```text
README.md
syllabus/master_plan.md
syllabus/12_week_schedule.md
syllabus/evaluation_rubric.md
syllabus/progress_tracker.md
syllabus/skill_mapping.md
resources/source_map.md
resources/official_sources.md
resources/concept_glossary.md
capstone/README.md
capstone/deliverables_checklist.md
interview_prep/questions.md
interview_prep/mock_interview_plan.md
interview_prep/system_design_template.md
```

Tools:

```text
tools/generate_expansion.py
tools/validate_course_quality.py
```

The generator creates or updates:

- `deep_dive.md`
- `question_bank.md`
- `project_lab.md`
- `dictionary.md`
- `references_numbered.md`
- chapter `README.md`
- numbered reference section in `lesson.md`

The validator catches generic repeated content and basic structural failures.

## Current Chapter Structure

There are 17 chapters:

```text
00_orientation
01_python_backend_foundations
02_sql_data_management
03_fastapi_rest_integration
04_docker_linux_git_cicd
05_llm_fundamentals_prompting
06_embeddings_vector_search
07_rag_pipeline_basics
08_advanced_rag_retrieval_reranking
09_llm_evaluation_ragas_deepeval
10_agentic_ai_langgraph_tool_use
11_azure_openai_foundry_semantic_kernel
12_production_serving_monitoring_mlops
13_optimization_caching_quantization_serving
14_finetuning_model_adaptation
15_security_guardrails_compliance
16_capstone_interview_portfolio
```

Each chapter currently contains:

```text
README.md
lesson.md
deep_dive.md
examples.md
homework.md
quiz.md
question_bank.md
projects.md
project_lab.md
dictionary.md
resources.md
references_numbered.md
my_work/README.md
```

Current coverage was verified:

- 17/17 `README.md`
- 17/17 `lesson.md`
- 17/17 `deep_dive.md`
- 17/17 `question_bank.md`
- 17/17 `project_lab.md`
- 17/17 `dictionary.md`
- 17/17 `references_numbered.md`

## Current README Study Order

Each chapter is intended to be read in this order:

```text
README.md
lesson.md
deep_dive.md
examples.md
question_bank.md
quiz.md
project_lab.md
projects.md
dictionary.md
resources.md
references_numbered.md
homework.md
```

## Quality Bar

You must raise the course quality. Do **not** simply generate more text. The course should feel like a serious, reviewable engineering curriculum.

For every improvement:

- Be specific.
- Avoid generic filler.
- Use verifiable claims.
- Prefer official documentation, active GitHub repositories, or primary papers.
- Add numbered references like `[1]`, `[2]` where claims depend on external sources.
- Avoid claims about APIs, model behavior, tool features, or pricing unless verified.
- Keep documentation English-only.
- Keep the course framework-neutral where possible.
- Do not turn the course into a vendor advertisement.
- Do not remove validation scripts.
- Do not reintroduce repeated generic question patterns.

## Required Development Rules

Use local files first. Inspect before editing.

Recommended commands:

```bash
find ai_llm_rag_agentic_engineer_course -maxdepth 3 -type f | sort
sed -n '1,220p' ai_llm_rag_agentic_engineer_course/README.md
python3 ai_llm_rag_agentic_engineer_course/tools/validate_course_quality.py
```

After edits, run:

```bash
python3 ai_llm_rag_agentic_engineer_course/tools/validate_course_quality.py
```

Also run searches for obvious bad patterns:

```bash
rg -n "To master .*document its definition|A core term in|Beginner Level|Intermediate Level|Advanced Level" ai_llm_rag_agentic_engineer_course/chapters
rg -n "[ğüşöçıİĞÜŞÖÇ]" ai_llm_rag_agentic_engineer_course
```

Expected:

- validation passes;
- no old generic patterns in chapter docs;
- no Turkish characters in course docs unless explicitly justified.

## Current Source Map

The source catalog is:

```text
resources/source_map.md
```

It includes official docs and repositories such as:

- OpenAI Platform Docs;
- OpenAI Cookbook;
- OpenAI Agents SDK;
- FastAPI;
- Pydantic;
- Docker;
- PostgreSQL;
- pgvector;
- LangChain;
- LangGraph;
- LlamaIndex;
- Haystack;
- Microsoft Foundry;
- Azure AI Foundry Agent Service;
- Semantic Kernel;
- AutoGen;
- CrewAI;
- Qdrant;
- Milvus;
- Weaviate;
- FAISS;
- Chroma;
- RAGAS;
- DeepEval;
- LangSmith;
- MLflow;
- OpenTelemetry;
- Prometheus;
- Grafana;
- vLLM;
- Hugging Face TGI;
- NVIDIA Triton;
- Hugging Face PEFT;
- Hugging Face TRL;
- ONNX Runtime;
- OWASP Top 10 for LLM Applications;
- NIST AI Risk Management Framework;
- Microsoft Responsible AI.

When you need current API details, verify from official docs, not memory.

## High-Priority Improvement Tasks

Work through these in order.

### Task 1: Audit Generated Content

Inspect representative files:

```text
chapters/00_orientation/question_bank.md
chapters/01_python_backend_foundations/question_bank.md
chapters/01_python_backend_foundations/dictionary.md
chapters/05_llm_fundamentals_prompting/deep_dive.md
chapters/08_advanced_rag_retrieval_reranking/project_lab.md
chapters/09_llm_evaluation_ragas_deepeval/project_lab.md
chapters/10_agentic_ai_langgraph_tool_use/deep_dive.md
chapters/15_security_guardrails_compliance/dictionary.md
```

Find:

- generic phrasing;
- repeated patterns;
- shallow questions;
- missing answer keys;
- vague project requirements;
- unsupported technical claims;
- outdated references;
- missing links.

Fix the root generator when the issue is generated.

### Task 2: Improve `generate_expansion.py`

The generator is useful but still somewhat template-driven.

Improve it so that generated files are more content-specific:

- `question_bank.md` should have richer concept-specific questions.
- Fill-in-the-blank questions should not all share the same sentence structure.
- Applied MCQs should be specific to the chapter, not reusable boilerplate.
- Scenario questions should include realistic production situations.
- `project_lab.md` should contain project-specific artifacts, datasets, test cases, metrics, and acceptance criteria.
- `dictionary.md` should remain concept-specific.
- `deep_dive.md` should remain useful and not repeat `lesson.md` too much.

If you edit generated files directly, also update the generator or document why direct editing was intentional.

### Task 3: Expand Validation

Improve:

```text
tools/validate_course_quality.py
```

It should catch:

- repeated fill-in question structures;
- duplicate question text within a file;
- generic dictionary definitions;
- missing numbered references;
- missing answer key sections;
- too-short dictionaries;
- too-short project labs;
- `deep_dive.md` files that do not include production failure modes;
- chapters missing any required file.

Validation should fail loudly with useful messages.

### Task 4: Improve Lessons

The `lesson.md` files are currently useful but should be upgraded.

Each lesson should ideally include:

- conceptual explanation;
- why it matters;
- implementation pattern;
- common mistakes;
- production failure modes;
- testing/evaluation approach;
- security or privacy consideration where relevant;
- references at the end using `[1]` format.

Do this carefully. Do not blindly expand every file with filler.

Priority chapters for lesson improvement:

1. `05_llm_fundamentals_prompting`
2. `06_embeddings_vector_search`
3. `07_rag_pipeline_basics`
4. `08_advanced_rag_retrieval_reranking`
5. `09_llm_evaluation_ragas_deepeval`
6. `10_agentic_ai_langgraph_tool_use`
7. `12_production_serving_monitoring_mlops`
8. `15_security_guardrails_compliance`

### Task 5: Make Project Labs More Real

Current `project_lab.md` files are structured, but still need more domain realism.

For each chapter, make projects feel like real portfolio-grade work:

- include concrete scenario;
- define input data;
- define output artifacts;
- define test cases;
- define metrics;
- define failure cases;
- define expected README section;
- include references.

Examples:

For vector search:

- compare Qdrant, FAISS, pgvector, and Weaviate on the same labeled retrieval set;
- include metadata filtering tests;
- measure Recall@5, MRR, latency;
- write index migration plan.

For RAG:

- use synthetic or public documents;
- implement ingestion, chunking, embeddings, retrieval, answer generation, citations;
- evaluate citation correctness and no-answer behavior.

For agentic AI:

- define tools with permission boundaries;
- create state schema;
- test wrong-tool calls, unauthorized tool calls, prompt injection through tool output, human approval.

For security:

- build threat model;
- build OWASP LLM Top 10 mapping;
- create guardrail test suite;
- design audit logs;
- define PII handling.

### Task 6: Improve Question Banks

Question banks should include:

- MCQ definitions;
- MCQ applied design decisions;
- fill-in-the-blank;
- short answer;
- scenario debugging;
- system design;
- code/design review prompts;
- answer key;
- rubric notes.

They must be varied, not template repetition.

Use the dictionary term data as a base, but write questions that require reasoning.

### Task 7: Improve Dictionaries

Dictionaries should be more than a glossary.

Each term should include:

- working definition;
- why it matters;
- common failure mode;
- mastery check;
- related terms;
- source reference if tool-specific.

If adding columns makes tables too wide, use subsections instead of giant tables.

### Task 8: Improve Source References

Make references more useful:

- Keep chapter-specific `references_numbered.md`.
- Ensure lesson/deep_dive/project_lab files end with numbered references.
- Prefer official docs and active GitHub repos.
- Add primary papers where appropriate.
- Avoid random blogs unless clearly marked as supplemental.
- If a source is unstable or version-sensitive, say so.

### Task 9: Improve Course Navigation

The repo should be pleasant to use.

Consider adding:

- `COURSE_MAP.md`
- `CONTRIBUTING.md`
- `QUALITY_CHECKS.md`
- `ROADMAP.md`
- `GITHUB_REPO_README_DRAFT.md`
- chapter index table with links;
- project index table;
- source index table;
- validation instructions.

Do not overdo it with decorative content. Keep it engineering-focused.

## Current Validation Script

Current file:

```text
tools/validate_course_quality.py
```

Current purpose:

- checks forbidden generic patterns;
- checks duplicate fill-in lines;
- checks minimum question counts;
- checks dictionary/deep dive patterns.

Improve this script as you improve the course.

## Current Generator

Current file:

```text
tools/generate_expansion.py
```

Important:

- It contains `TERM_DETAILS`, which maps concepts to:
  - definition;
  - relevance;
  - failure mode;
  - mastery check.
- It generates dictionaries and deep dives from this map.
- It appends numbered references to lessons.

If you add new concepts, update `TERM_DETAILS`.

If you modify generated structure, run:

```bash
python3 ai_llm_rag_agentic_engineer_course/tools/generate_expansion.py
python3 ai_llm_rag_agentic_engineer_course/tools/validate_course_quality.py
```

## Non-Negotiable Quality Requirements

Do not produce:

- repeated template filler;
- identical dictionary rows;
- identical fill-in questions;
- generic "advanced" language without concrete artifacts;
- unsupported claims;
- fake citations;
- invented tool capabilities;
- outdated API instructions;
- vendor-specific lock-in unless the chapter is explicitly about that vendor;
- Turkish course documentation.

Do produce:

- specific explanations;
- real failure modes;
- testable acceptance criteria;
- references;
- project artifacts;
- source-backed reasoning;
- validation checks.

## Recommended First Pass

Start with these commands:

```bash
cd /home/alperhan/Career/aiCareer
python3 ai_llm_rag_agentic_engineer_course/tools/validate_course_quality.py
sed -n '1,220p' ai_llm_rag_agentic_engineer_course/README.md
sed -n '1,220p' ai_llm_rag_agentic_engineer_course/chapters/01_python_backend_foundations/question_bank.md
sed -n '1,120p' ai_llm_rag_agentic_engineer_course/chapters/01_python_backend_foundations/dictionary.md
sed -n '1,180p' ai_llm_rag_agentic_engineer_course/chapters/08_advanced_rag_retrieval_reranking/project_lab.md
sed -n '1,180p' ai_llm_rag_agentic_engineer_course/tools/generate_expansion.py
```

Then inspect:

```bash
rg -n "To master .*document its definition|A core term in|Beginner Level|Intermediate Level|Advanced Level" ai_llm_rag_agentic_engineer_course/chapters
rg -n "source-backed|portfolio-grade|production tradeoffs" ai_llm_rag_agentic_engineer_course/chapters
```

The second search is not necessarily an error. It helps you find recurring template phrases that may deserve manual improvement.

## Example of Desired Rewrite Quality

Bad:

```text
To master vector search, document its definition, implementation role, failure mode, metric, and source reference.
```

Good:

```text
A retriever returns semantically similar chunks, but the correct policy clause is ranked 17th and never reaches the prompt. Which metric best captures this ranking problem, and what experiment would you run before adding a cross-encoder reranker?
```

Bad:

```text
Reranking is important for production tradeoffs.
```

Good:

```text
Reranking improves candidate ordering after first-stage retrieval, but it adds latency and cost. In a production RAG system, measure Recall@k before reranking, MRR/NDCG after reranking, and p95 latency for the full `/ask` path. Use reranking when first-stage recall is acceptable but the answer-supporting chunk is often ranked below the context cutoff.
```

## Desired End State

The final course should feel like:

- a serious open-source AI engineering curriculum;
- a portfolio builder;
- a system design training path;
- a source-backed reference library;
- a project-based path from fundamentals to advanced production AI engineering.

It should be good enough that a strong learner can start anywhere, understand the prerequisite concepts from the local material, and progress toward advanced competence through projects, evals, and capstone artifacts.

## Final Response Expected From You

When you finish your work, summarize:

- files changed;
- content quality improvements;
- validation results;
- remaining gaps;
- recommended next steps.

Do not claim the course is perfect. Be precise and honest.

---

End of handoff prompt.

