# Homework: Python Backend Foundations

Graded against `../../syllabus/evaluation_rubric.md`. Outputs under `my_work/`.

## Required

1. **Package skeleton.** Build the layered layout from `lesson.md` section 2
   (`api/`, `core/`, `models/`, `services/`, `repositories/`, `providers/`).
   It must be importable: `python -c "import <pkg>"` succeeds.

2. **Config via pydantic-settings.** Implement `core/config.py` reading from
   env vars with `extra="forbid"`. Commit a `.env.example` with every variable.
   Show that a misspelled env var fails at startup, not at request time.

3. **Pydantic schemas.** Define `AskRequest`, `AskResponse`, `Citation` with
   validation (length limits, bounded score). Add a test that invalid input
   raises.

4. **Service layer + provider Protocols.** Implement `RagService.answer` with
   constructor-injected `Retriever`, `Generator`, `AuditRepository` Protocols.
   Provide fake implementations under `tests/fakes/`.

5. **Error hierarchy.** Implement `core/errors.py` (validation, authorization,
   no-context, provider, unsafe) each with `error_code`, `user_message`,
   `retryable`.

6. **Structured logging.** Configure JSON logs carrying `request_id`,
   `tenant_id`, `model_id`, `prompt_version`, `latency_ms`. Add a
   `redact_for_log` helper and a test that it strips a fake API key.

7. **Test suite (no network).** Cover: schema validation, service happy path,
   no-answer path (audited), provider-error mapping, request-id propagation.
   Target: 100% pass, under 5 seconds, zero network calls.

## Stretch

8. **Composition root.** Implement `api/dependencies.py` as the single place
   concrete providers are wired. Show swapping `llm_provider` is a config-only
   change.

9. **Performance baseline.** Run the fake-only stack under load (`hey`/`oha`)
   and record p50/p95 and throughput in `my_work/baseline.md`. Investigate if
   p95 against fakes exceeds ~20ms.

10. **mypy clean.** Get `mypy` (or pyright) clean on the public service
    interface; add it as a CI step.

## Acceptance

- The service runs in tests with no network call.
- Swapping a provider is config, not code.
- Structured logs include the required fields; the redaction test passes.
- A teammate can extend the skeleton without asking you (README lists files).
