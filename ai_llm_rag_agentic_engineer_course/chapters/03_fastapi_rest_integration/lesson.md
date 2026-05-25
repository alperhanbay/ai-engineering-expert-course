# Lesson: FastAPI, REST, and Integration

## 1. Why APIs Matter in AI Engineering

An AI system becomes useful when other systems can call it reliably. The LLM pipeline should be exposed through stable contracts, not through notebook cells.

APIs connect your AI system to:

- web applications;
- internal tools;
- chat interfaces;
- CRM systems;
- document management systems;
- business workflow tools;
- evaluation runners;
- monitoring systems.

## 2. REST Concepts

REST is an architectural style based on resources and standard HTTP semantics.

Common HTTP methods:

| Method | Meaning |
| --- | --- |
| GET | read a resource |
| POST | create or run an operation |
| PUT | replace a resource |
| PATCH | partially update a resource |
| DELETE | delete a resource |

In AI systems, many operations are action-like:

- `POST /ask`
- `POST /documents/{id}/index`
- `POST /agent/run`
- `POST /eval/run`

These are acceptable when the operation does not map cleanly to CRUD.

## 3. FastAPI Core Concepts

FastAPI gives:

- path operations;
- request parsing;
- Pydantic validation;
- dependency injection;
- OpenAPI schema generation;
- async support;
- testing with HTTP clients.

Example:

```python
@router.post("/ask", response_model=AskResponse)
async def ask(request: AskRequest) -> AskResponse:
    return await rag_service.answer(request)
```

## 4. API Contract Design

A good AI API contract should include:

- explicit request schema;
- explicit response schema;
- citations;
- model/prompt/index metadata;
- error format;
- request ID;
- latency or trace reference.

Example response fields:

```json
{
  "answer": "...",
  "citations": [],
  "requires_human_review": false,
  "model_version": "model_x",
  "prompt_version": "rag_v4",
  "index_version": "idx_2026_05",
  "request_id": "req_123"
}
```

## 5. Error Handling

AI APIs should not hide all errors as `500`.

Examples:

| Case | Status |
| --- | --- |
| invalid request schema | 422 |
| unauthenticated | 401 |
| unauthorized document access | 403 |
| no relevant context | 422 or safe no-answer response |
| provider timeout | 503 |
| unsafe output blocked | 422 or policy-specific error |

## 6. Streaming

LLM answers can be slow. Streaming returns tokens or chunks as they are generated.

Streaming improves perceived latency, but it does not automatically reduce total compute. It also complicates:

- error handling after partial output;
- citation placement;
- output validation;
- guardrails.

Use streaming when user experience needs fast first output, but design validation carefully.

## 7. Background Jobs

Indexing documents can take seconds or minutes. It should often be asynchronous:

```text
POST /documents
  -> store document
  -> create ingestion job
  -> return job_id

GET /jobs/{job_id}
  -> return status
```

This avoids HTTP timeouts and gives users a way to track progress.

## 8. Integration Boundaries

External systems should not know your internal model provider or vector DB. Keep product API stable:

```text
Client -> AI API contract -> internal RAG/agent implementation
```

This lets you change:

- model;
- prompt;
- retriever;
- reranker;
- vector database;
- evaluation method.

## 9. Security Basics

Minimum API security:

- authentication;
- authorization;
- request size limits;
- rate limits;
- input validation;
- tenant-aware retrieval;
- audit logging;
- safe error messages.

## 10. Key Takeaway

FastAPI is not just a way to expose a model call. It is the boundary between your AI system and the rest of the product. A strong API contract protects users, product teams, and future versions of the system.
## Numbered References

[1] FastAPI first steps: https://fastapi.tiangolo.com/tutorial/first-steps/
[2] FastAPI request body: https://fastapi.tiangolo.com/tutorial/body/
[3] FastAPI error handling: https://fastapi.tiangolo.com/tutorial/handling-errors/
[4] FastAPI testing: https://fastapi.tiangolo.com/tutorial/testing/
[5] OpenAPI Specification: https://spec.openapis.org/oas/latest.html
