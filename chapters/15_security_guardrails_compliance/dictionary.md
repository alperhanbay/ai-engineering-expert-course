# Dictionary: Security, Guardrails, and Compliance

Use this dictionary at the end of the chapter. Add your own examples in `my_work/dictionary_notes.md`.

| Term | Working Definition | Why It Matters | Common Failure Mode | Mastery Check |
| --- | --- | --- | --- | --- |
| `prompt injection` | An attack or failure where untrusted text attempts to override trusted instructions. | RAG and tools introduce untrusted content into model context. | A retrieved document says to ignore policy and reveal private data. | Create adversarial tests and enforce permissions outside the model. |
| `PII` | Personally identifiable information. | PII must be protected in prompts, logs, traces, datasets, and outputs. | A trace stores unmasked customer identifiers. | Create PII handling rules for every data surface. |
| `RBAC` | Role-based access control. | It maps users or services to permitted actions and resources. | A support user can access admin-only documents. | Define roles, permissions, and tests for protected operations. |
| `ABAC` | Attribute-based access control. | It grants access based on attributes such as tenant, role, data class, or purpose. | Role alone is too coarse for document-level permissions. | Define attribute filters used during retrieval and tool calls. |
| `audit log` | A compliance-oriented record of who accessed or changed what, when, why, and through which system. | Audit logs support investigations and regulated-domain accountability. | The system cannot prove which user retrieved a sensitive document. | Record user, tenant, action, data IDs, purpose, model/prompt/index version, and timestamp. |
| `guardrail` | A system control that prevents or detects unsafe inputs, outputs, or actions. | Guardrails reduce risk across prompt, retrieval, generation, tools, and logs. | Only a prompt instruction blocks a dangerous tool action. | Implement validation, policy checks, approval, and audit logging. |
| `tenant isolation` | Separating data and access between organizations or user groups. | It prevents cross-customer data leakage. | Vector search returns another tenant's chunk because filters are missing. | Test cross-tenant retrieval and enforce filters before generation. |
| `excessive agency` | A risk where an agent has too much autonomy, permission, or tool power. | It can cause unauthorized, irreversible, or harmful actions. | The agent sends emails or updates records without approval. | Limit tools, enforce permissions, and require human approval for side effects. |
| `threat model` | A structured analysis of assets, actors, trust boundaries, threats, and controls. | It makes security assumptions explicit before incidents occur. | Security is added after implementation with no risk inventory. | Create a threat model and update it after architecture changes. |

## Dictionary Assignment

For each term:

1. Write a one-sentence definition in your own words.
2. Write a concrete example from your capstone (or planned capstone).
3. Write one failure mode you would test against.
4. Write one metric, test, or review check that would catch the failure.
5. Link one source from `references_numbered.md`.

## References

[1] OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
[2] OWASP LLM Top 10 2025 PDF: https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf
[3] NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
[4] Microsoft Responsible AI: https://www.microsoft.com/en-us/ai/principles-and-approach/
[5] Azure OpenAI responsible AI: https://learn.microsoft.com/en-us/legal/cognitive-services/openai/overview
