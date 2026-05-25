# Expanded Question Bank: FastAPI, REST, and Integration

## How To Use This Bank

Answer without looking at the answer key. For every wrong answer, write one sentence explaining the concept in your own words and one sentence explaining how it appears in a production AI system.


## Multiple Choice

1. Pick the description of `REST` you would put in a `dictionary.md` entry.
   - A. The validated structure returned by an API.
   - B. An API style using resources, HTTP methods, status codes, and representations.
   - C. A machine-readable specification for HTTP APIs.
   - D. The validated structure expected from an API client.

2. Which sentence is the best working definition of `OpenAPI`?
   - A. A machine-readable specification for HTTP APIs.
   - B. An API style using resources, HTTP methods, status codes, and representations.
   - C. The validated structure expected from an API client.
   - D. The validated structure returned by an API.

3. In production AI work, what is the primary role of `request schema`?
   - A. An API style using resources, HTTP methods, status codes, and representations.
   - B. A machine-readable specification for HTTP APIs.
   - C. The validated structure returned by an API.
   - D. The validated structure expected from an API client.

4. A teammate asks you to define `response schema` in one sentence. Which is closest?
   - A. A machine-readable specification for HTTP APIs.
   - B. The validated structure expected from an API client.
   - C. The validated structure returned by an API.
   - D. An API style using resources, HTTP methods, status codes, and representations.

5. Pick the description of `error contract` you would put in a `dictionary.md` entry.
   - A. The validated structure expected from an API client.
   - B. A consistent format for returning errors and failure details.
   - C. An API style using resources, HTTP methods, status codes, and representations.
   - D. A machine-readable specification for HTTP APIs.

6. Which sentence is the best working definition of `streaming`?
   - A. Sending partial model output to the client as it is generated.
   - B. An API style using resources, HTTP methods, status codes, and representations.
   - C. A machine-readable specification for HTTP APIs.
   - D. The validated structure expected from an API client.

7. In production AI work, what is the primary role of `background job`?
   - A. An API style using resources, HTTP methods, status codes, and representations.
   - B. A machine-readable specification for HTTP APIs.
   - C. The validated structure expected from an API client.
   - D. A long-running task executed outside the immediate HTTP request.

8. A teammate asks you to define `idempotency` in one sentence. Which is closest?
   - A. A machine-readable specification for HTTP APIs.
   - B. The validated structure expected from an API client.
   - C. The property that repeating a request does not create unintended duplicate side effects.
   - D. An API style using resources, HTTP methods, status codes, and representations.


## Applied Multiple Choice

1. Applied case: AI endpoints often hide all failures behind HTTP 500.
   - A. Skip the rollback plan; staging is close enough to production.
   - B. Hard-code the new behaviour for the first failing case and call it a fix.
   - C. Ship the change without measurement because the most recent demo looked good.
   - D. Set up a controlled experiment isolating `REST`, capture before/after numbers, and write the result to a decision record.

2. Applied case: Long document indexing jobs do not fit a single synchronous request.
   - A. Ship the change without measurement because the most recent demo looked good.
   - B. Remove logging and evaluation to keep the diff small and merge faster.
   - C. Add the work to the capstone as a reviewable artifact that exercises `OpenAPI` end-to-end, with tests and a trace.
   - D. Hard-code the new behaviour for the first failing case and call it a fix.

3. Applied case: Clients should not depend on a specific model, vector database, or orchestration framework.
   - A. Assume the largest available model will mask the underlying weakness in `REST` so no system change is needed.
   - B. Define explicit acceptance criteria, rollback steps, and a reviewer checklist tied to FastAPI, REST, and Integration.
   - C. Ship the change without measurement because the most recent demo looked good.
   - D. Remove logging and evaluation to keep the diff small and merge faster.

4. Applied case: Build an AI API with document ingestion, ask, feedback, eval, and agent endpoints.
   - A. Compare at least two approaches against a labelled set covering `idempotency`, then choose on measured quality, latency, cost, and risk.
   - B. Remove logging and evaluation to keep the diff small and merge faster.
   - C. Assume the largest available model will mask the underlying weakness in `REST` so no system change is needed.
   - D. Skip the rollback plan; staging is close enough to production.

5. Applied case: Design a streaming answer endpoint and document citation handling for partial output.
   - A. Assume the largest available model will mask the underlying weakness in `REST` so no system change is needed.
   - B. Skip the rollback plan; staging is close enough to production.
   - C. Hard-code the new behaviour for the first failing case and call it a fix.
   - D. Write a one-page design memo naming the assumption, the test that would falsify it, and the metric you'd watch in production.

6. Applied case: Create a background indexing job API with job states and failure recovery.
   - A. Hard-code the new behaviour for the first failing case and call it a fix.
   - B. Ship the change without measurement because the most recent demo looked good.
   - C. Set up a controlled experiment isolating `REST`, capture before/after numbers, and write the result to a decision record.
   - D. Skip the rollback plan; staging is close enough to production.


## Fill In The Blanks

1. ________ is best summarised as: An API style using resources, HTTP methods, status codes, and representations. Verification step: Design stable endpoints for ingestion, ask, feedback, eval, and agent runs.
2. On a system review, you find frontend and backend disagree on the RAG response shape — the underlying chapter concept is ________.
3. It prevents malformed or unsafe inputs from reaching expensive AI calls. A common failure looks like: A missing tenant ID lets retrieval run without access filters. The concept is ________.
4. Given the production failure "The API sometimes returns text and sometimes JSON for the same endpoint.", the concept being misused is ________.
5. To handle situations where it helps clients and operators distinguish validation, authorization, provider, and safety failures, the engineering tool you reach for is ________ (watch for: Every error becomes HTTP 500 and cannot be triaged.).
6. ________ is best summarised as: Sending partial model output to the client as it is generated. Verification step: Design streaming boundaries and specify how citations and errors are emitted.
7. On a system review, you find a document upload blocks until all embeddings complete and times out — the underlying chapter concept is ________.
8. Retries are normal in distributed AI systems. A common failure looks like: A client retry creates duplicate ingestion jobs and duplicate vectors. The concept is ________.

## Short Answer

1. When would you intentionally *avoid* using `REST`? Name a constraint or tradeoff.
2. What does a healthy log or trace look like for `OpenAPI`? List the fields you would expect.
3. Explain how `request schema` appears in the capstone, what artifact proves it, and what failure mode you would test.
4. If a reviewer asks 'why does `response schema` matter here?', what one-paragraph answer do you give? Include a metric.
5. Describe the smallest experiment that would tell you whether `error contract` is correctly implemented in your system.
6. When would you intentionally *avoid* using `streaming`? Name a constraint or tradeoff.
7. What does a healthy log or trace look like for `background job`? List the fields you would expect.
8. Explain how `idempotency` appears in the capstone, what artifact proves it, and what failure mode you would test.

## Scenario Questions

1. On-call triage: AI endpoints often hide all failures behind HTTP 500. Walk through the first three steps you would take.
2. Incident: Long document indexing jobs do not fit a single synchronous request. What do you inspect first, and which metric would prove the fix?
3. Design review: Clients should not depend on a specific model, vector database, or orchestration framework. Which artifact would you require before approving?
4. A pull request modifies `background job` and a downstream quality metric drops. What rollback, evaluation, and documentation do you require before merge?

## Practical Debug Questions

1. What log or trace fields would help you debug a failure in `REST` in this chapter's context?
2. What single metric would you watch in production when changing `error contract`?
3. You suspect `idempotency` is degraded. Design the smallest experiment that would falsify or confirm it in under an hour.
4. For the failure 'AI endpoints often hide all failures behind HTTP 500.', sketch a rollback plan with a clear restore-point definition.
5. What artifact would you put in a portfolio README to prove competence with `REST`, `OpenAPI`, `request schema`?

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

1. REST
2. OpenAPI
3. request schema
4. response schema
5. error contract
6. streaming
7. background job
8. idempotency

Short-answer, scenario, and debug questions should be graded against the rubric in `../../syllabus/evaluation_rubric.md`.

## References

[1] FastAPI first steps: https://fastapi.tiangolo.com/tutorial/first-steps/
[2] FastAPI request body: https://fastapi.tiangolo.com/tutorial/body/
[3] FastAPI error handling: https://fastapi.tiangolo.com/tutorial/handling-errors/
[4] FastAPI testing: https://fastapi.tiangolo.com/tutorial/testing/
[5] OpenAPI Specification: https://spec.openapis.org/oas/latest.html
