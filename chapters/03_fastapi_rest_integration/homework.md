# Homework: FastAPI, REST, and Integration

Graded against `../../syllabus/evaluation_rubric.md`. Put outputs under `my_work/`.

## Required

1. **Expose the chapter 01 service.** Wire your `RagService` behind FastAPI
   routes: `POST /ask`, `POST /documents`, `POST /feedback`, `GET /jobs/{id}`,
   `GET /healthz`. Every protected route uses the `request_context`
   dependency.

2. **Error contract.** Implement the unified exception handler so every
   non-2xx response carries `{error: {code, message, retryable, request_id}}`.
   Cover at least: validation error (422), auth error (403),
   no-relevant-context (422), provider error (503), rate limited (429).

3. **OpenAPI snapshot test.** Commit `tests/contract/openapi_snapshot.json`
   and a CI test that fails on drift. Document in your README how to update
   the snapshot intentionally.

4. **Streaming endpoint.** Implement `POST /ask/stream` emitting SSE events
   `session`, `token`, `citation`, `error`, `done` per `lesson.md` section 6.
   Include a 15 s heartbeat. Write a client snippet (curl or httpx) in
   `my_work/streaming_client.md` showing how to consume it.

5. **Idempotent ingestion.** `POST /documents` accepts `Idempotency-Key`;
   re-submitting with the same key + tenant returns the same `job_id` (202).
   Add a contract test that proves it.

6. **Contract tests.** Cover at minimum:
   - happy `/ask` happy path
   - missing required field → 422 with `code=validation_error`
   - missing/invalid token → 401
   - tenant mismatch on `/jobs/{id}` → 403
   - provider raises → 503 with `retryable=true`
   - idempotency replay returns same `job_id`

## Stretch

7. **Rate limiting.** Add per-tenant token-bucket rate limiting on `/ask`
   using Redis (or a memory backend for now). Return 429 with `Retry-After`.
   Test that bursts are absorbed and sustained excess is rejected.

8. **API versioning rehearsal.** Mount the existing router under `/v1`. Add
   a `/v2/ask` with one breaking schema change (e.g. `query` instead of
   `question`). Both versions must work concurrently; the v1 snapshot test
   must still pass.

9. **Cancellation discipline.** Write a test that simulates a client
   disconnect mid-stream and asserts the service-side LLM call was
   cancelled (use a fake provider with an `await asyncio.sleep` plus a
   `was_cancelled` flag).

## Acceptance

- `httpie` calls in your README work against a locally running app.
- OpenAPI snapshot test passes on a clean clone; an intentional change to
  one field causes it to fail with a useful diff.
- Streaming endpoint produces the documented event sequence under happy
  path and under an injected guardrail failure.
- Idempotency replay returns the same `job_id` for at least 3 distinct
  test cases.
