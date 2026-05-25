# Expanded Question Bank: Security, Guardrails, and Compliance

## How To Use This Bank

Answer without looking at the answer key. For every wrong answer, write one sentence explaining the concept in your own words and one sentence explaining how it appears in a production AI system.


## Multiple Choice

1. In production AI work, what is the primary role of `prompt injection`?
   - A. Personally identifiable information.
   - B. Role-based access control.
   - C. Attribute-based access control.
   - D. An attack or failure where untrusted text attempts to override trusted instructions.

2. A teammate asks you to define `PII` in one sentence. Which is closest?
   - A. Role-based access control.
   - B. Attribute-based access control.
   - C. Personally identifiable information.
   - D. An attack or failure where untrusted text attempts to override trusted instructions.

3. Pick the description of `RBAC` you would put in a `dictionary.md` entry.
   - A. Attribute-based access control.
   - B. Role-based access control.
   - C. An attack or failure where untrusted text attempts to override trusted instructions.
   - D. Personally identifiable information.

4. Which sentence is the best working definition of `ABAC`?
   - A. Attribute-based access control.
   - B. An attack or failure where untrusted text attempts to override trusted instructions.
   - C. Personally identifiable information.
   - D. Role-based access control.

5. In production AI work, what is the primary role of `audit log`?
   - A. An attack or failure where untrusted text attempts to override trusted instructions.
   - B. Personally identifiable information.
   - C. Role-based access control.
   - D. A compliance-oriented record of who accessed or changed what, when, why, and through which system.

6. A teammate asks you to define `guardrail` in one sentence. Which is closest?
   - A. Personally identifiable information.
   - B. Role-based access control.
   - C. A system control that prevents or detects unsafe inputs, outputs, or actions.
   - D. An attack or failure where untrusted text attempts to override trusted instructions.

7. Pick the description of `tenant isolation` you would put in a `dictionary.md` entry.
   - A. Role-based access control.
   - B. Separating data and access between organizations or user groups.
   - C. An attack or failure where untrusted text attempts to override trusted instructions.
   - D. Personally identifiable information.

8. Which sentence is the best working definition of `excessive agency`?
   - A. A risk where an agent has too much autonomy, permission, or tool power.
   - B. An attack or failure where untrusted text attempts to override trusted instructions.
   - C. Personally identifiable information.
   - D. Role-based access control.

9. In production AI work, what is the primary role of `threat model`?
   - A. An attack or failure where untrusted text attempts to override trusted instructions.
   - B. Personally identifiable information.
   - C. Role-based access control.
   - D. A structured analysis of assets, actors, trust boundaries, threats, and controls.


## Applied Multiple Choice

1. Applied case: Guardrails fail when they are only prompts and not system controls.
   - A. Hard-code the new behaviour for the first failing case and call it a fix.
   - B. Set up a controlled experiment isolating `prompt injection`, capture before/after numbers, and write the result to a decision record.
   - C. Assume the largest available model will mask the underlying weakness in `prompt injection` so no system change is needed.
   - D. Skip the rollback plan; staging is close enough to production.

2. Applied case: RAG and agents expand the attack surface through retrieved context and tool output.
   - A. Add the work to the capstone as a reviewable artifact that exercises `PII` end-to-end, with tests and a trace.
   - B. Skip the rollback plan; staging is close enough to production.
   - C. Hard-code the new behaviour for the first failing case and call it a fix.
   - D. Ship the change without measurement because the most recent demo looked good.

3. Applied case: Logs, traces, embeddings, and eval datasets can all contain sensitive data.
   - A. Hard-code the new behaviour for the first failing case and call it a fix.
   - B. Ship the change without measurement because the most recent demo looked good.
   - C. Remove logging and evaluation to keep the diff small and merge faster.
   - D. Define explicit acceptance criteria, rollback steps, and a reviewer checklist tied to Security, Guardrails, and Compliance.

4. Applied case: Build a threat model for the capstone with assets, actors, trust boundaries, threats, and controls.
   - A. Remove logging and evaluation to keep the diff small and merge faster.
   - B. Assume the largest available model will mask the underlying weakness in `prompt injection` so no system change is needed.
   - C. Compare at least two approaches against a labelled set covering `threat model`, then choose on measured quality, latency, cost, and risk.
   - D. Ship the change without measurement because the most recent demo looked good.

5. Applied case: Create a 50-case guardrail test suite for prompt injection, PII, authorization, and unsafe tools.
   - A. Skip the rollback plan; staging is close enough to production.
   - B. Write a one-page design memo naming the assumption, the test that would falsify it, and the metric you'd watch in production.
   - C. Remove logging and evaluation to keep the diff small and merge faster.
   - D. Assume the largest available model will mask the underlying weakness in `prompt injection` so no system change is needed.

6. Applied case: Design audit logs for document access, retrieval, answer generation, tool calls, blocks, and approvals.
   - A. Set up a controlled experiment isolating `prompt injection`, capture before/after numbers, and write the result to a decision record.
   - B. Assume the largest available model will mask the underlying weakness in `prompt injection` so no system change is needed.
   - C. Skip the rollback plan; staging is close enough to production.
   - D. Hard-code the new behaviour for the first failing case and call it a fix.


## Fill In The Blanks

1. To handle situations where rAG and tools introduce untrusted content into model context, the engineering tool you reach for is ________ (watch for: A retrieved document says to ignore policy and reveal private data.).
2. ________ is best summarised as: Personally identifiable information. Verification step: Create PII handling rules for every data surface.
3. On a system review, you find a support user can access admin-only documents — the underlying chapter concept is ________.
4. It grants access based on attributes such as tenant, role, data class, or purpose. A common failure looks like: Role alone is too coarse for document-level permissions. The concept is ________.
5. Given the production failure "The system cannot prove which user retrieved a sensitive document.", the concept being misused is ________.
6. To handle situations where guardrails reduce risk across prompt, retrieval, generation, tools, and logs, the engineering tool you reach for is ________ (watch for: Only a prompt instruction blocks a dangerous tool action.).
7. ________ is best summarised as: Separating data and access between organizations or user groups. Verification step: Test cross-tenant retrieval and enforce filters before generation.
8. On a system review, you find the agent sends emails or updates records without approval — the underlying chapter concept is ________.
9. It makes security assumptions explicit before incidents occur. A common failure looks like: Security is added after implementation with no risk inventory. The concept is ________.

## Short Answer

1. Describe the smallest experiment that would tell you whether `prompt injection` is correctly implemented in your system.
2. When would you intentionally *avoid* using `PII`? Name a constraint or tradeoff.
3. What does a healthy log or trace look like for `RBAC`? List the fields you would expect.
4. Explain how `ABAC` appears in the capstone, what artifact proves it, and what failure mode you would test.
5. If a reviewer asks 'why does `audit log` matter here?', what one-paragraph answer do you give? Include a metric.
6. Describe the smallest experiment that would tell you whether `guardrail` is correctly implemented in your system.
7. When would you intentionally *avoid* using `tenant isolation`? Name a constraint or tradeoff.
8. What does a healthy log or trace look like for `excessive agency`? List the fields you would expect.
9. Explain how `threat model` appears in the capstone, what artifact proves it, and what failure mode you would test.

## Scenario Questions

1. Design review: Guardrails fail when they are only prompts and not system controls. Which artifact would you require before approving?
2. Postmortem prompt: RAG and agents expand the attack surface through retrieved context and tool output. What regression test would prevent recurrence?
3. On-call triage: Logs, traces, embeddings, and eval datasets can all contain sensitive data. Walk through the first three steps you would take.
4. An engineer disables `excessive agency` to mitigate latency. Quality drops the next day. What evidence reverses the decision?

## Practical Debug Questions

1. What log or trace fields would help you debug a failure in `prompt injection` in this chapter's context?
2. What single metric would you watch in production when changing `audit log`?
3. You suspect `threat model` is degraded. Design the smallest experiment that would falsify or confirm it in under an hour.
4. For the failure 'Guardrails fail when they are only prompts and not system controls.', sketch a rollback plan with a clear restore-point definition.
5. What artifact would you put in a portfolio README to prove competence with `prompt injection`, `PII`, `RBAC`?

## Answer Key

### Multiple Choice

1. D
2. C
3. B
4. A
5. D
6. C
7. B
8. A
9. D

### Applied Multiple Choice

1. B
2. A
3. D
4. C
5. B
6. A

### Fill In The Blanks

1. prompt injection
2. PII
3. RBAC
4. ABAC
5. audit log
6. guardrail
7. tenant isolation
8. excessive agency
9. threat model

Short-answer, scenario, and debug questions should be graded against the rubric in `../../syllabus/evaluation_rubric.md`.

## References

[1] OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
[2] OWASP LLM Top 10 2025 PDF: https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf
[3] NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
[4] Microsoft Responsible AI: https://www.microsoft.com/en-us/ai/principles-and-approach/
[5] Azure OpenAI responsible AI: https://learn.microsoft.com/en-us/legal/cognitive-services/openai/overview
