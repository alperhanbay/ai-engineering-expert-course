# Expanded Question Bank: Python Backend Foundations

## How To Use This Bank

Answer without looking at the answer key. For every wrong answer, write one sentence explaining the concept in your own words and one sentence explaining how it appears in a production AI system.


## Multiple Choice

1. Pick the description of `package layout` you would put in a `dictionary.md` entry.
   - A. The application layer that owns business logic independent of HTTP routes.
   - B. The directory and module organization of a Python application.
   - C. Python annotations that document expected input and output types.
   - D. A Python data validation library commonly used for typed models and API schemas.

2. Which sentence is the best working definition of `type hints`?
   - A. Python annotations that document expected input and output types.
   - B. The directory and module organization of a Python application.
   - C. A Python data validation library commonly used for typed models and API schemas.
   - D. The application layer that owns business logic independent of HTTP routes.

3. In production AI work, what is the primary role of `Pydantic`?
   - A. The directory and module organization of a Python application.
   - B. Python annotations that document expected input and output types.
   - C. The application layer that owns business logic independent of HTTP routes.
   - D. A Python data validation library commonly used for typed models and API schemas.

4. A teammate asks you to define `service layer` in one sentence. Which is closest?
   - A. Python annotations that document expected input and output types.
   - B. A Python data validation library commonly used for typed models and API schemas.
   - C. The application layer that owns business logic independent of HTTP routes.
   - D. The directory and module organization of a Python application.

5. Pick the description of `repository` you would put in a `dictionary.md` entry.
   - A. A Python data validation library commonly used for typed models and API schemas.
   - B. A component that hides persistence details behind a stable interface.
   - C. The directory and module organization of a Python application.
   - D. Python annotations that document expected input and output types.

6. Which sentence is the best working definition of `provider adapter`?
   - A. A wrapper that isolates external providers such as LLMs, embedding APIs, or vector stores.
   - B. The directory and module organization of a Python application.
   - C. Python annotations that document expected input and output types.
   - D. A Python data validation library commonly used for typed models and API schemas.

7. In production AI work, what is the primary role of `async I/O`?
   - A. The directory and module organization of a Python application.
   - B. Python annotations that document expected input and output types.
   - C. A Python data validation library commonly used for typed models and API schemas.
   - D. Concurrent waiting for network or file operations without blocking the event loop.

8. A teammate asks you to define `structured logging` in one sentence. Which is closest?
   - A. Python annotations that document expected input and output types.
   - B. A Python data validation library commonly used for typed models and API schemas.
   - C. Machine-readable logs with consistent event names and fields.
   - D. The directory and module organization of a Python application.


## Applied Multiple Choice

1. Applied case: Model provider logic often leaks into routes and makes systems hard to test.
   - A. Skip the rollback plan; staging is close enough to production.
   - B. Hard-code the new behaviour for the first failing case and call it a fix.
   - C. Ship the change without measurement because the most recent demo looked good.
   - D. Set up a controlled experiment isolating `package layout`, capture before/after numbers, and write the result to a decision record.

2. Applied case: Untyped request and response objects make downstream failures harder to debug.
   - A. Ship the change without measurement because the most recent demo looked good.
   - B. Remove logging and evaluation to keep the diff small and merge faster.
   - C. Add the work to the capstone as a reviewable artifact that exercises `type hints` end-to-end, with tests and a trace.
   - D. Hard-code the new behaviour for the first failing case and call it a fix.

3. Applied case: Notebook prototypes usually lack error contracts, dependency boundaries, and logs.
   - A. Assume the largest available model will mask the underlying weakness in `package layout` so no system change is needed.
   - B. Define explicit acceptance criteria, rollback steps, and a reviewer checklist tied to Python Backend Foundations.
   - C. Ship the change without measurement because the most recent demo looked good.
   - D. Remove logging and evaluation to keep the diff small and merge faster.

4. Applied case: Build a typed AI service skeleton with fake LLM, fake retriever, and tests.
   - A. Compare at least two approaches against a labelled set covering `structured logging`, then choose on measured quality, latency, cost, and risk.
   - B. Remove logging and evaluation to keep the diff small and merge faster.
   - C. Assume the largest available model will mask the underlying weakness in `package layout` so no system change is needed.
   - D. Skip the rollback plan; staging is close enough to production.

5. Applied case: Create a provider adapter interface for LLM, embedding, and vector store calls.
   - A. Assume the largest available model will mask the underlying weakness in `package layout` so no system change is needed.
   - B. Skip the rollback plan; staging is close enough to production.
   - C. Hard-code the new behaviour for the first failing case and call it a fix.
   - D. Write a one-page design memo naming the assumption, the test that would falsify it, and the metric you'd watch in production.

6. Applied case: Implement structured logging with request IDs and model/prompt/index metadata.
   - A. Hard-code the new behaviour for the first failing case and call it a fix.
   - B. Ship the change without measurement because the most recent demo looked good.
   - C. Set up a controlled experiment isolating `package layout`, capture before/after numbers, and write the result to a decision record.
   - D. Skip the rollback plan; staging is close enough to production.


## Fill In The Blanks

1. ________ is best summarised as: The directory and module organization of a Python application. Verification step: Show where API, service, provider, and persistence code live in your capstone.
2. On a system review, you find a retriever returns inconsistent objects and downstream generation fails late — the underlying chapter concept is ________.
3. It validates request/response shapes and helps enforce structured contracts. A common failure looks like: Invalid tool arguments reach a provider because input was only informally checked. The concept is ________.
4. Given the production failure "The RAG pipeline is embedded inside a route handler and cannot be unit tested.", the concept being misused is ________.
5. To handle situations where it lets SQL storage change without rewriting business logic, the engineering tool you reach for is ________ (watch for: SQL queries are scattered across agent, API, and evaluation code.).
6. ________ is best summarised as: A wrapper that isolates external providers such as LLMs, embedding APIs, or vector stores. Verification step: Define provider protocols and replace real providers with fakes in tests.
7. On a system review, you find a slow provider call blocks unrelated requests in the API service — the underlying chapter concept is ________.
8. It enables tracing, debugging, analytics, incident response, and audit workflows. A common failure looks like: Logs contain plain text messages with no request ID or version metadata. The concept is ________.

## Short Answer

1. When would you intentionally *avoid* using `package layout`? Name a constraint or tradeoff.
2. What does a healthy log or trace look like for `type hints`? List the fields you would expect.
3. Explain how `Pydantic` appears in the capstone, what artifact proves it, and what failure mode you would test.
4. If a reviewer asks 'why does `service layer` matter here?', what one-paragraph answer do you give? Include a metric.
5. Describe the smallest experiment that would tell you whether `repository` is correctly implemented in your system.
6. When would you intentionally *avoid* using `provider adapter`? Name a constraint or tradeoff.
7. What does a healthy log or trace look like for `async I/O`? List the fields you would expect.
8. Explain how `structured logging` appears in the capstone, what artifact proves it, and what failure mode you would test.

## Scenario Questions

1. On-call triage: Model provider logic often leaks into routes and makes systems hard to test. Walk through the first three steps you would take.
2. Incident: Untyped request and response objects make downstream failures harder to debug. What do you inspect first, and which metric would prove the fix?
3. Design review: Notebook prototypes usually lack error contracts, dependency boundaries, and logs. Which artifact would you require before approving?
4. A teammate proposes a major change to `async I/O` with no experiment. Which artifact do you ask for before approving?

## Practical Debug Questions

1. What log or trace fields would help you debug a failure in `package layout` in this chapter's context?
2. What single metric would you watch in production when changing `repository`?
3. You suspect `structured logging` is degraded. Design the smallest experiment that would falsify or confirm it in under an hour.
4. For the failure 'Model provider logic often leaks into routes and makes systems hard to test.', sketch a rollback plan with a clear restore-point definition.
5. What artifact would you put in a portfolio README to prove competence with `package layout`, `type hints`, `Pydantic`?

## Answer Key

### Multiple Choice

1. B
2. A
3. D
4. C
5. B
6. A
7. D
8. C

### Applied Multiple Choice

1. D
2. C
3. B
4. A
5. D
6. C

### Fill In The Blanks

1. package layout
2. type hints
3. Pydantic
4. service layer
5. repository
6. provider adapter
7. async I/O
8. structured logging

Short-answer, scenario, and debug questions should be graded against the rubric in `../../syllabus/evaluation_rubric.md`.

## References

[1] Python typing: https://docs.python.org/3/library/typing.html
[2] Python logging: https://docs.python.org/3/library/logging.html
[3] Pydantic documentation: https://docs.pydantic.dev/
[4] pytest documentation: https://docs.pytest.org/
[5] FastAPI documentation: https://fastapi.tiangolo.com/
