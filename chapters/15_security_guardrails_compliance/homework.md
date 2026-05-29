# Homework: Security, Guardrails, and Compliance

Graded against `../../syllabus/evaluation_rubric.md`. Outputs under `my_work/`.

## Required

1. **Threat model.** Write `my_work/threat_model.md` with assets, actors, trust
   boundaries, threats (each mapped to an OWASP LLM Top 10 category), controls,
   and explicitly named residual risks with owners.

2. **Guardrail test suite.** Build `my_work/guardrail_tests/` with ≥50 cases:
   direct prompt injection, indirect (via retrieved doc), tool-output
   injection, PII in output, cross-tenant access attempt, RBAC-exceeding tool
   call. Each has expected safe behaviour. Wire as pytest; document your honest
   pass rate.

3. **OWASP mapping.** Write `my_work/owasp_mapping.md` mapping each of the 10
   categories to at least one concrete control in your system. Flag any
   category with no control as a gap.

4. **Audit log schema.** Write `my_work/audit_log_schema.md`: fields plus the
   list of sensitive actions that must produce an entry. Show it's append-only
   (app role has INSERT/SELECT only).

5. **PII policy.** Write `my_work/pii_policy.md` with a control per data surface
   (prompt, log, trace, embedding, eval, cache, backup), retention per surface,
   and how a deletion request propagates to all of them. No "TBD" entries.

6. **Code-enforced permission proof.** Demonstrate that an unauthorized tool
   call is blocked by a code check even when the prompt is manipulated to
   request it (i.e. the block does not rely on the model behaving).

## Stretch

7. **Red-team session.** Spend an hour trying to break your own system
   (inject, escalate, leak). Turn every success into a new guardrail test.
   Document in `my_work/redteam.md`.

8. **Streaming guardrail.** Prove your streaming endpoint blocks unsafe content
   *before* the user sees it (delay or per-chunk check).

9. **Deletion propagation test.** Delete a document and verify it's gone from
   the DB, the vector store, the cache, and that logs are redacted per policy.

## Acceptance

- Every OWASP LLM Top 10 category maps to at least one control.
- The unauthorized-tool-call block works even with a manipulated prompt.
- The PII policy names a control for every data surface.
- The guardrail suite runs in CI and the pass rate is reported honestly.
