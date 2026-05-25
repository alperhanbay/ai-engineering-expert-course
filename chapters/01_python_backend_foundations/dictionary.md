# Dictionary: Python Backend Foundations

Use this dictionary at the end of the chapter. Add your own examples in `my_work/dictionary_notes.md`.

| Term | Working Definition | Why It Matters | Common Failure Mode | Mastery Check |
| --- | --- | --- | --- | --- |
| `package layout` | The directory and module organization of a Python application. | A clean layout separates routes, services, repositories, providers, models, and tests. | All logic lives in one script, making provider changes and tests difficult. | Show where API, service, provider, and persistence code live in your capstone. |
| `type hints` | Python annotations that document expected input and output types. | They make contracts visible and improve editor, static analysis, and review quality. | A retriever returns inconsistent objects and downstream generation fails late. | Annotate service/provider interfaces and run type-aware reviews. |
| `Pydantic` | A Python data validation library commonly used for typed models and API schemas. | It validates request/response shapes and helps enforce structured contracts. | Invalid tool arguments reach a provider because input was only informally checked. | Use Pydantic models for API requests, responses, config, and tool schemas. |
| `service layer` | The application layer that owns business logic independent of HTTP routes. | It keeps core AI behavior testable without running the web framework. | The RAG pipeline is embedded inside a route handler and cannot be unit tested. | Call the RAG service from both API tests and direct service tests. |
| `repository` | A component that hides persistence details behind a stable interface. | It lets SQL storage change without rewriting business logic. | SQL queries are scattered across agent, API, and evaluation code. | Implement document, feedback, and audit repositories with explicit methods. |
| `provider adapter` | A wrapper that isolates external providers such as LLMs, embedding APIs, or vector stores. | It reduces vendor lock-in and makes testing with fakes possible. | OpenAI-specific response parsing is hardcoded inside the RAG service. | Define provider protocols and replace real providers with fakes in tests. |
| `async I/O` | Concurrent waiting for network or file operations without blocking the event loop. | LLM, vector DB, SQL, and tool calls are often network-bound. | A slow provider call blocks unrelated requests in the API service. | Use async boundaries where I/O dominates and measure behavior under concurrent load. |
| `structured logging` | Machine-readable logs with consistent event names and fields. | It enables tracing, debugging, analytics, incident response, and audit workflows. | Logs contain plain text messages with no request ID or version metadata. | Log request ID, tenant, model, prompt, index, latency, and error type. |

## Dictionary Assignment

For each term:

1. Write a one-sentence definition in your own words.
2. Write a concrete example from your capstone (or planned capstone).
3. Write one failure mode you would test against.
4. Write one metric, test, or review check that would catch the failure.
5. Link one source from `references_numbered.md`.

## References

[1] Python typing: https://docs.python.org/3/library/typing.html
[2] Python logging: https://docs.python.org/3/library/logging.html
[3] Pydantic documentation: https://docs.pydantic.dev/
[4] pytest documentation: https://docs.pytest.org/
[5] FastAPI documentation: https://fastapi.tiangolo.com/
