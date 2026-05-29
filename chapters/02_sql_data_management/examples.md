# Examples: SQL and Data Management

Concrete snippets you can paste into your `my_work/` files and adapt. Each
example is intentionally short — the full discussion is in `lesson.md`.

## 1. Idempotent document ingestion

```sql
INSERT INTO documents (tenant_id, source_uri, title, document_type,
                       mime_type, sha256, byte_size, access_level, created_by)
VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
ON CONFLICT (tenant_id, sha256) WHERE deleted_at IS NULL
DO UPDATE SET title = EXCLUDED.title      -- harmless touch; returns id
RETURNING id;
```

The partial unique index on `(tenant_id, sha256)` makes re-uploading the
same file a no-op that returns the existing id.

## 2. Soft delete with audit in one transaction

```sql
BEGIN;

UPDATE documents
SET deleted_at = NOW(),
    deleted_by = $1,
    delete_reason = $2
WHERE id = $3
  AND tenant_id = $4
  AND deleted_at IS NULL;

INSERT INTO audit_log (actor_type, actor_id, tenant_id, action,
                       resource_type, resource_id, purpose, payload)
VALUES ('user', $1, $4, 'document.delete', 'document', $3, $2,
        jsonb_build_object('soft_delete', true));

COMMIT;
```

If the audit insert fails, the soft delete rolls back. Single transaction,
single source of truth.

## 3. Latency p95 by tenant for the last 24 hours

```sql
SELECT
    r.tenant_id,
    PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY a.latency_ms) AS p50_ms,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY a.latency_ms) AS p95_ms,
    COUNT(*) AS n
FROM answers a
JOIN requests r ON r.id = a.request_id
WHERE r.received_at >= NOW() - INTERVAL '24 hours'
GROUP BY r.tenant_id
HAVING COUNT(*) >= 10            -- avoid noise from low-traffic tenants
ORDER BY p95_ms DESC;
```

Add `WHERE r.endpoint = '/ask'` to scope to a specific endpoint.

## 4. Quality regression across releases

```sql
WITH ranked AS (
    SELECT
        er.dataset_id, er.model_id, er.prompt_version,
        er.completed_at,
        (er.summary->>'pass_rate')::numeric AS pass_rate,
        ROW_NUMBER() OVER (
            PARTITION BY er.dataset_id, er.model_id, er.prompt_version
            ORDER BY er.completed_at DESC
        ) AS rn
    FROM eval_runs er
    WHERE er.completed_at IS NOT NULL
)
SELECT dataset_id, model_id, prompt_version, completed_at, pass_rate
FROM ranked
WHERE rn <= 2
ORDER BY dataset_id, model_id, prompt_version, completed_at DESC;
```

Compare consecutive runs of the same `(dataset, model, prompt)` to detect
regressions before release.

## 5. Cross-tenant leak check (should return 0 rows)

```sql
SELECT a.request_id, r.tenant_id AS request_tenant, c.tenant_id AS chunk_tenant
FROM answers a
JOIN requests r ON r.id = a.request_id
JOIN UNNEST(a.cited_chunk_ids) AS cid ON TRUE
JOIN chunks c ON c.id = cid
WHERE r.tenant_id <> c.tenant_id
LIMIT 100;
```

Run this nightly as a guardrail. If it ever returns a row, you have a leak;
freeze releases and investigate.

## 6. JSONB metadata containment query

```sql
SELECT id, title
FROM documents
WHERE tenant_id = $1
  AND deleted_at IS NULL
  AND metadata @> '{"jurisdiction": "TR", "regulatory_class": "PII"}'::jsonb;
```

Requires a GIN index for speed at scale:

```sql
CREATE INDEX ix_documents_metadata_gin
    ON documents USING GIN (metadata jsonb_path_ops);
```

## 7. pgvector retrieval with metadata filter

```sql
SELECT c.id, c.text, e.vector <=> $1 AS distance
FROM embeddings e
JOIN chunks c ON c.id = e.chunk_id
WHERE c.tenant_id = $2
  AND e.index_version = $3
  AND c.metadata @> $4              -- e.g. {"jurisdiction": "TR"}
ORDER BY e.vector <=> $1
LIMIT $5;
```

`<=>` is cosine distance under `vector_cosine_ops`. With an HNSW index on
`embeddings.vector`, this is the canonical RAG retrieval query when using
pgvector.

## 8. Audit query: who touched a sensitive document last week?

```sql
SELECT occurred_at, actor_id, action, purpose, request_id, ip_address
FROM audit_log
WHERE resource_type = 'document'
  AND resource_id = $1
  AND occurred_at >= NOW() - INTERVAL '7 days'
ORDER BY occurred_at DESC;
```

Investigators ask this query; design for it from day one.

## 9. Deletion job: what's left to clean up?

```sql
SELECT d.id AS document_id, d.deleted_at,
       COUNT(c.id) AS remaining_chunks,
       COUNT(e.id) AS remaining_embeddings
FROM documents d
LEFT JOIN chunks c ON c.document_id = d.id
LEFT JOIN embeddings e ON e.chunk_id = c.id
WHERE d.deleted_at IS NOT NULL
  AND d.deleted_at < NOW() - INTERVAL '30 days'
GROUP BY d.id
HAVING COUNT(c.id) > 0 OR COUNT(e.id) > 0;
```

Documents that are soft-deleted but still have chunks/embeddings are
deletion-job backlog. Should always be a small, decreasing number.

## 10. Schema migration: add a column the safe way

```sql
-- Step 1: add nullable column (fast)
ALTER TABLE answers ADD COLUMN reranker_version TEXT;

-- Step 2: backfill in batches (no big transaction)
WITH batch AS (
    SELECT request_id FROM answers
    WHERE reranker_version IS NULL
    LIMIT 1000
)
UPDATE answers SET reranker_version = 'unknown'
WHERE request_id IN (SELECT request_id FROM batch);
-- repeat until 0 rows updated

-- Step 3: enforce NOT NULL (after backfill completes)
ALTER TABLE answers ALTER COLUMN reranker_version SET NOT NULL;
```

This pattern avoids the table rewrite that a `DEFAULT` value would trigger
on older Postgres.

## 11. Connection pool config (SQLAlchemy async)

```python
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine(
    settings.database_url,
    pool_size=10,
    max_overflow=10,
    pool_pre_ping=True,
    pool_recycle=1800,
    echo=False,
)
```

Tune `pool_size + max_overflow` to match worker concurrency. With PgBouncer
in transaction-pool mode, shrink the application pool to ~5 and let PgBouncer
multiplex.

## 12. Row-level security policy

```sql
ALTER TABLE chunks ENABLE ROW LEVEL SECURITY;

CREATE POLICY chunks_tenant_iso ON chunks
    USING (tenant_id = current_setting('app.tenant_id', true)::uuid);

-- In the application, per request:
-- SET LOCAL app.tenant_id = '...';
```

The `true` second argument to `current_setting` makes it return NULL instead
of error if the setting is missing, which is safer (the policy then matches
no rows rather than crashing).
