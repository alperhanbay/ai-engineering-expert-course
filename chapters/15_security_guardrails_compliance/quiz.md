# Quiz: Security, Guardrails, and Compliance

## Multiple Choice

1. Are guardrails only prompts?
   - A. No, they include system controls such as validation, permissions, masking, and audit logs
   - B. Yes, only system prompts
   - C. Yes, only user prompts
   - D. They are unrelated to AI

2. Who should enforce data access permissions?
   - A. The application/system layer
   - B. The model's good intentions only
   - C. The user
   - D. The citation string

3. Why is RAG prompt injection dangerous?
   - A. Retrieved documents may contain malicious instructions
   - B. It improves vector recall
   - C. It is only a UI issue
   - D. It cannot happen

4. Which is sensitive data storage risk?
   - A. Logs and traces may contain private content
   - B. Prompts never contain data
   - C. Embeddings are always free of risk
   - D. Evaluation data cannot leak

5. What should an audit log answer?
   - A. Who did what, when, using which data, and why
   - B. Only CSS theme
   - C. Only Docker build time
   - D. Nothing

## Fill in the Blanks

1. Prompt injection attempts to override trusted ________.
2. PII stands for personally identifiable ________.
3. The model should not be the only layer enforcing ________.
4. Agents need stricter control because tools may have side ________.
5. Audit logs should be protected against ________.

## Short Answer

1. Name five OWASP-style risks for LLM applications.
2. Design a tenant-aware retrieval filter.
3. Explain how you would handle PII in logs and traces.

## Answer Key

### Multiple Choice

1. A
2. A
3. A
4. A
5. A

### Fill in the Blanks

1. instructions
2. information
3. permissions
4. effects
5. tampering

