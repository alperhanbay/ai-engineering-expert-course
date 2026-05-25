# Lesson: Security, Guardrails, and Compliance

## 1. Why Security Is Core AI Engineering

LLM systems can expose data, execute actions, follow malicious instructions, hallucinate unsafe claims, or leak private information. In high-risk domains, security is not optional.

Security must be enforced by the system, not only by the prompt.

## 2. Core Risks

| Risk | Example |
| --- | --- |
| prompt injection | retrieved document tells model to ignore instructions |
| data leakage | user sees another tenant's document |
| sensitive information disclosure | PII appears in answer |
| unsafe action | agent updates a record without permission |
| hallucinated advice | unsupported legal/financial answer |
| supply chain risk | unsafe third-party tool or dependency |
| model denial of service | huge input causes cost/latency spike |
| insecure plugin/tool design | tool executes untrusted input |

## 3. OWASP LLM Top 10

OWASP provides a risk framework for LLM applications. Use it as a checklist for:

- prompt injection;
- sensitive information disclosure;
- supply chain risks;
- data and model poisoning;
- improper output handling;
- excessive agency;
- system prompt leakage;
- vector and embedding weaknesses;
- misinformation;
- unbounded consumption.

Always verify current names and ordering from the OWASP source.

## 4. Guardrails

Guardrails are controls that reduce unsafe behavior.

Types:

- input validation;
- output validation;
- PII masking;
- policy classification;
- citation enforcement;
- no-answer rules;
- tool permission checks;
- human approval;
- rate limiting;
- audit logging.

Guardrails are not only prompts. They are system controls.

## 5. Access Control

Minimum access control:

```text
authenticated user
  -> tenant
  -> roles/groups
  -> data classification permissions
  -> retrieval filter
  -> tool permission check
```

The model should not decide whether the user is allowed to access data.

## 6. PII and Sensitive Data

Sensitive data can appear in:

- raw documents;
- chunks;
- embeddings;
- prompts;
- logs;
- traces;
- generated answers;
- evaluation datasets.

You need policies for:

- detection;
- masking;
- encryption;
- retention;
- deletion;
- audit access.

## 7. Prompt Injection Defense

RAG prompt injection is dangerous because the malicious instruction may come from retrieved documents.

Controls:

- isolate instructions from data;
- mark retrieved content as untrusted;
- validate tool calls outside the model;
- do not expose system prompts or secrets;
- test adversarial documents;
- log injection attempts.

## 8. Agent Security

Agents require additional controls:

- tool allowlist;
- permission checks;
- side-effect classification;
- sandboxing where possible;
- human approval;
- rate limits;
- trace review;
- rollback or compensation actions.

## 9. Auditability

Audit logs should record:

- who;
- did what;
- when;
- using which data;
- for which purpose;
- with which model/prompt/index version;
- what was returned or blocked.

Audit logs should be protected against tampering according to your compliance needs.

## 10. Key Takeaway

Safe AI systems are designed with layers: authentication, authorization, retrieval filters, prompt rules, validation, tool permissions, monitoring, human review, and audit logs.
## Numbered References

[1] OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
[2] OWASP LLM Top 10 2025 PDF: https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf
[3] NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
[4] Microsoft Responsible AI: https://www.microsoft.com/en-us/ai/principles-and-approach/
[5] Azure OpenAI responsible AI: https://learn.microsoft.com/en-us/legal/cognitive-services/openai/overview
