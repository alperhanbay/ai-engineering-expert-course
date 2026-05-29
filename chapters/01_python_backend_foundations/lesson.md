# Lesson: Python Backend Foundations for AI Systems

## 1. Why This Chapter Exists

Most LLM, RAG, and agent tooling is Python-first. That is convenient and dangerous. It is convenient because almost every model SDK, vector-store client, evaluation library, and orchestration framework — OpenAI's SDK, LangChain, LlamaIndex, LangGraph, RAGAS, DeepEval, the Hugging Face stack — ships a usable Python client first. It is dangerous because the same convenience that lets you build a working RAG demo in a notebook in an afternoon also lets you ship a fragile, untested, unmaintainable application six months later under the same code shape.

Production AI engineering is not notebook engineering. The notebook is a thinking tool; production code is a *contract*. A working notebook proves "this can be done"; a production service proves "this can be done reliably, repeatedly, by someone else, under load, with rollback, and without leaking data." The translation from one to the other is not glamorous, but it is the thing that turns model capability into a system users can trust.

Concretely, you are moving from:

```text
notebook cell  ->  demo output
```

to:

```text
typed package  ->  tested service  ->  HTTP API
              ->  structured logs  ->  observability
              ->  reproducible deployment  ->  release manifest
              ->  rollback story  ->  audit trail
```

Every later chapter assumes you have done this work. Chapter 02 needs a service layer to plug SQL into. Chapter 03 needs typed schemas to expose. Chapters 05–10 need provider abstractions so that swapping a model or vector store is a config change, not a rewrite. Chapter 12 needs structured logs to build observability on. Chapter 15 needs explicit boundaries to apply guardrails to. If your code is one 800-line `main.py`, every subsequent chapter becomes harder than it should be.

The good news: the structural work is *finite*. Once you have a clean package layout, typed contracts, provider adapters, a service layer, structured logging, and a test harness with fakes, you build everything else on top. That is what this chapter teaches you to lay down.

## 2. Project Structure: The First Decision

Code is read more than it is written, and AI code is read by people who will need to change one component — the embedding model, the chunking strategy, the prompt version, the vector store — without rewriting the rest. The package layout you pick on day one shapes how easy that is for the next twelve months.

Use a layered structure that separates the *what* (business behaviour), the *how* (specific tools and providers), and the *where* (persistence and external boundaries):

```text
src/<package_name>/
  api/
    routes.py           # HTTP handlers; thin, no business logic
    dependencies.py     # FastAPI dependencies (auth, tenant injection)
  core/
    config.py           # pydantic-settings; reads .env
    logging.py          # structlog/loguru/stdlib config
    errors.py           # domain exception hierarchy
    metrics.py          # counters, histograms, registry
  models/
    requests.py         # Pydantic request schemas (API boundary)
    responses.py        # Pydantic response schemas
    domain.py           # internal dataclasses (Chunk, Citation, etc.)
  services/
    rag_service.py      # answer(question, tenant_id) -> AnswerDTO
    agent_service.py    # run(graph, state) -> AgentResult
    eval_service.py     # run_eval(dataset) -> EvalReport
  repositories/
    document_repository.py
    feedback_repository.py
    audit_repository.py
  providers/
    llm_provider.py     # Protocol + real + fake implementations
    embedding_provider.py
    vector_store.py
    reranker.py
tests/
  unit/
  contract/
  integration/
  eval/
```

The names matter less than the *separation*. The two rules that pay off:

1. **API layer cannot import from providers directly.** It calls a service. The service calls providers. This means you can write a route test using a fake service without booting any HTTP machinery, and a service test using fake providers without any network call. If you ever find yourself writing `from <pkg>.providers.openai import client` inside `api/routes.py`, you've crossed the line.
2. **Providers cannot import from services or API.** Dependencies point one direction: API → services → providers and repositories. A circular import is a design failure, not a Python quirk.

### Anti-patterns to spot in code review

- **`main.py` with everything in it.** A 600-line file is not a microservice; it is a script with a `__main__` block. Split it before it hits 200 lines.
- **The "utils" dumping ground.** `utils.py` is where modules go to die. Name things by what they own: `tokenizer.py`, `chunking.py`, `prompt_render.py`.
- **Reaching into private state.** If your test does `service._retriever._client._api_key = "fake"`, the boundary is wrong. Inject the fake.
- **Inheritance for code reuse.** Composition (passing providers into services) is almost always clearer than a five-deep base class hierarchy for AI code.

A well-laid-out package is the cheapest investment you will make in the entire course. Get it right once and you will not revisit it.

## 3. Type Hints and Data Models: Making Contracts Visible

Untyped Python code in an AI system is a slow-motion debugging tax. Retrieval can return a list of strings, a list of `Document` objects, a list of `(score, chunk_id, text)` tuples, or `None`. Each downstream caller will assume one of those shapes; one of those callers will be wrong, and the wrongness will surface as a `TypeError` in the generation prompt rather than at the boundary where it originated.

Type hints document expectations. Pydantic models *enforce* them at runtime, which is what you actually want at system boundaries (HTTP requests, provider responses, tool arguments).

### Type hints

Annotate every public function:

```python
def retrieve(
    query: str,
    tenant_id: str,
    top_k: int = 8,
) -> list[RetrievedChunk]:
    ...
```

Use `from __future__ import annotations` at the top of every module to defer annotation evaluation (cheaper, avoids most forward-reference headaches). Run a type checker in CI — `mypy` and `pyright` are both fine. The first time it catches a `None` you forgot to handle in a retrieval fallback, you'll see the payoff.

### Pydantic models at the boundary

Pydantic validates at runtime, coerces types where it can, and rejects what it can't. Use it for HTTP request/response bodies, configuration, and tool argument schemas. Do **not** use Pydantic for every internal dataclass — `dataclasses.dataclass` or `attrs` is lighter and avoids paying the validation cost on every object.

A canonical AI service schema:

```python
from pydantic import BaseModel, Field, field_validator


class AskRequest(BaseModel):
    question: str = Field(min_length=1, max_length=2000)
    tenant_id: str = Field(min_length=1)
    user_id: str = Field(min_length=1)
    # Optional knobs are explicit, not magic kwargs.
    top_k: int = Field(default=8, ge=1, le=50)

    @field_validator("question")
    @classmethod
    def reject_control_chars(cls, v: str) -> str:
        if any(ord(c) < 0x20 and c not in "\n\r\t" for c in v):
            raise ValueError("question contains control characters")
        return v


class Citation(BaseModel):
    document_id: str
    chunk_id: str
    source: str
    page: int | None = None
    score: float = Field(ge=0.0, le=1.0)


class AskResponse(BaseModel):
    answer: str
    citations: list[Citation]
    requires_human_review: bool = False
    request_id: str
```

Two non-obvious decisions in that block:

- `question` has a `max_length`. Without it, an attacker can send a 5 MB prompt and you'll spend real money before refusing. Validation at the boundary is cheap.
- `score` is bounded `[0, 1]`. If your retriever returns raw dot products instead of normalised similarities, you'll fail validation immediately instead of confusing downstream rerankers.

### Discriminated unions for tool calls

When you start building agents (chapter 10), tool calls are heterogeneous: one tool takes `{document_id}`, another takes `{user_email, subject, body}`. Use a Pydantic discriminated union so that the type system understands which tool a call is for:

```python
from typing import Literal, Union
from pydantic import BaseModel, Field


class SearchDocsArgs(BaseModel):
    tool: Literal["search_docs"]
    query: str
    top_k: int = 5


class SendEmailArgs(BaseModel):
    tool: Literal["send_email"]
    to: str
    subject: str
    body: str


ToolCall = Union[SearchDocsArgs, SendEmailArgs]


class AgentMessage(BaseModel):
    role: Literal["tool_call"]
    call: ToolCall = Field(discriminator="tool")
```

This will pay off when the LLM hallucinates a tool name — Pydantic will reject the message at the boundary rather than letting bad input reach the `send_email` implementation.

## 4. Configuration and Secrets

Configuration that lives in code is a bug waiting to happen. The model name should differ between dev and prod. The vector-store URL should not be hard-coded. Secrets must never be committed.

The cleanest pattern is `pydantic-settings` (Pydantic's settings extension), reading from environment variables with a `.env.example` checked into the repo (no real values):

```python
# core/config.py
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="forbid"
    )

    # Public
    app_name: str = "ai-service"
    log_level: str = "INFO"

    # Providers
    llm_provider: str = Field(default="openai", pattern="^(openai|azure|anthropic|fake)$")
    llm_model: str = "gpt-4o-mini"
    embedding_model: str = "text-embedding-3-small"

    # Infrastructure
    database_url: str
    vector_store_url: str

    # Secrets (never logged; see logging section)
    openai_api_key: str | None = None
    azure_openai_api_key: str | None = None
```

`extra="forbid"` is a real safety net: misspelled env vars (`OPENAI_KEY` instead of `OPENAI_API_KEY`) become startup errors instead of silent "key not found" failures at request time. Catching this at boot saves a 3 a.m. incident.

The `.env.example` lists every variable with a placeholder:

```
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/ai
VECTOR_STORE_URL=http://localhost:6333
OPENAI_API_KEY=sk-...REPLACE...
```

Two rules that should be non-negotiable:

1. **`.env` is in `.gitignore`.** Always. The first time you commit a real key, you're rotating it.
2. **Secrets are not constructor arguments to user-facing classes.** Pass them only to provider adapters at composition time, and never into Pydantic response models (one accidental `.model_dump()` and your key is in a log line).

## 5. The Service Layer: Where Behaviour Lives

The service layer holds business behaviour, decoupled from how the request arrived (HTTP, CLI, batch job) and from which specific providers are wired in. It is the thing you test the most. If you do this right, the API layer becomes mechanical translation:

```python
# api/routes.py
@router.post("/ask", response_model=AskResponse)
async def ask(
    request: AskRequest,
    service: RagService = Depends(get_rag_service),
) -> AskResponse:
    return await service.answer(request)
```

There is nothing interesting here, and that is the point. The interesting logic is in `RagService.answer`:

```python
# services/rag_service.py
from dataclasses import dataclass


@dataclass
class RagService:
    retriever: Retriever        # provider Protocol
    generator: Generator        # provider Protocol
    audit: AuditRepository      # repository
    metrics: MetricsRecorder

    async def answer(self, request: AskRequest) -> AskResponse:
        # request_id is set at the API boundary as a contextvar (see section 10),
        # not carried on AskRequest. The response echoes it.
        request_id = current_request_id()
        with self.metrics.timer("rag_answer", tenant=request.tenant_id):
            chunks = await self.retriever.retrieve(
                query=request.question,
                tenant_id=request.tenant_id,
                top_k=request.top_k,
            )

            if not chunks:
                await self.audit.record_no_answer(request, request_id)
                return AskResponse(
                    answer="I do not have enough information in the available sources.",
                    citations=[],
                    requires_human_review=True,
                    request_id=request_id,
                )

            result = await self.generator.generate(request, chunks)
            await self.audit.record_answer(request, result)
            return result
```

Several deliberate choices in there:

- The service is a `dataclass` with explicit dependencies. No global imports of `openai_client`. Tests inject fakes.
- The no-answer branch is *first-class* and audited. Refusal is a feature, not an edge case.
- The metrics timer wraps the whole call. You get latency observability for free, and adding cost tracking later is a one-line change.
- The return type is the same `AskResponse` the API will serialise. The route handler does not invent its own response shape.

### Dependency injection without a framework

You do not need a DI container. A small `dependencies.py` module that composes services and caches them per app lifetime is enough:

```python
# api/dependencies.py
from functools import lru_cache
from .config import Settings

@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


@lru_cache(maxsize=1)
def get_rag_service() -> RagService:
    settings = get_settings()
    retriever = build_retriever(settings)
    generator = build_generator(settings)
    return RagService(retriever=retriever, generator=generator, ...)
```

In tests, you override `get_rag_service` with a fake. FastAPI's `app.dependency_overrides[get_rag_service] = lambda: fake_service` makes this idiomatic.

## 6. Provider Adapters: The Lock-in Firewall

Every external system that can change should sit behind an adapter you own. That includes LLMs, embedding APIs, vector stores, rerankers, and tool endpoints. The cost of writing the adapter once is paid back the first time you need to compare two providers, run tests offline, or swap a vendor.

Define a `Protocol` (structural typing), not an ABC. The structural type is satisfied by any class with matching methods, including ad-hoc fakes in tests:

```python
# providers/llm_provider.py
from typing import Protocol


class LlmProvider(Protocol):
    async def complete(
        self,
        *,
        system: str,
        messages: list[dict],
        max_tokens: int,
        temperature: float,
    ) -> LlmResult:
        ...
```

Then implement it twice — once for real, once fake:

```python
class OpenAiLlmProvider:
    def __init__(self, client, model: str) -> None:
        self._client = client
        self._model = model

    async def complete(self, *, system, messages, max_tokens, temperature) -> LlmResult:
        response = await self._client.chat.completions.create(
            model=self._model,
            messages=[{"role": "system", "content": system}, *messages],
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return LlmResult(
            text=response.choices[0].message.content or "",
            input_tokens=response.usage.prompt_tokens,
            output_tokens=response.usage.completion_tokens,
            model=response.model,
        )


class FakeLlmProvider:
    """Deterministic fake for tests; never hits a network."""

    def __init__(self, canned: str = "FAKE_ANSWER") -> None:
        self._canned = canned
        self.calls: list[dict] = []

    async def complete(self, *, system, messages, **_) -> LlmResult:
        self.calls.append({"system": system, "messages": messages})
        return LlmResult(text=self._canned, input_tokens=0, output_tokens=0, model="fake")
```

A few practical notes:

- The Protocol uses keyword-only arguments. Real providers diverge on parameter names; the adapter normalises them, so the service code never sees `max_completion_tokens` vs `max_output_tokens` vs `max_tokens`.
- The fake records calls. Half of all retrieval/agent tests are "did we call the LLM with the right system prompt?" — the recorded calls let the test assert that without mocks.
- The provider returns a domain `LlmResult`, not the raw OpenAI/Anthropic/Azure response. That's deliberate. Your service should not know what `response.choices[0].message.content` looks like for any specific vendor.

### Timeouts and retries belong here

Each adapter should set its own timeout policy and retry behaviour. Without it, a slow provider blocks your event loop and burns through a request budget:

```python
import asyncio
import httpx

class OpenAiLlmProvider:
    async def complete(self, **kwargs) -> LlmResult:
        for attempt in range(3):
            try:
                async with asyncio.timeout(15):  # whole-call timeout
                    return await self._call(**kwargs)
            except (httpx.TimeoutException, httpx.HTTPStatusError) as e:
                if attempt == 2 or not _is_retryable(e):
                    raise
                await asyncio.sleep(2 ** attempt)
```

The retry classification (`_is_retryable`) belongs *inside* the adapter — your service should not have to reason about which HTTP codes from which vendor are retryable.

## 7. Repositories: A Stable Interface to Storage

A repository hides persistence details behind methods that name *what* you want, not *how* SQL spells it:

```python
class DocumentRepository(Protocol):
    async def get(self, document_id: str, tenant_id: str) -> Document | None: ...
    async def insert(self, doc: NewDocument) -> Document: ...
    async def soft_delete(self, document_id: str, actor: str, reason: str) -> None: ...


class FeedbackRepository(Protocol):
    async def record(self, feedback: Feedback) -> None: ...
    async def list_for_request(self, request_id: str) -> list[Feedback]: ...
```

A few rules:

- **Repository methods are not generic.** A repository for `Document` has methods about documents. Resist the urge to write a single `Repository[T]` superclass with `find_by(criteria)` — you lose the entire benefit of a typed contract.
- **Tenant id is a required parameter, not optional.** Multi-tenancy is the most common place a missing parameter becomes a cross-tenant data leak. Forcing it into the signature makes it impossible to forget.
- **Soft delete carries an actor and a reason.** Audit lives in chapter 02 in detail; the repository signature is the first place you encode that "deletion is not free."

The asynchronous session lifecycle (SQLAlchemy `AsyncSession`, or whatever you pick) is the implementation's problem, not the service's. The service receives a constructed repository and calls methods on it.

## 8. Errors: Make Failure Modes Visible

The default Python posture is to let exceptions propagate. In an AI service, that translates to "every failure becomes a 500 with a stack trace in the response body" — which is unhelpful to the client and a small security bug (it leaks internals).

Design a small exception hierarchy that maps to real operational categories:

```python
# core/errors.py

class AiServiceError(Exception):
    """Base; carries a stable error_code and an optional cause."""
    error_code: str = "internal_error"
    user_message: str = "Something went wrong."
    retryable: bool = False


class ValidationError(AiServiceError):
    error_code = "validation_error"
    retryable = False


class AuthorizationError(AiServiceError):
    error_code = "authorization_error"
    user_message = "You do not have access to this resource."
    retryable = False


class NoRelevantContextError(AiServiceError):
    """No supporting evidence in the knowledge base. Not always an error."""
    error_code = "no_relevant_context"
    user_message = "I could not find enough supporting evidence to answer."
    retryable = False


class ProviderError(AiServiceError):
    """External provider problem (LLM, vector store, embedding)."""
    error_code = "provider_error"
    retryable = True


class UnsafeOutputError(AiServiceError):
    error_code = "unsafe_output"
    user_message = "The response was blocked by a safety policy."
    retryable = False
```

The API layer translates these to HTTP, preserving the `error_code`:

```python
# api/routes.py
@app.exception_handler(AiServiceError)
async def handle_ai_error(request: Request, exc: AiServiceError):
    status = {
        "validation_error": 422,
        "authorization_error": 403,
        "no_relevant_context": 422,
        "provider_error": 503,
        "unsafe_output": 422,
        "internal_error": 500,
    }.get(exc.error_code, 500)
    return JSONResponse(
        status_code=status,
        content={
            "error": {
                "code": exc.error_code,
                "message": exc.user_message,
                "retryable": exc.retryable,
                "request_id": request.state.request_id,
            }
        },
    )
```

| Error class | Typical HTTP | Operational meaning |
| --- | --- | --- |
| `ValidationError` | 422 | bad input; client should fix and not retry |
| `AuthorizationError` | 403 | access issue; auth team's problem |
| `NoRelevantContextError` | 422 | retrieval coverage issue; product/data problem |
| `ProviderError` | 503 | external dependency; safe to retry with backoff |
| `UnsafeOutputError` | 422 | safety failure; security/policy problem |
| anything else | 500 | bug; page the engineer |

The classification matters because it tells your monitoring what to alert on: a `provider_error` spike means call the model vendor; a `no_relevant_context` spike means the corpus is wrong; a `validation_error` spike means a client is misusing your API.

### Chaining and `raise from`

Never swallow the cause. Always:

```python
try:
    result = await client.complete(...)
except httpx.TimeoutException as e:
    raise ProviderError("LLM timed out") from e
```

The `from e` preserves the original traceback in logs while exposing a clean domain error to the caller. Without it, debugging an incident becomes a guessing game.

## 9. Sync vs Async: Concurrency Where It Pays

LLM serving is dominated by network waits. A single `/ask` request typically does:

1. one vector-store query (network)
2. one or more LLM API calls (network, slow)
3. several DB calls (network, fast)

If your handler runs synchronously, your process can serve roughly one request at a time per worker. With `asyncio`, the same process can hold hundreds of pending requests — none of them doing CPU work, all of them waiting on a socket. The throughput difference is dramatic.

But async has sharp edges. Two failure modes worth memorising:

### Blocking code in async functions

A common bug:

```python
async def answer(self, request: AskRequest) -> AskResponse:
    # ...
    digest = hashlib.sha256(huge_text.encode()).hexdigest()  # CPU work, blocks the loop
    response = sync_openai_client.chat.completions.create(...)  # synchronous call!
```

Both of those lines stop the entire event loop. While they run, *every* other in-flight request in this worker is frozen. Use the async client (`openai.AsyncOpenAI`), and push true CPU work to `asyncio.to_thread` or a process pool:

```python
digest = await asyncio.to_thread(_hash, huge_text)
```

### Unbounded concurrency

If you write `await asyncio.gather(*[provider.complete(...) for _ in range(1000)])`, you have just opened 1000 concurrent connections to your provider and probably exceeded its rate limit, your file descriptor budget, and your memory. Always bound concurrency:

```python
sem = asyncio.Semaphore(8)

async def one(item):
    async with sem:
        return await provider.complete(...)

results = await asyncio.gather(*[one(i) for i in items])
```

Eight is a reasonable starting bound for an LLM provider; you'll tune it from real numbers later.

### When async hurts you

Async is not a free lunch. For a CLI tool, a batch job, or a small worker that processes one item at a time, plain sync code is simpler to read and debug. Reach for async when you have *concurrency* you want to exploit, not because it's the modern thing.

## 10. Structured Logging: Logs You Can Query

Free-text logs are a debugging black hole. "Something failed in retrieval" tells you nothing; "retrieval failed for `request_id=req_a31b9` tenant=`acme` top_k=8 latency_ms=14021 error=`provider_timeout`" tells you everything.

Use structured logs (JSON or logfmt). `structlog`, `loguru`, or stdlib `logging` with a JSON formatter are all fine. The library matters less than the discipline of *what fields you log*.

A minimum per-request log surface:

```json
{
  "ts": "2026-05-26T12:30:01.482Z",
  "level": "info",
  "event": "rag_answer_completed",
  "request_id": "req_a31b9c",
  "tenant_id": "acme",
  "user_id": "user_4711",
  "model_id": "gpt-4o-mini-2024-07-18",
  "prompt_version": "rag_v4",
  "embedding_model_id": "text-embedding-3-small",
  "index_version": "v17",
  "retrieved_k": 8,
  "answered": true,
  "no_answer": false,
  "latency_ms": 1450,
  "input_tokens": 1320,
  "output_tokens": 256
}
```

Two non-obvious rules:

1. **`request_id` is generated at the API boundary and threaded through everything.** Inject it as a context variable (`contextvars.ContextVar`) so every log line in the request automatically carries it. Without this, correlating "the LLM call that took 14 seconds" with "the slow request" is manual archaeology.
2. **Never log secrets or raw PII at default verbosity.** If your policy is "log redacted prompt at DEBUG only" and your DEBUG level is enabled in prod, the policy is fiction. Build a redaction helper and unit-test it:

```python
def redact_for_log(prompt: str) -> str:
    # strip obvious patterns: API keys, long base64, emails, phone numbers
    ...
```

The full PII policy comes in chapter 15. The point here is to have a *place* to apply it consistently.

## 11. Testing Strategy: What to Test, How, and With What

AI service tests come in distinct flavours. Mixing them is a common mistake — a unit test that hits the real LLM is slow, expensive, and flaky; an "integration test" that mocks the database tests almost nothing.

| Test type | Scope | Speed | What it proves |
| --- | --- | --- | --- |
| Unit | one function/class with fakes | milliseconds | the logic is correct given mocked inputs |
| Contract | API request/response schemas | milliseconds | the HTTP contract matches the schema |
| Integration | real DB + fake providers | seconds | the persistence layer actually works |
| Eval | full pipeline against golden set | minutes | the system's quality has not regressed |
| Regression | a previously-failing case still passes | seconds | a fix stays fixed |

The seed test suite for chapter 01 should cover:

1. **Pydantic validation rejects bad input.** A missing `tenant_id` returns a 422 with the field name and no stack trace.
2. **Service happy path with fakes.** `RagService.answer` returns the expected `AskResponse` shape; the fake retriever and fake generator are called with expected arguments.
3. **No-answer path is audited.** When the fake retriever returns `[]`, the service returns `requires_human_review=True` *and* writes to the audit repository.
4. **Provider error mapping.** When the fake LLM raises `ProviderTimeout`, the API returns 503 with `error_code=provider_error`.
5. **Request id is propagated.** A request id set at the boundary appears in every log emitted during the request (use `caplog` and a context filter).

A canonical service-layer test:

```python
import pytest
from <pkg>.services.rag_service import RagService
from <pkg>.providers.fakes import FakeRetriever, FakeGenerator, FakeAudit


@pytest.mark.asyncio
async def test_no_answer_path_is_audited():
    retriever = FakeRetriever(returns=[])
    generator = FakeGenerator()
    audit = FakeAudit()
    service = RagService(retriever=retriever, generator=generator, audit=audit, ...)

    response = await service.answer(AskRequest(
        question="anything", tenant_id="t1", user_id="u1",
    ))

    assert response.requires_human_review
    assert generator.calls == []                # never called the LLM
    assert audit.no_answer_records == 1         # audit was written
```

The test is short, fast, and tells you exactly what behaviour is being asserted. No mocking framework, no network, no flakes. This is the bar for unit tests.

### When to *not* mock

Mocking is overused. Two cases where it is wrong:

- **The thing you're testing is the integration.** A test for `DocumentRepository.insert` that mocks the SQLAlchemy session tests your mock, not your repository. Use a real SQLite or Postgres test database.
- **The mock encodes assumptions you didn't verify.** Mocking the OpenAI client to return `{"choices": [{"message": {"content": "x"}}]}` is fine until the SDK changes shape and your tests pass while production breaks. Prefer a thin fake adapter that satisfies the same `Protocol` your real code uses.

## 12. Common Mistakes and Anti-Patterns

A checklist of things to scan for in your own code and in PR reviews:

1. **Provider calls inside route handlers.** You cannot unit-test routes without booting HTTP and you cannot test providers without booting routes. Fix: extract to a service.
2. **Free-text logs.** `logger.info(f"got result for {user}: {result}")` is not queryable. Fix: structured logging with named fields.
3. **`Exception` caught and swallowed.** `except Exception: pass` is a guarantee of a future incident. At minimum, log and re-raise.
4. **Sync HTTP client in async code.** Using `requests` inside an `async def` is the single most common production performance bug. Fix: use `httpx.AsyncClient` or the vendor's async SDK.
5. **Tests that depend on env vars being unset.** A test that fails when a developer has `OPENAI_API_KEY` set in their shell is a flaky test. Fix: explicitly set/clear in a fixture.
6. **Implicit ordering between tests.** Test A creates a document; test B assumes it exists. The CI runner in parallel mode makes this nondeterministic. Fix: each test sets up its own state, ideally in a transaction that rolls back.
7. **`from <pkg> import *`.** Hides what a module depends on; breaks type checkers; surfaces no errors when something disappears. Don't.
8. **Logging the prompt at INFO.** Prompts often contain user input which often contains PII. Fix: redact, or log a hash, or log at DEBUG only.
9. **Wrapping every line in try/except.** Errors should bubble up to a layer that *knows* what to do (the API handler). Catching `ValueError` deep in a retriever and turning it into `None` makes upstream debugging impossible.
10. **No timeout on outbound calls.** A provider hang turns into a process hang. Always set a whole-call timeout in the adapter.

## 13. Production Failure Modes

The chapter's `deep_dive.md` enumerates concept-level failures; this section names the *operational* ones you should write runbooks for in chapter 12.

- **A new dependency upgrade silently changes Pydantic v1 → v2 behaviour.** Defensive measure: pin major versions, run the contract test suite on every dependency PR.
- **Async test passes locally, hangs in CI.** Usually a missing `await` or a context leak between tests. Defensive measure: pytest with `--timeout=30` so a hung test fails loudly.
- **Memory grows unbounded under load.** A leak from caching responses keyed by request id, or unbounded log buffering. Defensive measure: memory metric, profile periodically.
- **Worker dies under load and orchestrator restarts it forever.** Often a startup-time validation failure that only happens with prod env vars. Defensive measure: validate config on import in a smoke test that runs at deploy time.
- **A long-running async task is cancelled mid-write.** Half-written documents, dangling rows. Defensive measure: use transactions; or write atomically; or use idempotency keys (chapter 03).
- **Provider returns a 200 with an error body.** Real example: rate limits sometimes come back as 200 with `{"error": "rate_limited"}`. Defensive measure: the provider adapter parses bodies, not status codes alone.

## 14. Security and Privacy at the Foundation Layer

Chapter 15 covers the full security story (OWASP LLM Top 10, PII, audit logs, guardrails). At the *foundation* layer, three things are worth getting right on day one:

1. **Tenancy in the type system.** Every retrieval, every storage call, every cache key carries a `tenant_id`. Make it impossible to forget by putting it in the function signature as a required parameter. The cost is a few extra arguments; the benefit is that an entire class of cross-tenant data leaks becomes a compile-time error.
2. **No secrets in logs.** The logging redaction helper from section 10 is not optional. Add a unit test that emits a log line containing a fake API key and asserts the formatter strips it.
3. **No raw user input in error responses.** When validation fails, return "missing field `tenant_id`", not "your input was `<5 KB of attacker-controlled text>`". Echoing input is how stored-XSS-like issues sneak in even on JSON APIs.

A reasonable default header set for the API:

```python
app.add_middleware(
    SecurityHeadersMiddleware,
    headers={
        "X-Content-Type-Options": "nosniff",
        "Strict-Transport-Security": "max-age=63072000; includeSubDomains",
        "Referrer-Policy": "no-referrer",
    },
)
```

These are not specific to AI but missing them is a common audit finding.

## 15. Composition Root: One Place Where Concrete Wiring Lives

A subtle but important pattern: every concrete dependency wiring decision — which LLM provider class, which vector store URL, which retry policy — should live in *one* module, the composition root. The rest of the codebase only sees Protocols and abstract dependencies.

For a FastAPI app the composition root is `api/dependencies.py`. For a CLI tool it's the `__main__` block of the entry script. For a worker it's the worker's startup function. The composition root is the only place where you write `OpenAiLlmProvider(...)` or `QdrantVectorStore(...)`. Everywhere else, code receives a `LlmProvider` or `VectorStore` interface.

```python
# api/dependencies.py — the only file that knows about specific vendor classes
from functools import lru_cache

from .config import Settings
from <pkg>.providers.openai_llm import OpenAiLlmProvider
from <pkg>.providers.azure_llm import AzureOpenAiLlmProvider
from <pkg>.providers.fake_llm import FakeLlmProvider
from <pkg>.providers.qdrant_store import QdrantVectorStore
from <pkg>.providers.pgvector_store import PgVectorStore
from <pkg>.services.rag_service import RagService


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


def _build_llm(settings: Settings) -> LlmProvider:
    match settings.llm_provider:
        case "openai":
            return OpenAiLlmProvider(client=..., model=settings.llm_model)
        case "azure":
            return AzureOpenAiLlmProvider(client=..., deployment=settings.llm_model)
        case "fake":
            return FakeLlmProvider(canned="dev_answer")
        case other:
            raise ValueError(f"unknown llm_provider: {other}")


def _build_vector_store(settings: Settings) -> VectorStore:
    if "qdrant" in settings.vector_store_url:
        return QdrantVectorStore(url=settings.vector_store_url)
    if "postgresql" in settings.vector_store_url:
        return PgVectorStore(dsn=settings.vector_store_url)
    raise ValueError(f"unsupported vector store: {settings.vector_store_url}")


@lru_cache(maxsize=1)
def get_rag_service() -> RagService:
    settings = get_settings()
    llm = _build_llm(settings)
    vector = _build_vector_store(settings)
    # ... build retriever, generator, audit, metrics ...
    return RagService(retriever=..., generator=..., audit=..., metrics=...)
```

The payoff: when a teammate asks "where do I add a new LLM provider?", the answer is "implement the `LlmProvider` Protocol, then add a `case` in `_build_llm`." No grep across the codebase, no surprise import in a service file. The composition root is a small, slow-changing, easily reviewable file.

A diagnostic question for any AI codebase: how many files would you have to touch to swap OpenAI for Anthropic? If the answer is more than two (a new provider class and one `case` in the composition root), the boundaries are weak.

## 16. Performance Baselines for the Skeleton

You won't optimise seriously until chapter 13, but the foundation deserves baseline numbers so you notice when something is wrong. Run these on the skeleton you built with all fake providers (no real network) — they measure your code, not anyone's LLM.

A reasonable target on a modern laptop with the fake-only stack:

| Metric | Target | What it tests |
| --- | --- | --- |
| `/ask` p50 latency | < 5 ms | overhead of routing + validation + service path |
| `/ask` p95 latency | < 20 ms | tail behaviour under light contention |
| concurrent throughput (8 workers, 100 connections) | > 2000 req/s | event loop is not blocked |
| memory after 10k requests | flat (no slope) | no leaking caches |
| cold start | < 1.5 s | import graph hasn't ballooned |

If your p95 against fake providers is in the *hundreds* of milliseconds, you have a synchronous call somewhere, or a CPU-bound operation per request (hashing a huge string, recompiling a regex, re-reading a file). Profile with `py-spy` and find it before adding any real provider; otherwise you'll incorrectly blame the LLM for what your own code is doing.

A simple smoke benchmark uses `wrk`, `oha`, or just `hey`:

```bash
hey -n 5000 -c 50 -m POST -T application/json \
    -d '{"question":"hello","tenant_id":"t1","user_id":"u1"}' \
    http://localhost:8000/ask
```

Capture the numbers in `my_work/baseline.md`. When chapter 12 (observability) tells you to set SLOs, you'll have actual data instead of guesses.

## 17. Suggested Test Repository Layout

For reference, a workable test layout that aligns with the test types from section 11:

```text
tests/
  conftest.py                # shared fixtures: app, settings_override, fakes
  fakes/
    __init__.py
    llm.py                   # FakeLlmProvider
    retriever.py             # FakeRetriever
    generator.py             # FakeGenerator
    audit.py                 # FakeAudit, FakeFeedbackRepo
  unit/
    test_rag_service.py
    test_errors_mapping.py
    test_config.py
    test_redact_for_log.py
  contract/
    test_ask_endpoint_schema.py
    test_openapi_snapshot.py
  integration/
    test_document_repository_sqlite.py
    test_audit_repository.py
  eval/
    test_golden_smoke.py     # single-case golden eval as a smoke gate in CI
```

A few decisions worth copying:

- `conftest.py` provides a `client` fixture that overrides `get_rag_service` with a fake. Every contract test reuses it.
- `test_openapi_snapshot.py` writes a hash of the generated OpenAPI spec and fails if it drifts unexpectedly. Combined with the requirement that real OpenAPI changes are deliberate, this catches accidental schema breakage.
- Integration tests use SQLite-in-memory or an ephemeral Postgres container — never the dev database.
- The eval smoke runs a single golden case to make sure the *plumbing* still wires up end-to-end. The full eval suite runs separately, on demand, not on every PR.

This layout will carry you through chapters 02 and 03 without rework.

## 18. The Capstone Checklist

By the end of this chapter, the following should exist in your `chapters/01_python_backend_foundations/my_work/`:

- A Python package skeleton matching the layout in section 2, importable as `python -c "import <pkg>"`.
- `core/config.py` reading from env vars via `pydantic-settings`, with a `.env.example` checked in.
- Pydantic schemas for `AskRequest`, `AskResponse`, `Citation`.
- A `RagService` with constructor-injected `Retriever`, `Generator`, and `AuditRepository` Protocols.
- Fake implementations of those Protocols in a `tests/fakes/` module.
- An exception hierarchy in `core/errors.py`.
- A structured-logging configuration emitting JSON with `request_id`, `tenant_id`, `model_id`, `prompt_version`, `latency_ms` at minimum.
- A `tests/unit/` suite that exercises the service's happy path, no-answer path, and error mapping — all running in under five seconds with no network.
- A README in `my_work/` listing every file and what it does, in one paragraph.

If you can hand this to a teammate and they can extend it without asking you any questions, the chapter is done.

## 19. Key Takeaway

Production AI systems are made of the same boring components that make any production service work: a clear package layout, typed contracts, explicit error categories, structured logs, replaceable provider adapters, and tests that run without a network. The AI part is what people talk about in conference talks. The boring part is what keeps the AI part shipping reliably.

Get this layer right once and the next sixteen chapters will move ten times faster.

## Numbered References

[1] Python typing: https://docs.python.org/3/library/typing.html
[2] Python logging: https://docs.python.org/3/library/logging.html
[3] Pydantic documentation: https://docs.pydantic.dev/
[4] pytest documentation: https://docs.pytest.org/
[5] FastAPI documentation: https://fastapi.tiangolo.com/
