# Quiz: Production Serving, Monitoring, and MLOps

## Multiple Choice

1. Which artifact should be versioned in an LLM system?
   - A. Prompt
   - B. Model
   - C. Index
   - D. All of the above

2. What does tracing help with?
   - A. Understanding request path and latency breakdown
   - B. Replacing authorization
   - C. Removing evaluation
   - D. Generating random prompts

3. Which is a production AI incident?
   - A. Cross-tenant data leakage
   - B. Model provider outage
   - C. Prompt regression
   - D. All of the above

4. What should feedback become over time?
   - A. Labeled cases and evaluation data
   - B. Unused database rows
   - C. Docker layers only
   - D. UI colors

5. Which metric is useful for cost monitoring?
   - A. Tokens per request
   - B. Font size
   - C. CSS classes
   - D. Document title length only

## Fill in the Blanks

1. p95 latency means 95 percent of requests are faster than that ________.
2. AI regression can come from code, model, prompt, index, or ________ changes.
3. Logs should be structured and ________.
4. Incident response includes containment, rollback, root cause analysis, and ________.
5. LLMOps extends MLOps with prompt, retrieval, tool, trace, and safety ________.

## Short Answer

1. Name ten fields in a production RAG log event.
2. What would you monitor to detect retrieval quality decline?
3. Explain how feedback becomes a regression test.

## Answer Key

### Multiple Choice

1. D
2. A
3. D
4. A
5. A

### Fill in the Blanks

1. threshold
2. dataset
3. queryable
4. prevention
5. management

