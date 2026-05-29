# Examples: Python Backend Foundations

Reusable snippets matching `lesson.md`.

## 1. Package layout

```text
src/<pkg>/
  api/         routes.py  dependencies.py
  core/        config.py  logging.py  errors.py  metrics.py
  models/      requests.py  responses.py  domain.py
  services/    rag_service.py
  repositories/document_repository.py  audit_repository.py
  providers/   llm_provider.py  embedding_provider.py  vector_store.py
tests/         unit/  contract/  integration/  fakes/
```

## 2. Config with pydantic-settings (`extra="forbid"`)

```python
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="forbid")
    app_name: str = "ai-service"
    llm_provider: str = Field("openai", pattern="^(openai|azure|fake)$")
    llm_model: str = "gpt-4o-mini"
    database_url: str
    openai_api_key: str | None = None   # never logged
```

## 3. Request/response schemas

```python
from pydantic import BaseModel, Field

class AskRequest(BaseModel):
    question: str = Field(min_length=1, max_length=2000)
    tenant_id: str = Field(min_length=1)
    user_id: str = Field(min_length=1)
    top_k: int = Field(8, ge=1, le=50)

class Citation(BaseModel):
    document_id: str; chunk_id: str; source: str
    score: float = Field(ge=0.0, le=1.0)

class AskResponse(BaseModel):
    answer: str | None
    citations: list[Citation]
    requires_human_review: bool = False
    request_id: str
```

## 4. Provider Protocol + real + fake

```python
from typing import Protocol

class LlmProvider(Protocol):
    async def complete(self, *, system: str, messages: list[dict],
                       max_tokens: int, temperature: float) -> LlmResult: ...

class FakeLlmProvider:
    def __init__(self, canned="FAKE"): self.canned, self.calls = canned, []
    async def complete(self, *, system, messages, **_) -> LlmResult:
        self.calls.append({"system": system, "messages": messages})
        return LlmResult(text=self.canned, input_tokens=0, output_tokens=0, model="fake")
```

## 5. Service layer (dataclass-injected deps)

```python
from dataclasses import dataclass

@dataclass
class RagService:
    retriever: Retriever
    generator: Generator
    audit: AuditRepository

    # request_id is generated at the API boundary (ch03) and passed in,
    # not carried on AskRequest. The response echoes it.
    async def answer(self, req: AskRequest, request_id: str) -> AskResponse:
        chunks = await self.retriever.retrieve(req.question, req.tenant_id, req.top_k)
        if not chunks:
            await self.audit.record_no_answer(req, request_id)
            return AskResponse(answer=None, citations=[], requires_human_review=True,
                               request_id=request_id)
        return await self.generator.generate(req, chunks, request_id)
```

## 6. Error hierarchy + HTTP mapping

```python
class AiServiceError(Exception):
    error_code = "internal_error"; user_message = "Something went wrong."; retryable = False
class ValidationError(AiServiceError): error_code = "validation_error"
class ProviderError(AiServiceError): error_code = "provider_error"; retryable = True
class NoRelevantContextError(AiServiceError): error_code = "no_relevant_context"

# raise from, never swallow the cause:
try:
    await client.complete(...)
except TimeoutError as e:
    raise ProviderError("LLM timed out") from e
```

## 7. Structured logging with redaction

```python
import logging, re, json

def redact_for_log(text: str) -> str:
    text = re.sub(r"(sk-|github_pat_)[A-Za-z0-9_]+", "[REDACTED_KEY]", text)
    return re.sub(r"[\w.+-]+@[\w-]+\.[\w.-]+", "[EMAIL]", text)

logger.info(json.dumps({
    "event": "rag_answer_completed", "request_id": rid, "tenant_id": tid,
    "model_id": "gpt-4o-mini-2024-07-18", "prompt_version": "rag_v4",
    "latency_ms": 1450,
}))
```

## 8. Service test (no network, fakes)

```python
import pytest

@pytest.mark.asyncio
async def test_no_answer_is_audited():
    retriever = FakeRetriever(returns=[]); gen = FakeGenerator(); audit = FakeAudit()
    svc = RagService(retriever=retriever, generator=gen, audit=audit)
    resp = await svc.answer(
        AskRequest(question="x", tenant_id="t", user_id="u"), request_id="r1")
    assert resp.requires_human_review
    assert resp.request_id == "r1"
    assert gen.calls == []                 # LLM never called
    assert audit.no_answer_records == 1
```

## 9. Composition root (only place concretes are wired)

```python
from functools import lru_cache

@lru_cache(maxsize=1)
def get_rag_service() -> RagService:
    s = get_settings()
    return RagService(retriever=build_retriever(s), generator=build_generator(s),
                      audit=build_audit(s))
# tests: app.dependency_overrides[get_rag_service] = lambda: fake_service
```

## 10. Bounded async concurrency

```python
import asyncio
sem = asyncio.Semaphore(8)
async def one(item):
    async with sem:
        return await provider.complete(**item)
results = await asyncio.gather(*[one(i) for i in items])   # never unbounded gather
```
