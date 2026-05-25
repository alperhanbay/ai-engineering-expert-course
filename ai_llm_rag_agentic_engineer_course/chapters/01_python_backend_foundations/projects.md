# Projects: Python Backend Foundations

## Project 1: AI Service Skeleton

Build a Python package with this structure:

```text
app/
  api/
  core/
  models/
  services/
  repositories/
  providers/
tests/
```

Deliverables:

- `AskRequest`, `AskResponse`, `Citation`, `RetrievedChunk` models;
- `RagService`;
- fake retriever;
- fake generator;
- unit tests;
- structured logs.

Acceptance criteria:

- at least 8 tests pass;
- type hints are present;
- no API code inside service tests;
- no provider-specific code inside the service contract.

## Project 2: Error Taxonomy

Create `my_work/error_taxonomy.md`.

Include:

- validation errors;
- authentication errors;
- authorization errors;
- no-context errors;
- LLM provider errors;
- vector DB errors;
- unsafe output errors;
- tool execution errors.

For each one, define:

- API status code;
- log level;
- retry policy;
- user-facing response.

## Project 3: Logging Contract

Design a JSON logging schema for:

- document ingestion;
- retrieval;
- generation;
- agent tool call;
- feedback submission;
- evaluation run.

