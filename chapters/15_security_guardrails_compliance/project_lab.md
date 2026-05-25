# Project Lab: Security, Guardrails, and Compliance

Safe AI systems use layered controls across input, retrieval, generation, tools, logs, and human review. This lab turns the chapter's projects into concrete, reviewable
deliverables. Pick one project and finish it end-to-end before starting another.
The "Acceptance Criteria" sections are the gate — not the existence of files.

## Project 1: Build a threat model for the capstone with assets, actors, trust boundaries, threats, and controls.

### Scenario

A compliance reviewer is about to audit your capstone. You need a threat model, a guardrail test suite covering OWASP LLM Top 10, audit logs across every sensitive surface, and a PII handling policy that holds up under inspection.

### Inputs

- capstone architecture diagram (API, retrieval, generation, tools, storage, traces)
- data inventory: which fields are PII, where they appear (prompts, logs, embeddings, evals)
- OWASP Top 10 for LLM Applications (2025 release) as the threat reference

### Outputs / Artifacts

- `threat_model.md` — assets, actors, trust boundaries, threats, mitigations, residual risk
- `guardrail_tests/` — at least 50 cases across injection, PII, authorization, unsafe tools
- `audit_log_schema.md` — fields for document access, retrieval, generation, tool calls, blocks, approvals
- `pii_policy.md` — handling rules per data surface (prompt, log, embedding, eval, backup)

### Test Cases

- direct prompt injection in user input
- indirect prompt injection via retrieved document
- cross-tenant retrieval attempt (filter bypass)
- tool call that would exceed user's RBAC role
- PII echoed in model output despite redaction layer
- log entry containing unmasked secret or API key

### Metrics

- % of guardrail tests that pass (target 100% on high-risk classes)
- % of audit-required actions with a complete log entry
- time to detect and revoke a leaked-credential scenario in a tabletop exercise

### Failure Cases To Cover

- Guardrails live only in the system prompt — model can be talked around them
- Cache key omits tenant id, leaking responses across tenants
- Embeddings retain PII even after the source document is deleted
- Audit log is best-effort and silently drops entries under load

### Acceptance Criteria

- every OWASP LLM Top 10 category has at least one mapped guardrail test
- the PII policy names a control per data surface — none are 'TBD'
- the threat model lists residual risks explicitly with owners

### Deliverables Layout

```
my_work/
  project_1_scope.md            # one paragraph + concept list
  project_1_implementation/      # code or design doc
  project_1_report.md            # results, numbers, plots
  project_1_decision_record.md   # alternatives + chosen approach + why
  project_1_tests/               # the test cases above, runnable or scripted
```

### Expected README Section

In your portfolio README, this project should appear under "Projects" with:
a one-sentence summary, the headline metric you measured, the main tradeoff
you made, and a link to the decision record. Avoid screenshots-only entries.

## Project 2: Create a 50-case guardrail test suite for prompt injection, PII, authorization, and unsafe tools.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `prompt injection`, `PII`, `RBAC`, `ABAC`, `audit log`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `prompt injection`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_2_implementation/`
- `my_work/project_2_report.md` summarising results with numbers
- `my_work/project_2_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `prompt injection`
- an edge case driven by the failure mode of `PII`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `prompt injection` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Guardrails fail when they are only prompts and not system controls.
- RAG and agents expand the attack surface through retrieved context and tool output.
- Logs, traces, embeddings, and eval datasets can all contain sensitive data.
- silent degradation of `threat model` after a config change goes unnoticed

### Acceptance Criteria

- a reviewer can run or read the artifact and understand what was built without asking you
- every numeric claim is backed by a test, eval result, or measured run logged in the report
- at least one known limitation is named honestly (not a humblebrag)
- the artifact is wired into the capstone, not orphaned in `my_work/`

### Deliverables Layout

```
my_work/
  project_2_scope.md            # one paragraph + concept list
  project_2_implementation/      # code or design doc
  project_2_report.md            # results, numbers, plots
  project_2_decision_record.md   # alternatives + chosen approach + why
  project_2_tests/               # the test cases above, runnable or scripted
```

### Expected README Section

In your portfolio README, this project should appear under "Projects" with:
a one-sentence summary, the headline metric you measured, the main tradeoff
you made, and a link to the decision record. Avoid screenshots-only entries.

## Project 3: Design audit logs for document access, retrieval, answer generation, tool calls, blocks, and approvals.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `prompt injection`, `PII`, `RBAC`, `ABAC`, `audit log`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `prompt injection`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_3_implementation/`
- `my_work/project_3_report.md` summarising results with numbers
- `my_work/project_3_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `prompt injection`
- an edge case driven by the failure mode of `PII`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `prompt injection` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Guardrails fail when they are only prompts and not system controls.
- RAG and agents expand the attack surface through retrieved context and tool output.
- Logs, traces, embeddings, and eval datasets can all contain sensitive data.
- silent degradation of `threat model` after a config change goes unnoticed

### Acceptance Criteria

- a reviewer can run or read the artifact and understand what was built without asking you
- every numeric claim is backed by a test, eval result, or measured run logged in the report
- at least one known limitation is named honestly (not a humblebrag)
- the artifact is wired into the capstone, not orphaned in `my_work/`

### Deliverables Layout

```
my_work/
  project_3_scope.md            # one paragraph + concept list
  project_3_implementation/      # code or design doc
  project_3_report.md            # results, numbers, plots
  project_3_decision_record.md   # alternatives + chosen approach + why
  project_3_tests/               # the test cases above, runnable or scripted
```

### Expected README Section

In your portfolio README, this project should appear under "Projects" with:
a one-sentence summary, the headline metric you measured, the main tradeoff
you made, and a link to the decision record. Avoid screenshots-only entries.

## Review Rubric

| Dimension | Evidence that passes |
| --- | --- |
| Specificity | scenario, inputs, and outputs match what the artifact actually does |
| Measurement | metrics are numeric, named, and reproducible from the repo |
| Failure handling | at least three failure cases are exercised in tests |
| Tradeoff honesty | decision record names alternatives and a measured reason |
| Source backing | numbered references support every external claim |

## References

[1] OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
[2] OWASP LLM Top 10 2025 PDF: https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf
[3] NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
[4] Microsoft Responsible AI: https://www.microsoft.com/en-us/ai/principles-and-approach/
[5] Azure OpenAI responsible AI: https://learn.microsoft.com/en-us/legal/cognitive-services/openai/overview
