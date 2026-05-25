# Lesson: Python Backend Foundations for AI Systems

## 1. Why Python Backend Foundations Matter

Most LLM, RAG, and agent frameworks have strong Python ecosystems. However, production AI engineering is not notebook engineering. You need code that can be imported, tested, deployed, logged, and maintained.

Your goal is to move from:

```text
notebook cell -> demo output
```

to:

```text
typed package -> tested service -> API -> logs -> deployment
```

## 2. Project Structure

A clean Python AI service separates responsibilities:

```text
app/
  api/
    routes.py
  core/
    config.py
    logging.py
    errors.py
  models/
    schemas.py
  services/
    rag_service.py
    agent_service.py
  repositories/
    document_repository.py
    feedback_repository.py
  providers/
    llm_provider.py
    embedding_provider.py
    vector_store.py
tests/
```

### Why This Matters

If provider logic, database logic, API logic, and prompt logic all live in one file, you cannot test or replace parts safely.

Good architecture lets you replace:

- OpenAI with Azure OpenAI or another provider;
- Qdrant with pgvector;
- a naive retriever with a hybrid retriever;
- a prompt with a new prompt version;
- synchronous logic with async calls.

## 3. Type Hints and Data Models

Type hints make data contracts visible:

```python
def retrieve(query: str, tenant_id: str, top_k: int) -> list[RetrievedChunk]:
    ...
```

Pydantic models add runtime validation:

```python
from pydantic import BaseModel, Field

class AskRequest(BaseModel):
    question: str = Field(min_length=1)
    tenant_id: str
    user_id: str

class Citation(BaseModel):
    document_id: str
    chunk_id: str
    source: str
    score: float

class AskResponse(BaseModel):
    answer: str
    citations: list[Citation]
    requires_human_review: bool = False
```

In AI systems, validation prevents vague and unsafe inputs from flowing into expensive model calls.

## 4. Service Layer

The service layer holds business logic:

```text
API route receives request
  -> validates request
  -> calls service
  -> maps service result to response
```

The API should not contain the whole RAG pipeline. It should delegate:

```python
class RagService:
    def __init__(self, retriever, generator, logger):
        self.retriever = retriever
        self.generator = generator
        self.logger = logger

    async def answer(self, request: AskRequest) -> AskResponse:
        chunks = await self.retriever.retrieve(
            query=request.question,
            tenant_id=request.tenant_id,
            top_k=8,
        )
        if not chunks:
            return AskResponse(
                answer="I do not have enough information in the available sources.",
                citations=[],
                requires_human_review=True,
            )
        return await self.generator.generate(request, chunks)
```

## 5. Repository and Provider Boundaries

Repositories hide database details:

```python
class DocumentRepository:
    async def get_document(self, document_id: str) -> Document:
        ...
```

Providers hide external model/vector-store details:

```python
class EmbeddingProvider:
    async def embed_texts(self, texts: list[str]) -> list[list[float]]:
        ...
```

This makes code easier to test with fake implementations.

## 6. Error Handling

AI systems need explicit errors:

```python
class AiServiceError(Exception):
    pass

class NoRelevantContextError(AiServiceError):
    pass

class ProviderTimeoutError(AiServiceError):
    pass

class UnsafeOutputError(AiServiceError):
    pass
```

Different errors require different responses:

| Error | API response | Operational meaning |
| --- | --- | --- |
| validation error | 400 or 422 | bad input |
| auth error | 401 or 403 | access issue |
| no context | 422 or safe answer | retrieval coverage issue |
| provider timeout | 503 | external dependency issue |
| unsafe output | 422 or 500 depending on policy | safety failure |

## 7. Sync vs Async

Async is useful when your service waits on network I/O:

- LLM API calls;
- vector DB queries;
- SQL queries;
- HTTP tools;
- file storage.

Async does not make CPU-heavy work faster by itself. For CPU-heavy parsing, embedding batches, or model inference, use background workers, process pools, or external services.

## 8. Logging

Good logs answer:

- what happened?
- for which request?
- for which user/tenant?
- which model/prompt/index version?
- how long did it take?
- what failed?

Example event:

```json
{
  "event": "rag_answer_completed",
  "request_id": "req_123",
  "tenant_id": "tenant_a",
  "model_version": "gpt-x",
  "prompt_version": "rag_v4",
  "retrieved_k": 8,
  "latency_ms": 1450
}
```

## 9. Testing

You need several test types:

| Test type | Purpose |
| --- | --- |
| unit test | test one function/class |
| contract test | test request/response schema |
| integration test | test DB/vector store/API interaction |
| eval test | test model/RAG quality |
| regression test | detect quality drops after changes |

Unit tests are not enough for LLM quality, but they are still necessary for the non-model system.

## 10. Key Takeaway

Strong Python backend foundations make AI work maintainable. A production AI system should not be a pile of scripts. It should be a tested application with explicit contracts, errors, logs, and replaceable components.
## Numbered References

[1] Python typing: https://docs.python.org/3/library/typing.html
[2] Python logging: https://docs.python.org/3/library/logging.html
[3] Pydantic documentation: https://docs.pydantic.dev/
[4] pytest documentation: https://docs.pytest.org/
[5] FastAPI documentation: https://fastapi.tiangolo.com/
