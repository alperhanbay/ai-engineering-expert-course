# Homework: SQL and Data Management

These tasks are graded against `../../syllabus/evaluation_rubric.md`. Put your
work under `my_work/` and link to it from `my_work/summary.md`.

## Required

1. **Schema implementation.** Translate the seven canonical tables from
   `lesson.md` (documents, chunks, embeddings, requests, answers, feedback,
   audit_log) plus the eval tables into a runnable `my_work/schema.sql`.
   Apply it to a local Postgres (`docker compose up postgres`) and capture
   `\d+ <table>` output for each table in `my_work/schema_dump.md`.

2. **Index justification.** For every non-PK index in your schema, add a row
   in `my_work/schema_notes.md`:
   `| index name | table | columns | query it serves | size after seed |`.
   If you cannot name the query, the index does not belong in the schema.

3. **Six named queries.** Write the following queries against your schema as
   parameterised SQL in `my_work/queries/`:
   - `latency_p95.sql` — p95 `/ask` latency by tenant for the last 24h
   - `quality_regression.sql` — eval pass rate by `(model_id, prompt_version)`
     for the latest two runs of each dataset
   - `top_failure_category.sql` — top failure categories from feedback in the
     last 7 days, by tenant
   - `unauthorized_access.sql` — requests where the answer cited a chunk
     belonging to a different tenant (should always return 0 rows)
   - `daily_cost.sql` — token totals and estimated cost per tenant per day
   - `eval_coverage.sql` — % of risk levels covered by the latest eval
     dataset version

4. **Retention policy.** Write `my_work/retention_policy.md` with a row per
   table and per external store (object storage, vector store), naming the
   TTL, the deletion control, and the audit entry produced.

5. **Migration with rollback.** Add a column to the `answers` table
   (e.g. `reranker_version TEXT`). Use Alembic (or your migration tool of
   choice) to write a forward + rollback pair, apply forward, verify, roll
   back, verify. Commit the migration files and a `my_work/migration_log.md`
   showing the sequence.

## Stretch

6. **Row-level security.** Enable RLS on `documents` and `chunks`, add a
   policy that filters by a session-local `tenant_id`, and write a test that
   proves a query without the setting raises (or returns zero rows) for
   cross-tenant data.

7. **`pg_stat_statements` snapshot.** After running each named query 100
   times against a seeded dataset, capture the top 10 by `total_exec_time`
   in `my_work/stats_snapshot.md`. Identify the one most worth tuning.

## Acceptance

- Schema applies clean on a fresh database.
- Every named query returns the documented shape on the seed data.
- The retention policy doc has no "TBD" entries.
- The migration rolls back without losing data.
