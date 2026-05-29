# Instructor's Guide

For faculty adopting this course. The repo is designed to be teachable by
someone other than the original author — this document captures the
non-obvious knowledge needed to run it well.

## Course identity

| | |
| --- | --- |
| Level | senior undergraduate (4th year) or graduate elective |
| Prerequisites | one ML/AI course OR strong Python + linear algebra; familiarity with HTTP/SQL |
| Best fit | a 14-16 week semester, project-heavy |
| What it is NOT | a first ML course; a deep-learning fundamentals course |

If your students have not seen tensors, gradient descent, or a softmax before,
pair this with a foundations course (CS231N / CS224N / DeepLearning.AI's
specialization) or expand chapter 05 with a fundamentals primer week.

## Suggested calendar (14-week semester)

| Week | Chapter | Notes |
| --- | --- | --- |
| 1 | 00 Orientation | proposal due end of week 1 |
| 2 | 01 Python backend | service skeleton due |
| 3 | 02 SQL data management | schema + 6 queries due |
| 4 | 03 FastAPI / REST | API + contract tests due |
| 5 | 04 Docker / CI | one-command stack + manifest due |
| 6 | 05 LLM fundamentals + prompting | prompt registry + injection set due |
| 7 | 05b (optional) Build tiny transformer | only if time / appetite (`supplementary/`) |
| 7 | 06 Embeddings and vector search | benchmark + cross-tenant test due |
| 8 | **Midterm: system design** (open-book, take-home) | covers ch01-06 |
| 9 | 07 RAG basics | end-to-end RAG + no-answer due |
| 10 | 08 Advanced RAG | experiment harness + rerank decision due |
| 11 | 09 Evaluation | golden set + release gate due |
| 12 | 10 Agents | agent graph + approval gates due |
| 13 | 12 Production + 13 Optimization | observability + latency budget due |
| 14 | 14 Fine-tuning + 15 Security | adaptation memo + threat model + guardrails due |
| 15 | 16 Capstone integration + portfolio polish | demo runbook due |
| 16 | **Final: oral defense + demo** | 30 min per student |

Chapters 11 (Azure/Foundry) and 14 (fine-tuning) are typically assigned as
**reading + memo**, not full implementations, due to cloud-account and GPU
constraints.

## Grading scheme (suggested)

| Component | Weight |
| --- | --- |
| Participation + paper notes (one paper/week, see `syllabus/papers_to_read.md`) | 10% |
| Chapter homeworks (drop lowest 2) | 20% |
| Quizzes (15 total, drop lowest 3) | 10% |
| Midterm system design | 15% |
| Capstone (M1-M9 milestones graded incrementally) | 30% |
| Final oral defense + demo | 15% |

Adjust the capstone weight upward (to 40-45%) for graduate sections.

## Per-chapter notes for instructors

Each block is intentionally short — the pitfalls students hit, time estimate,
where to find the answer key. Expand as you teach.

### ch00 Orientation
- **Pitfall**: students pick a domain they cannot legally use (proprietary
  corpora). Push them toward open standards, project docs, or synthetic data.
- **Reviewer time**: 20 min per proposal.
- **Answer key**: there isn't one — the artifact is a planning document.
  Grade against the rubric in `chapters/00_orientation/examples.md`.

### ch01 Python backend
- **Pitfall**: 70% of students put provider calls in route handlers.
  Block this in week 2 review; otherwise it cascades.
- **Pitfall**: students forget `extra="forbid"` and chase silent ignored fields.
- **Answer-key proxy**: `chapters/01_python_backend_foundations/examples.md`
  contains a reference skeleton.

### ch02 SQL
- **Pitfall**: cascading deletes; not denormalising `tenant_id` onto chunks.
- **Most common late bug**: a forgotten `WHERE tenant_id = ?` in a custom query.

### ch03 FastAPI
- **Pitfall**: putting `tenant_id` in the request body. The grader's first
  test should be "can a tenant query another tenant via body?".
- **Time sink**: streaming SSE — budget extra office hours.

### ch04 Docker/CI
- **Pitfall**: container running as root; missing `extra="forbid"` equivalent
  for env config.
- **Setup**: ensure CI minutes are available; students will exceed free tiers.

### ch05 LLM fundamentals
- **Pitfall**: students conflate the model with the API. Use chapter 5b
  (supplementary) for the strong students.
- **Common confusion**: "temperature 0" isn't perfectly deterministic
  (batch effects, MoE routing) — covered in the lesson; expect questions.

### ch06 Embeddings
- **Pitfall**: post-filtering (filter after retrieval). This is the
  single most-graded mistake in this chapter.
- **Karpathy-style optional lab**: `chapters/06_embeddings_vector_search/my_work/`
  README includes a "compute and visualise embeddings yourself" extension.

### ch07 RAG
- **Pitfall**: citation presence vs correctness. Always test on at least
  10 cases where the supporting chunk is known.
- **Optional stretch**: the "no-framework RAG" assignment in the homework —
  raw HTTP, numpy cosine, no LangChain. Strongly recommended for ML majors.

### ch08 Advanced RAG
- **Pitfall**: adopting reranking because it raises NDCG, without checking
  faithfulness. Block this in week 10 review.

### ch09 Evaluation
- **Pitfall**: uncalibrated LLM-as-judge. Require the calibration study.

### ch10 Agents
- **Pitfall**: permission checks in the prompt. Test with an injection case
  that asks the agent to call an unauthorised tool.

### ch11 Azure/Foundry
- **Reading-only week** for most cohorts. Have students produce
  `platform_mapping.md` + `framework_compare.md` only.

### ch12 Production/MLOps
- **Pitfall**: monitoring uptime, not quality. Require a quality SLO.

### ch13 Optimization
- **Pitfall**: cache key without tenant. Cross-tenant cache test is mandatory.

### ch14 Fine-tuning
- **Reading + memo for most cohorts** unless GPU resources are available.
- The decision memo is the deliverable; actual training is optional.

### ch15 Security
- **Pitfall**: guardrails as prompts. Require code-enforced permission proof.

### ch16 Capstone integration
- **Pitfall**: leaving honest limitations off the README. Without ≥3 named
  limitations, the portfolio is incomplete.

## Common student mistakes (across chapters)

1. **Treating the model as the system.** Cure: walk them through the chapter-01
   layered architecture in week 2 office hours.
2. **Demo thinking.** Their first eval run is a ritual, not a measurement.
   Cure: require a *failure analysis* per chapter, not a success report.
3. **Skipping the no-answer path.** Cure: 30% of golden-set cases must be
   unanswerable; refusal accuracy is a release-gate metric.
4. **Citation presence ≠ correctness.** See ch07 note.
5. **`tenant_id` in request body.** See ch03 note.
6. **Optimising the wrong stage.** Cure: require a latency budget *before*
   any optimization.
7. **Adopting techniques without baselines.** Especially ch08. Cure: every
   advanced technique passes the chapter-09 release gate.

## Office-hour FAQ (chapter-agnostic)

- *"How long should the lesson take?"* 60-90 min for the lesson + deep_dive;
  another 2-4 hours for the project lab. Adjust per cohort.
- *"My corpus has PII."* It doesn't anymore (see ch15 PII policy). Don't use it.
- *"Can I use Claude / ChatGPT for the homework?"* See `ACADEMIC_INTEGRITY.md`.
- *"My eval judge keeps disagreeing with me."* That's the calibration problem
  (ch09 §6). Run the calibration study.

## Where the answer keys live

- **Quizzes**: `chapters/*/question_bank.md` has an explicit Answer Key
  section for MCQs, applied MCQs, and fill-in-the-blanks.
- **Project labs**: graded against the *Acceptance Criteria* sections, not a
  reference implementation. Multiple correct designs are expected.
- **Capstone**: graded against `capstone/deliverables_checklist.md` and the
  per-chapter capstone checklists at the end of each lesson.

## Customisation guidance

- **Shorter (10-12 week) version**: drop ch11, treat ch14 as reading, merge
  ch12 and ch13 into one production week.
- **Industry-track (compressed)**: skip ch00 planning details; do midterm
  as a paid project review.
- **Research-track (longer, 20 weeks)**: insert the `supplementary/05b`
  lab, expand the papers-to-read list with one paper per week, require
  each student to extend one chapter.

## What to update each year

| Item | Frequency |
| --- | --- |
| `syllabus/papers_to_read.md` post-2023 entries | annually |
| `resources/source_map.md` (links rot) | semester |
| Model ids in examples (e.g. `gpt-4o-mini-2024-07-18`) | semester |
| Vendor pricing references | semester |

## Feedback loop

Students who improve the repo earn extra credit (cap 5%) — they open PRs
fixing typos, breaking-source links, weak diagrams. This is real engineering
practice and produces useful repo improvements.
