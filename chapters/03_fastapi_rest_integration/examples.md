# Examples: FastAPI, REST, and Integration

Reusable snippets matching `lesson.md`. Paste, adapt, commit.

## 1. App bootstrap with router-level auth

```python
from fastapi import APIRouter, Depends, FastAPI
from .deps import request_context

app = FastAPI(title="ai-service", version="1.0.0")

# Every route on this router requires a valid token + RequestContext
api = APIRouter(prefix="/v1", dependencies=[Depends(request_context)])

app.include_router(api)
app.include_router(public_router)   # /healthz lives here, no auth
```

## 2. Auth dependency

```python
from fastapi import Depends, Header, HTTPException
from dataclasses import dataclass
import uuid


@dataclass(frozen=True)
class RequestContext:
    request_id: str
    tenant_id: str
    user_id: str
    role: str


async def request_context(
    authorization: str = Header(...),
    x_request_id: str | None = Header(default=None),
) -> RequestContext:
    if not authorization.startswith("Bearer "):
        raise HTTPException(401, detail={"code": "authorization_error",
                                         "message": "missing bearer token"})
    claims = await verify_token(authorization[len("Bearer "):])
    return RequestContext(
        request_id=x_request_id or f"req_{uuid.uuid4().hex[:12]}",
        tenant_id=claims["tenant_id"],
        user_id=claims["sub"],
        role=claims["role"],
    )
```

## 3. Pydantic schema with `extra="forbid"`

```python
from pydantic import BaseModel, ConfigDict, Field


class AskRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    question: str = Field(min_length=1, max_length=2000,
                          description="user's natural-language question")
    top_k: int = Field(default=8, ge=1, le=50)
```

## 4. Unified error handler

```python
from fastapi import Request
from fastapi.responses import JSONResponse


_STATUS = {
    "validation_error": 422,
    "authorization_error": 403,
    "no_relevant_context": 422,
    "provider_error": 503,
    "unsafe_output": 422,
    "rate_limited": 429,
    "not_found": 404,
}


@app.exception_handler(AiServiceError)
async def handle_ai_error(request: Request, exc: AiServiceError):
    return JSONResponse(
        status_code=_STATUS.get(exc.error_code, 500),
        content={"error": {
            "code": exc.error_code,
            "message": exc.user_message,
            "retryable": exc.retryable,
            "request_id": getattr(request.state, "request_id", None),
        }},
    )
```

## 5. Streaming endpoint (SSE)

```python
from fastapi.responses import StreamingResponse
import asyncio, json


def _sse(event: str, data: dict) -> str:
    return f"event: {event}\ndata: {json.dumps(data)}\n\n"


@router.post("/ask/stream")
async def ask_stream(request: AskRequest,
                     ctx: RequestContext = Depends(request_context),
                     service: RagService = Depends(get_rag_service)):
    async def gen():
        yield _sse("session", {"request_id": ctx.request_id})
        last_keepalive = asyncio.get_event_loop().time()
        try:
            async for ev in service.answer_stream(request, ctx):
                yield _sse(ev.type, ev.payload)
                now = asyncio.get_event_loop().time()
                if now - last_keepalive > 15:
                    yield ": keepalive\n\n"
                    last_keepalive = now
            yield _sse("done", {})
        except AiServiceError as e:
            yield _sse("error", {"code": e.error_code,
                                 "message": e.user_message,
                                 "request_id": ctx.request_id})

    return StreamingResponse(gen(), media_type="text/event-stream")
```

## 6. SSE client (curl + httpx)

```bash
# curl: tail an SSE stream
curl -N -X POST http://localhost:8000/v1/ask/stream \
    -H "Authorization: Bearer dev_token" \
    -H "Content-Type: application/json" \
    -d '{"question":"What is the claim deadline?","top_k":5}'
```

```python
# httpx async client
import httpx, json

async def stream():
    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream(
            "POST", "http://localhost:8000/v1/ask/stream",
            headers={"Authorization": "Bearer dev_token"},
            json={"question": "What is the claim deadline?"},
        ) as resp:
            event = None
            async for line in resp.aiter_lines():
                if line.startswith("event: "):
                    event = line[len("event: "):]
                elif line.startswith("data: "):
                    data = json.loads(line[len("data: "):])
                    print(event, data)
```

## 7. Idempotent ingestion endpoint

```python
@router.post("/documents", response_model=JobAccepted, status_code=202)
async def ingest_document(
    request: IngestRequest,
    ctx: RequestContext = Depends(request_context),
    idempotency_key: str | None = Header(default=None, alias="Idempotency-Key"),
    jobs: JobService = Depends(get_job_service),
):
    job_id = await jobs.enqueue(
        kind="document.ingest",
        tenant_id=ctx.tenant_id,
        actor_id=ctx.user_id,
        payload=request.model_dump(),
        idempotency_key=idempotency_key,
    )
    return JobAccepted(job_id=job_id, status_url=f"/v1/jobs/{job_id}")
```

## 8. Contract test for missing field

```python
import pytest

@pytest.mark.parametrize("missing", ["question"])
def test_ask_rejects_missing_required_fields(client, missing):
    body = {"question": "hello", "top_k": 5}
    body.pop(missing)
    r = client.post("/v1/ask", json=body, headers={"Authorization": "Bearer fake"})
    assert r.status_code == 422
    err = r.json()["error"]
    assert err["code"] == "validation_error"
    assert missing in err["message"]
    assert err["request_id"]
```

## 9. OpenAPI snapshot test

```python
import json
from pathlib import Path

def test_openapi_schema_unchanged(client):
    spec = client.get("/openapi.json").json()
    actual = json.dumps(spec, sort_keys=True, indent=2)
    snapshot = (Path(__file__).parent / "openapi_snapshot.json").read_text()
    assert actual == snapshot, (
        "OpenAPI drift. Run `python scripts/update_openapi_snapshot.py` "
        "if the change is intentional, then re-review the diff."
    )
```

## 10. Per-tenant rate limiter (token bucket via Redis)

```python
import time
from fastapi import HTTPException

class TenantRateLimiter:
    def __init__(self, redis, rps: int, burst: int):
        self.redis = redis; self.rps = rps; self.burst = burst

    async def check(self, tenant_id: str) -> None:
        key = f"rl:{tenant_id}"
        now = time.time()
        # naive token bucket via Lua or Redis transaction; see slowapi for a hardened version
        tokens = float(await self.redis.get(key) or self.burst)
        last = float(await self.redis.get(f"{key}:t") or now)
        tokens = min(self.burst, tokens + (now - last) * self.rps)
        if tokens < 1:
            retry = int((1 - tokens) / self.rps) + 1
            raise HTTPException(429, headers={"Retry-After": str(retry)},
                                detail={"code": "rate_limited",
                                        "message": "tenant quota exceeded",
                                        "retryable": True})
        await self.redis.mset({key: tokens - 1, f"{key}:t": now})
```

## 11. Whole-request timeout wrapper

```python
import asyncio

@router.post("/ask")
async def ask(request: AskRequest,
              ctx: RequestContext = Depends(request_context),
              service: RagService = Depends(get_rag_service)):
    try:
        async with asyncio.timeout(30):
            return await service.answer(request, ctx)
    except asyncio.TimeoutError:
        raise ProviderError("request exceeded 30s budget")
```

## 12. Cancellation-aware fake provider (for tests)

```python
import asyncio


class SlowFakeLlm:
    def __init__(self) -> None:
        self.was_cancelled = False

    async def complete(self, **kwargs):
        try:
            await asyncio.sleep(10)
            return LlmResult(text="ok", input_tokens=0, output_tokens=0, model="fake")
        except asyncio.CancelledError:
            self.was_cancelled = True
            raise
```

Use it in a test that disconnects the client mid-stream and asserts
`fake.was_cancelled is True`.
