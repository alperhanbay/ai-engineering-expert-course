# Dictionary: SQL and Data Management

Use this dictionary at the end of the chapter. Add your own examples in `my_work/dictionary_notes.md`.

| Term | Working Definition | Why It Matters | Common Failure Mode | Mastery Check |
| --- | --- | --- | --- | --- |
| `documents` | Source files or records ingested into an AI knowledge system. | Documents are the root of traceability for chunks, embeddings, citations, and permissions. | The answer cites a chunk but cannot identify its source document. | Track document ID, source, version, owner, tenant, and access metadata. |
| `chunks` | Smaller text units created from documents for retrieval. | Chunk quality directly affects retrieval, citations, and generation quality. | A chunk cuts a legal clause in half and retrieval loses the condition. | Inspect sample chunks and measure retrieval outcomes by chunking strategy. |
| `metadata` | Structured fields describing data, such as source, tenant, date, type, permissions, and version. | Metadata powers filtering, access control, evaluation grouping, and citations. | Vector search retrieves semantically relevant but unauthorized content. | Define required metadata fields and validate them before indexing. |
| `audit log` | A compliance-oriented record of who accessed or changed what, when, why, and through which system. | Audit logs support investigations and regulated-domain accountability. | The system cannot prove which user retrieved a sensitive document. | Record user, tenant, action, data IDs, purpose, model/prompt/index version, and timestamp. |
| `golden dataset` | A curated set of test cases with expected behavior and reference evidence. | It provides regression protection for prompts, models, indexes, and retrievers. | A new prompt feels better but silently breaks old high-risk cases. | Build versioned cases with question, expected answer, reference chunks, and risk level. |
| `feedback table` | A database table that stores user or expert judgments about system outputs. | Feedback becomes training signal, eval data, and product quality evidence. | Users downvote answers but the data is never categorized or reused. | Store rating, reason, failure category, reviewer, model/prompt/index version. |
| `index` | A data structure that accelerates lookup, either in SQL or vector search. | Indexes affect latency, recall, storage, and filtering behavior. | A filter-heavy query scans too much data and misses latency targets. | Explain which indexes support your common query paths and why. |
| `retention policy` | Rules for how long data is stored and when it is deleted or anonymized. | AI systems duplicate data across raw files, chunks, embeddings, logs, and evals. | A deleted document remains embedded and retrievable from an old index. | Document deletion behavior for raw docs, chunks, embeddings, logs, and traces. |

<!-- HAND-AUTHORED: do not regenerate -->
## Extended Glossary

Additional terms used in this chapter, each with a concise definition and an authoritative source.

- **Primary key / Foreign key** — a row's unique identifier / a reference enforcing referential integrity. Source: [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)
- **Composite index** — an index over multiple columns, serving multi-column query/filter patterns. Source: [PostgreSQL multicolumn indexes](https://www.postgresql.org/docs/current/indexes-multicolumn.html)
- **GIN index** — an inverted index for JSONB/arrays/full-text. Source: [PostgreSQL GIN](https://www.postgresql.org/docs/current/gin.html)
- **JSONB** — PostgreSQL's binary JSON type, indexable and queryable. Source: [JSON types](https://www.postgresql.org/docs/current/datatype-json.html)
- **HNSW (pgvector)** — graph-based approximate nearest-neighbour index for vectors. Source: [pgvector](https://github.com/pgvector/pgvector)
- **Transaction / ACID** — an all-or-nothing unit of work with atomicity, consistency, isolation, durability. Source: [PostgreSQL transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)
- **Row-Level Security (RLS)** — per-row access policies enforced by the database. Source: [PostgreSQL RLS](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)
- **Soft delete** — marking a row deleted (timestamp) instead of removing it, for audit. Source: [Designing Data-Intensive Applications](https://dataintensive.net/)
- **Idempotency key** — a client-supplied key making a repeated write safe (no duplicates). Source: [Stripe idempotency](https://docs.stripe.com/api/idempotent_requests)
- **Partitioning** — splitting a large table (e.g. by month) for manageability/performance. Source: [PostgreSQL partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html)
- **Connection pooling / PgBouncer** — reusing DB connections to handle concurrency. Source: [PgBouncer](https://www.pgbouncer.org/)
- **pg_stat_statements** — extension tracking query execution statistics. Source: [pg_stat_statements](https://www.postgresql.org/docs/current/pgstatstatements.html)
- **Denormalization** — duplicating a column (e.g. tenant_id on chunks) to avoid costly/forgotten joins. Source: [DDIA](https://dataintensive.net/)

## Dictionary Assignment

For each term:

1. Write a one-sentence definition in your own words.
2. Write a concrete example from your capstone (or planned capstone).
3. Write one failure mode you would test against.
4. Write one metric, test, or review check that would catch the failure.
5. Link one source from `references_numbered.md`.

## References

[1] PostgreSQL documentation: https://www.postgresql.org/docs/
[2] PostgreSQL indexes: https://www.postgresql.org/docs/current/indexes.html
[3] PostgreSQL JSON types: https://www.postgresql.org/docs/current/datatype-json.html
[4] pgvector GitHub: https://github.com/pgvector/pgvector
[5] MLflow tracking: https://www.mlflow.org/docs/latest/ml/tracking
