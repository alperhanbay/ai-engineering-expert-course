# Grading Scheme

A defensible grading scheme for a 14-16 week semester (undergraduate senior or
graduate elective). Adjust weights for your institution; the structure is what
matters.

## Weights

| # | Component | Weight | Why |
| --- | --- | --- | --- |
| 1 | Participation + paper notes (one paper/week from `syllabus/papers_to_read.md`) | 10% | first-principles literacy + engagement |
| 2 | Chapter homeworks (drop lowest 2) | 20% | scaffolded weekly practice |
| 3 | Quizzes (drop lowest 3) | 10% | low-stakes recall checks |
| 4 | Midterm system design (take-home, after ch08) | 15% | analyze/evaluate-level assessment |
| 5 | Capstone (M1-M9, graded incrementally) | 30% | the integrative artifact |
| 6 | Final oral defense + demo | 15% | senior-signal verification |

**Total: 100%**

For graduate sections, push capstone to 40% and reduce homeworks to 15%.

## Component details

### 1. Participation + paper notes (10%)

- One paper per week from `syllabus/papers_to_read.md`.
- Deliverable per paper: `my_work/papers/<short_name>.md` containing:
  1. one-sentence claim;
  2. main contribution;
  3. the headline experimental result + caveat;
  4. one limitation the authors named;
  5. **your** one critical question.
- Grading: pass/fail per week; cap-and-floor scoring.
- See `ACADEMIC_INTEGRITY.md` — AI-summarised notes do not count.

### 2. Chapter homeworks (20%)

- Each chapter's `homework.md` lists Required + Stretch tasks with explicit
  acceptance criteria.
- Graded against acceptance criteria, not against a reference implementation.
- Drop the lowest 2 scores to allow for one bad week.
- Each homework: 0-100 scale.

### 3. Quizzes (10%)

- One quiz per chapter (15 total in a 14-week semester) — `quiz.md` + selected
  items from `question_bank.md`.
- Drop the lowest 3.
- Cover remember/understand/apply Bloom levels.

### 4. Midterm system design (15%)

- After chapter 08. Take-home, 72 hours.
- Prompt: design a RAG+evaluation system for a domain the student has *not*
  built. Must include: data model, retrieval strategy, eval plan, failure
  modes, rollback story.
- Length: 6-10 pages plus 1-2 diagrams.
- Grading rubric (each scored 1-5):

| Dimension | Description |
| --- | --- |
| Requirements clarity | Who are the users, what is the accuracy bar, what counts as success |
| Data + retrieval design | Concrete schema, retrieval strategy with measurement plan |
| Evaluation plan | Golden set construction, metrics per risk level, release gate |
| Failure modes | At least 5 named with mitigations |
| Operations + security | Tenant isolation, audit, rollback, monitoring |
| Tradeoffs named | Decision criteria + alternatives considered |

### 5. Capstone (30%)

Graded incrementally on milestones from `capstone/deliverables_checklist.md`:

| Milestone | Weight inside capstone | Due (14-wk) |
| --- | --- | --- |
| M1 API skeleton + SQL schema | 5% | week 4 |
| M2 Document ingestion + chunking | 10% | week 9 |
| M3 Embeddings + vector DB | 10% | week 7 |
| M4 Basic RAG with citations | 15% | week 9 |
| M5 Hybrid + reranking + eval | 15% | week 10-11 |
| M6 Evaluation suite + release gate | 15% | week 11 |
| M7 Agent workflow with tools | 10% | week 12 |
| M8 Observability + security | 10% | week 13-14 |
| M9 Demo script + portfolio README | 10% | week 15 |

Late milestones lose 10%/day.

### 6. Final oral defense + demo (15%)

- 30 minutes per student.
- 10 min live demo from a clean clone.
- 10 min system-design walkthrough.
- 10 min Q&A on tradeoffs, failures, what they would change.

Grading rubric (each 1-5):

| Dimension | Description |
| --- | --- |
| Demo works | Ingest, supported answer, unsupported→refusal, eval, blocked injection |
| Code understanding | Can explain any line on request |
| Tradeoffs articulated | Names alternatives + measured/expert reasoning |
| Limitations honest | Names ≥3 gaps with planned fixes |
| Answers under pressure | Updates beliefs in response to counter-questions |

## Letter-grade mapping (US-style)

| Percentage | Letter |
| ---: | --- |
| ≥ 90 | A |
| 80-89 | B |
| 70-79 | C |
| 60-69 | D |
| < 60 | F |

For pass/fail variants, the threshold is 70%.

## Late, makeup, regrade policies

- **Late**: 10% per day, max 5 days, then 0.
- **Makeup**: only with documented circumstances (medical, family). Negotiate
  a new due date — not a waiver.
- **Regrade**: open a request within 1 week of receiving the grade,
  identifying which rubric line you contest, with evidence.

## Academic integrity

See `ACADEMIC_INTEGRITY.md`. Material from that document is enforced through
this grading scheme — missing AI-tool acknowledgement is a 10% per-assignment
penalty.

## Customisation

- **Compressed (10-12 week)**: drop ch11/14 to reading + memo only; reduce
  capstone milestones to M1-M6.
- **Industry-track**: replace midterm with a paid design review; raise final
  weight to 20%.
- **Research-track (20 week)**: insert `supplementary/05b` lab; require one
  course-extending PR per student.
