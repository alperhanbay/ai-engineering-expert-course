# Lesson: SQL and Data Management for AI Systems

## 1. Why SQL Still Matters in LLM Systems

Vector databases are important, but they do not replace relational data management. Production AI systems need SQL for:

- documents and metadata;
- users and tenants;
- permissions;
- evaluation datasets;
- feedback;
- request logs;
- audit logs;
- prompt/model/index versions;
- incident analysis.

Vector search answers "which chunks are semantically similar?" SQL answers "who can access them, what version produced this answer, and what happened over time?"

## 2. Core Data Entities

### Documents

Represent uploaded or ingested source material.

Fields:

- `id`;
- `tenant_id`;
- `source_uri`;
- `document_type`;
- `domain`;
- `created_at`;
- `version`;
- `access_level`.

### Chunks

Represent retrievable text units.

Fields:

- `id`;
- `document_id`;
- `chunk_index`;
- `text`;
- `token_count`;
- `section`;
- `page_number`;
- `metadata`.

### Embedding Records

You may store vectors in a vector DB, but SQL can track embedding metadata:

- `chunk_id`;
- `embedding_model`;
- `embedding_dimension`;
- `vector_store`;
- `vector_id`;
- `index_version`;
- `created_at`.

### Requests and Answers

You need request-level traceability:

- question;
- user;
- tenant;
- model version;
- prompt version;
- index version;
- latency;
- retrieved chunks;
- generated answer;
- citations.

### Feedback and Evaluation

Feedback and eval cases make quality measurable:

- user rating;
- expert rating;
- failure category;
- expected answer;
- reference contexts;
- pass/fail;
- evaluator output.

## 3. Metadata Design

Good metadata enables:

- filtering;
- access control;
- relevance improvement;
- audits;
- evaluation grouping.

Examples:

```json
{
  "domain": "insurance",
  "document_type": "policy",
  "section": "claim_deadline",
  "jurisdiction": "TR",
  "effective_date": "2026-01-01"
}
```

## 4. Access Control and Tenant Isolation

Do not retrieve all vectors and filter unauthorized records afterward. Protected data should be filtered before or during retrieval.

Minimum access model:

```text
authenticated user
  -> tenant_id
  -> allowed document groups
  -> allowed classification levels
  -> retrieval filter
```

SQL should store the policy-relevant metadata. The vector search layer should enforce filters where possible.

## 5. Evaluation Data Model

A golden dataset should be versioned. Each case should include:

- `case_id`;
- `question`;
- `expected_answer`;
- `reference_context_ids`;
- `domain`;
- `difficulty`;
- `risk_level`;
- `created_by`;
- `created_at`;
- `dataset_version`.

This allows regression testing:

```text
prompt_v3 + index_2026_05 -> eval score
prompt_v4 + index_2026_05 -> eval score
prompt_v4 + index_2026_06 -> eval score
```

## 6. SQL Performance Concepts

You need to understand:

- primary keys;
- foreign keys;
- indexes;
- composite indexes;
- JSONB indexes;
- transactions;
- query plans;
- connection pooling.

For RAG systems, common query patterns include:

- recent requests by tenant;
- feedback by model version;
- failed eval cases by prompt version;
- slow requests;
- chunks for a document;
- audit events for a user;
- documents visible to a user.

## 7. Audit Logs vs Application Logs

Application logs help engineers debug. Audit logs provide compliance evidence.

Application log:

```text
retrieval completed in 120ms
```

Audit log:

```text
user u_42 accessed chunk c_99 from document d_10 for purpose rag_answer
```

Audit logs should be harder to mutate and should have retention rules.

## 8. Data Retention and Deletion

AI systems often duplicate data:

- raw document;
- parsed text;
- chunks;
- embeddings;
- logs;
- traces;
- evaluation examples.

Deletion policy must consider every copy. If a user or tenant data deletion request comes in, embeddings and logs may also be in scope depending on policy and regulation.

## 9. Key Takeaway

SQL is the control plane of a production AI system. Vector search retrieves semantic candidates, but SQL manages identity, permissions, metadata, logs, feedback, evaluation, and auditability.
## Numbered References

[1] PostgreSQL documentation: https://www.postgresql.org/docs/
[2] PostgreSQL indexes: https://www.postgresql.org/docs/current/indexes.html
[3] PostgreSQL JSON types: https://www.postgresql.org/docs/current/datatype-json.html
[4] pgvector GitHub: https://github.com/pgvector/pgvector
[5] MLflow tracking: https://www.mlflow.org/docs/latest/ml/tracking
