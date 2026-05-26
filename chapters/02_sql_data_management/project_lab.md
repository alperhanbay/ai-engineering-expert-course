# Project Lab: SQL and Data Management

SQL is the control plane for documents, metadata, permissions, logs, feedback, evaluation, and auditability. This lab turns the chapter's projects into concrete, reviewable
deliverables. Pick one project and finish it end-to-end before starting another.
The "Acceptance Criteria" sections are the gate — not the existence of files.

## Project 1: Design a complete AI metadata schema with documents, chunks, requests, answers, feedback, evals, and audit logs.

### Scenario

Design the SQL backbone that will track every document, chunk, request, answer, feedback, evaluation, and audit event. Without this, the capstone can retrieve and answer but can't explain itself to a reviewer or auditor.

### Inputs

- PostgreSQL (or compatible) running locally via docker-compose
- the document IDs from chapter 01's tiny corpus
- a sample list of users with tenant_id and role

### Outputs / Artifacts

- `schema.sql` with tables: `documents`, `chunks`, `requests`, `answers`, `feedback`, `evals`, `audit_log`
- indexes justified in `schema_notes.md` (which query each index serves)
- `queries/` with 6 named queries: latency p95, quality regression, top failure category, unauthorized access, daily cost, eval coverage
- a retention policy doc naming TTL per table and what is anonymized vs purged

### Test Cases

- insert a document and 5 chunks; foreign keys prevent orphans
- soft-delete a document; the audit_log shows who, when, why
- query top failure category over the last 7 days — runs in under 200ms on a seeded dataset
- unauthorized-access query identifies a request that touched another tenant's chunk
- retention dry-run reports rows that would be purged without deleting them

### Metrics

- query p95 latency on each of the 6 named queries (target under 200ms on seed data)
- % of audit-required actions that produce a row in `audit_log`
- schema migration tested with at least one forward + one rollback

### Failure Cases To Cover

- Vector store keeps embeddings for documents long after the row is deleted
- Audit log is best-effort and a write failure silently swallows the event
- Indexes optimize one query and slow down ingestion writes by 5x
- Retention deletes a document but leaves answers that cite it dangling

### Acceptance Criteria

- each table has a documented purpose and at least one query that exercises it
- the retention policy answers: raw doc, chunk, embedding, request, log — each gets a named control
- the rollback migration is tested, not just written

### Deliverables Layout

```
my_work/
  project_1_scope.md            # one paragraph + concept list
  project_1_implementation/      # code or design doc
  project_1_report.md            # results, numbers, plots
  project_1_decision_record.md   # alternatives + chosen approach + why
  project_1_tests/               # the test cases above, runnable or scripted
```

### Expected README Section

In your portfolio README, this project should appear under "Projects" with:
a one-sentence summary, the headline metric you measured, the main tradeoff
you made, and a link to the decision record. Avoid screenshots-only entries.

## Project 2: Write incident-analysis SQL queries for latency, quality regression, and unsafe access.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `documents`, `chunks`, `metadata`, `audit log`, `golden dataset`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `documents`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_2_implementation/`
- `my_work/project_2_report.md` summarising results with numbers
- `my_work/project_2_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `documents`
- an edge case driven by the failure mode of `chunks`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `documents` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Vector stores retrieve candidates, but SQL explains who accessed what and why.
- Evaluation data becomes useless if it is not versioned and queryable.
- Regulated systems need auditability across raw documents, chunks, embeddings, prompts, and outputs.
- silent degradation of `retention policy` after a config change goes unnoticed

### Acceptance Criteria

- a reviewer can run or read the artifact and understand what was built without asking you
- every numeric claim is backed by a test, eval result, or measured run logged in the report
- at least one known limitation is named honestly (not a humblebrag)
- the artifact is wired into the capstone, not orphaned in `my_work/`

### Deliverables Layout

```
my_work/
  project_2_scope.md            # one paragraph + concept list
  project_2_implementation/      # code or design doc
  project_2_report.md            # results, numbers, plots
  project_2_decision_record.md   # alternatives + chosen approach + why
  project_2_tests/               # the test cases above, runnable or scripted
```

### Expected README Section

In your portfolio README, this project should appear under "Projects" with:
a one-sentence summary, the headline metric you measured, the main tradeoff
you made, and a link to the decision record. Avoid screenshots-only entries.

## Project 3: Build a versioned golden dataset registry with reviewer and risk metadata.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `documents`, `chunks`, `metadata`, `audit log`, `golden dataset`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `documents`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_3_implementation/`
- `my_work/project_3_report.md` summarising results with numbers
- `my_work/project_3_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `documents`
- an edge case driven by the failure mode of `chunks`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `documents` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Vector stores retrieve candidates, but SQL explains who accessed what and why.
- Evaluation data becomes useless if it is not versioned and queryable.
- Regulated systems need auditability across raw documents, chunks, embeddings, prompts, and outputs.
- silent degradation of `retention policy` after a config change goes unnoticed

### Acceptance Criteria

- a reviewer can run or read the artifact and understand what was built without asking you
- every numeric claim is backed by a test, eval result, or measured run logged in the report
- at least one known limitation is named honestly (not a humblebrag)
- the artifact is wired into the capstone, not orphaned in `my_work/`

### Deliverables Layout

```
my_work/
  project_3_scope.md            # one paragraph + concept list
  project_3_implementation/      # code or design doc
  project_3_report.md            # results, numbers, plots
  project_3_decision_record.md   # alternatives + chosen approach + why
  project_3_tests/               # the test cases above, runnable or scripted
```

### Expected README Section

In your portfolio README, this project should appear under "Projects" with:
a one-sentence summary, the headline metric you measured, the main tradeoff
you made, and a link to the decision record. Avoid screenshots-only entries.

## Review Rubric

| Dimension | Evidence that passes |
| --- | --- |
| Specificity | scenario, inputs, and outputs match what the artifact actually does |
| Measurement | metrics are numeric, named, and reproducible from the repo |
| Failure handling | at least three failure cases are exercised in tests |
| Tradeoff honesty | decision record names alternatives and a measured reason |
| Source backing | numbered references support every external claim |

## References

[1] PostgreSQL documentation: https://www.postgresql.org/docs/
[2] PostgreSQL indexes: https://www.postgresql.org/docs/current/indexes.html
[3] PostgreSQL JSON types: https://www.postgresql.org/docs/current/datatype-json.html
[4] pgvector GitHub: https://github.com/pgvector/pgvector
[5] MLflow tracking: https://www.mlflow.org/docs/latest/ml/tracking
