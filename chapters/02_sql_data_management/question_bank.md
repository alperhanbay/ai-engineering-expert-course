# Expanded Question Bank: SQL and Data Management

## How To Use This Bank

Answer without looking at the answer key. For every wrong answer, write one sentence explaining the concept in your own words and one sentence explaining how it appears in a production AI system.


## Multiple Choice

1. Pick the description of `documents` you would put in a `dictionary.md` entry.
   - A. A compliance-oriented record of who accessed or changed what, when, why, and through which system.
   - B. Source files or records ingested into an AI knowledge system.
   - C. Smaller text units created from documents for retrieval.
   - D. Structured fields describing data, such as source, tenant, date, type, permissions, and version.

2. Which sentence is the best working definition of `chunks`?
   - A. Smaller text units created from documents for retrieval.
   - B. Source files or records ingested into an AI knowledge system.
   - C. Structured fields describing data, such as source, tenant, date, type, permissions, and version.
   - D. A compliance-oriented record of who accessed or changed what, when, why, and through which system.

3. In production AI work, what is the primary role of `metadata`?
   - A. Source files or records ingested into an AI knowledge system.
   - B. Smaller text units created from documents for retrieval.
   - C. A compliance-oriented record of who accessed or changed what, when, why, and through which system.
   - D. Structured fields describing data, such as source, tenant, date, type, permissions, and version.

4. A teammate asks you to define `audit log` in one sentence. Which is closest?
   - A. Smaller text units created from documents for retrieval.
   - B. Structured fields describing data, such as source, tenant, date, type, permissions, and version.
   - C. A compliance-oriented record of who accessed or changed what, when, why, and through which system.
   - D. Source files or records ingested into an AI knowledge system.

5. Pick the description of `golden dataset` you would put in a `dictionary.md` entry.
   - A. Structured fields describing data, such as source, tenant, date, type, permissions, and version.
   - B. A curated set of test cases with expected behavior and reference evidence.
   - C. Source files or records ingested into an AI knowledge system.
   - D. Smaller text units created from documents for retrieval.

6. Which sentence is the best working definition of `feedback table`?
   - A. A database table that stores user or expert judgments about system outputs.
   - B. Source files or records ingested into an AI knowledge system.
   - C. Smaller text units created from documents for retrieval.
   - D. Structured fields describing data, such as source, tenant, date, type, permissions, and version.

7. In production AI work, what is the primary role of `index`?
   - A. Source files or records ingested into an AI knowledge system.
   - B. Smaller text units created from documents for retrieval.
   - C. Structured fields describing data, such as source, tenant, date, type, permissions, and version.
   - D. A data structure that accelerates lookup, either in SQL or vector search.

8. A teammate asks you to define `retention policy` in one sentence. Which is closest?
   - A. Smaller text units created from documents for retrieval.
   - B. Structured fields describing data, such as source, tenant, date, type, permissions, and version.
   - C. Rules for how long data is stored and when it is deleted or anonymized.
   - D. Source files or records ingested into an AI knowledge system.


## Applied Multiple Choice

1. Applied case: Vector stores retrieve candidates, but SQL explains who accessed what and why.
   - A. Skip the rollback plan; staging is close enough to production.
   - B. Hard-code the new behaviour for the first failing case and call it a fix.
   - C. Ship the change without measurement because the most recent demo looked good.
   - D. Set up a controlled experiment isolating `documents`, capture before/after numbers, and write the result to a decision record.

2. Applied case: Evaluation data becomes useless if it is not versioned and queryable.
   - A. Ship the change without measurement because the most recent demo looked good.
   - B. Remove logging and evaluation to keep the diff small and merge faster.
   - C. Add the work to the capstone as a reviewable artifact that exercises `chunks` end-to-end, with tests and a trace.
   - D. Hard-code the new behaviour for the first failing case and call it a fix.

3. Applied case: Regulated systems need auditability across raw documents, chunks, embeddings, prompts, and outputs.
   - A. Assume the largest available model will mask the underlying weakness in `documents` so no system change is needed.
   - B. Define explicit acceptance criteria, rollback steps, and a reviewer checklist tied to SQL and Data Management.
   - C. Ship the change without measurement because the most recent demo looked good.
   - D. Remove logging and evaluation to keep the diff small and merge faster.

4. Applied case: Design a complete AI metadata schema with documents, chunks, requests, answers, feedback, evals, and audit logs.
   - A. Compare at least two approaches against a labelled set covering `retention policy`, then choose on measured quality, latency, cost, and risk.
   - B. Remove logging and evaluation to keep the diff small and merge faster.
   - C. Assume the largest available model will mask the underlying weakness in `documents` so no system change is needed.
   - D. Skip the rollback plan; staging is close enough to production.

5. Applied case: Write incident-analysis SQL queries for latency, quality regression, and unsafe access.
   - A. Assume the largest available model will mask the underlying weakness in `documents` so no system change is needed.
   - B. Skip the rollback plan; staging is close enough to production.
   - C. Hard-code the new behaviour for the first failing case and call it a fix.
   - D. Write a one-page design memo naming the assumption, the test that would falsify it, and the metric you'd watch in production.

6. Applied case: Build a versioned golden dataset registry with reviewer and risk metadata.
   - A. Hard-code the new behaviour for the first failing case and call it a fix.
   - B. Ship the change without measurement because the most recent demo looked good.
   - C. Set up a controlled experiment isolating `documents`, capture before/after numbers, and write the result to a decision record.
   - D. Skip the rollback plan; staging is close enough to production.


## Fill In The Blanks

1. ________ is best summarised as: Source files or records ingested into an AI knowledge system. Verification step: Track document ID, source, version, owner, tenant, and access metadata.
2. On a system review, you find a chunk cuts a legal clause in half and retrieval loses the condition — the underlying chapter concept is ________.
3. Metadata powers filtering, access control, evaluation grouping, and citations. A common failure looks like: Vector search retrieves semantically relevant but unauthorized content. The concept is ________.
4. Given the production failure "The system cannot prove which user retrieved a sensitive document.", the concept being misused is ________.
5. To handle situations where it provides regression protection for prompts, models, indexes, and retrievers, the engineering tool you reach for is ________ (watch for: A new prompt feels better but silently breaks old high-risk cases.).
6. ________ is best summarised as: A database table that stores user or expert judgments about system outputs. Verification step: Store rating, reason, failure category, reviewer, model/prompt/index version.
7. On a system review, you find a filter-heavy query scans too much data and misses latency targets — the underlying chapter concept is ________.
8. AI systems duplicate data across raw files, chunks, embeddings, logs, and evals. A common failure looks like: A deleted document remains embedded and retrievable from an old index. The concept is ________.

## Short Answer

1. When would you intentionally *avoid* using `documents`? Name a constraint or tradeoff.
2. What does a healthy log or trace look like for `chunks`? List the fields you would expect.
3. Explain how `metadata` appears in the capstone, what artifact proves it, and what failure mode you would test.
4. If a reviewer asks 'why does `audit log` matter here?', what one-paragraph answer do you give? Include a metric.
5. Describe the smallest experiment that would tell you whether `golden dataset` is correctly implemented in your system.
6. When would you intentionally *avoid* using `feedback table`? Name a constraint or tradeoff.
7. What does a healthy log or trace look like for `index`? List the fields you would expect.
8. Explain how `retention policy` appears in the capstone, what artifact proves it, and what failure mode you would test.

## Scenario Questions

1. On-call triage: Vector stores retrieve candidates, but SQL explains who accessed what and why. Walk through the first three steps you would take.
2. Incident: Evaluation data becomes useless if it is not versioned and queryable. What do you inspect first, and which metric would prove the fix?
3. Design review: Regulated systems need auditability across raw documents, chunks, embeddings, prompts, and outputs. Which artifact would you require before approving?
4. A teammate proposes a major change to `metadata` with no experiment. Which artifact do you ask for before approving?

## Practical Debug Questions

1. What log or trace fields would help you debug a failure in `documents` in this chapter's context?
2. What single metric would you watch in production when changing `golden dataset`?
3. You suspect `retention policy` is degraded. Design the smallest experiment that would falsify or confirm it in under an hour.
4. For the failure 'Vector stores retrieve candidates, but SQL explains who accessed what and why.', sketch a rollback plan with a clear restore-point definition.
5. What artifact would you put in a portfolio README to prove competence with `documents`, `chunks`, `metadata`?

## Answer Key

### Multiple Choice

1. B
2. A
3. D
4. C
5. B
6. A
7. D
8. C

### Applied Multiple Choice

1. D
2. C
3. B
4. A
5. D
6. C

### Fill In The Blanks

1. documents
2. chunks
3. metadata
4. audit log
5. golden dataset
6. feedback table
7. index
8. retention policy

Short-answer, scenario, and debug questions should be graded against the rubric in `../../syllabus/evaluation_rubric.md`.

## References

[1] PostgreSQL documentation: https://www.postgresql.org/docs/
[2] PostgreSQL indexes: https://www.postgresql.org/docs/current/indexes.html
[3] PostgreSQL JSON types: https://www.postgresql.org/docs/current/datatype-json.html
[4] pgvector GitHub: https://github.com/pgvector/pgvector
[5] MLflow tracking: https://www.mlflow.org/docs/latest/ml/tracking
