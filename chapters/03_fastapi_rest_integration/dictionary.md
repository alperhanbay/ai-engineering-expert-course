# Dictionary: FastAPI, REST, and Integration

Use this dictionary at the end of the chapter. Add your own examples in `my_work/dictionary_notes.md`.

| Term | Working Definition | Why It Matters | Common Failure Mode | Mastery Check |
| --- | --- | --- | --- | --- |
| `REST` | An API style using resources, HTTP methods, status codes, and representations. | REST contracts let product systems call AI capabilities predictably. | The API exposes internal provider-specific objects as public responses. | Design stable endpoints for ingestion, ask, feedback, eval, and agent runs. |
| `OpenAPI` | A machine-readable specification for HTTP APIs. | It makes AI API contracts inspectable, testable, and shareable. | Frontend and backend disagree on the RAG response shape. | Generate and review OpenAPI schemas for all public endpoints. |
| `request schema` | The validated structure expected from an API client. | It prevents malformed or unsafe inputs from reaching expensive AI calls. | A missing tenant ID lets retrieval run without access filters. | Define required fields, validation rules, and examples. |
| `response schema` | The validated structure returned by an API. | It protects downstream clients from unparseable or incomplete model outputs. | The API sometimes returns text and sometimes JSON for the same endpoint. | Return typed responses with answer, citations, flags, versions, and request ID. |
| `error contract` | A consistent format for returning errors and failure details. | It helps clients and operators distinguish validation, authorization, provider, and safety failures. | Every error becomes HTTP 500 and cannot be triaged. | Define status codes, error codes, user message, retryability, and trace ID. |
| `streaming` | Sending partial model output to the client as it is generated. | It improves perceived latency but complicates safety, citations, and validation. | Unsafe text is streamed before guardrails run. | Design streaming boundaries and specify how citations and errors are emitted. |
| `background job` | A long-running task executed outside the immediate HTTP request. | Indexing, parsing, embedding, and evaluations often exceed request timeouts. | A document upload blocks until all embeddings complete and times out. | Create job states, retry behavior, idempotency, and status endpoints. |
| `idempotency` | The property that repeating a request does not create unintended duplicate side effects. | Retries are normal in distributed AI systems. | A client retry creates duplicate ingestion jobs and duplicate vectors. | Use idempotency keys for document ingestion and tool actions. |

<!-- HAND-AUTHORED: do not regenerate -->
## Extended Glossary

Additional terms used in this chapter, each with a concise definition and an authoritative source.

- **REST** — an API style using resources, HTTP methods, and status codes. Source: [restfulapi.net](https://restfulapi.net/)
- **OpenAPI** — a machine-readable specification of an HTTP API. Source: [OpenAPI Spec](https://spec.openapis.org/oas/latest.html)
- **ASGI / Starlette** — the async interface and toolkit FastAPI is built on. Source: [Starlette](https://www.starlette.io/)
- **Dependency injection (FastAPI)** — `Depends(...)` providing auth/context/services to routes. Source: [FastAPI dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
- **Server-Sent Events (SSE)** — one-way streaming of events over HTTP. Source: [MDN SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)
- **CORS** — browser cross-origin access control. Source: [MDN CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
- **JWT** — a signed token carrying identity claims. Source: [jwt.io introduction](https://jwt.io/introduction)
- **Idempotency key** — header making a retried write safe. Source: [Stripe idempotency](https://docs.stripe.com/api/idempotent_requests)
- **HTTP status codes** — standardized response codes (422, 429, 503, ...). Source: [MDN status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- **response_model (FastAPI)** — declares + validates the response shape. Source: [FastAPI response model](https://fastapi.tiangolo.com/tutorial/response-model/)
- **Rate limiting** — bounding request rate per client/tenant. Source: [MDN 429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429)

## Dictionary Assignment

For each term:

1. Write a one-sentence definition in your own words.
2. Write a concrete example from your capstone (or planned capstone).
3. Write one failure mode you would test against.
4. Write one metric, test, or review check that would catch the failure.
5. Link one source from `references_numbered.md`.

## References

[1] FastAPI first steps: https://fastapi.tiangolo.com/tutorial/first-steps/
[2] FastAPI request body: https://fastapi.tiangolo.com/tutorial/body/
[3] FastAPI error handling: https://fastapi.tiangolo.com/tutorial/handling-errors/
[4] FastAPI testing: https://fastapi.tiangolo.com/tutorial/testing/
[5] OpenAPI Specification: https://spec.openapis.org/oas/latest.html
