# System Design Template

## Problem

Kullanici kim?

Hangi is problemini cozuyoruz?

## Constraints

- Latency:
- Accuracy:
- Data privacy:
- Compliance:
- Cost:
- Scale:

## Architecture

```text
Client
  -> API
  -> Auth
  -> RAG/Agent service
  -> Retrieval
  -> LLM
  -> Evaluation/logging
```

## Data Model

- documents
- chunks
- embeddings
- requests
- retrieved_contexts
- answers
- feedback
- eval_cases
- audit_logs

## Retrieval Strategy

- chunking:
- embedding model:
- vector DB:
- metadata filters:
- hybrid search:
- reranking:

## Agent Strategy

- tools:
- state:
- memory:
- approval:
- tracing:

## Evaluation Strategy

- golden dataset:
- metrics:
- human review:
- regression gate:

## Security

- tenant isolation:
- PII masking:
- RBAC:
- prompt injection:
- audit logs:

## Operations

- monitoring:
- logging:
- incident response:
- rollback:
- cost controls:

