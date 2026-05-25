# Expanded Question Bank: Orientation and Expert Roadmap

## How To Use This Bank

Answer without looking at the answer key. For every wrong answer, write one sentence explaining the concept in your own words and one sentence explaining how it appears in a production AI system.


## Multiple Choice

1. Which sentence is the best working definition of `AI engineering`?
   - A. The practice of building reliable products around AI models, data, APIs, evaluation, and operations.
   - B. The explicit line separating users, APIs, model providers, data stores, tools, and operations.
   - C. The integrated project that proves your ability to connect concepts into a working AI system.
   - D. A collection of code, diagrams, evaluations, logs, and decision records proving competence.

2. In production AI work, what is the primary role of `system boundary`?
   - A. The practice of building reliable products around AI models, data, APIs, evaluation, and operations.
   - B. The integrated project that proves your ability to connect concepts into a working AI system.
   - C. A collection of code, diagrams, evaluations, logs, and decision records proving competence.
   - D. The explicit line separating users, APIs, model providers, data stores, tools, and operations.

3. A teammate asks you to define `capstone` in one sentence. Which is closest?
   - A. The explicit line separating users, APIs, model providers, data stores, tools, and operations.
   - B. A collection of code, diagrams, evaluations, logs, and decision records proving competence.
   - C. The integrated project that proves your ability to connect concepts into a working AI system.
   - D. The practice of building reliable products around AI models, data, APIs, evaluation, and operations.

4. Pick the description of `evidence portfolio` you would put in a `dictionary.md` entry.
   - A. The integrated project that proves your ability to connect concepts into a working AI system.
   - B. A collection of code, diagrams, evaluations, logs, and decision records proving competence.
   - C. The practice of building reliable products around AI models, data, APIs, evaluation, and operations.
   - D. The explicit line separating users, APIs, model providers, data stores, tools, and operations.

5. Which sentence is the best working definition of `failure log`?
   - A. A structured record of failed cases, root causes, fixes, and follow-up tests.
   - B. The practice of building reliable products around AI models, data, APIs, evaluation, and operations.
   - C. The explicit line separating users, APIs, model providers, data stores, tools, and operations.
   - D. The integrated project that proves your ability to connect concepts into a working AI system.

6. In production AI work, what is the primary role of `decision record`?
   - A. The practice of building reliable products around AI models, data, APIs, evaluation, and operations.
   - B. The explicit line separating users, APIs, model providers, data stores, tools, and operations.
   - C. The integrated project that proves your ability to connect concepts into a working AI system.
   - D. A concise document explaining an engineering choice, alternatives, tradeoffs, and evidence.

7. A teammate asks you to define `source map` in one sentence. Which is closest?
   - A. The explicit line separating users, APIs, model providers, data stores, tools, and operations.
   - B. The integrated project that proves your ability to connect concepts into a working AI system.
   - C. A curated map of official docs, repositories, papers, and standards used for verification.
   - D. The practice of building reliable products around AI models, data, APIs, evaluation, and operations.

8. Pick the description of `expert rubric` you would put in a `dictionary.md` entry.
   - A. The integrated project that proves your ability to connect concepts into a working AI system.
   - B. A scoring system that distinguishes definition, implementation, evaluation, and production judgment.
   - C. The practice of building reliable products around AI models, data, APIs, evaluation, and operations.
   - D. The explicit line separating users, APIs, model providers, data stores, tools, and operations.


## Applied Multiple Choice

1. Applied case: Many learners collect tools without building an integrated system.
   - A. Hard-code the new behaviour for the first failing case and call it a fix.
   - B. Ship the change without measurement because the most recent demo looked good.
   - C. Set up a controlled experiment isolating `AI engineering`, capture before/after numbers, and write the result to a decision record.
   - D. Skip the rollback plan; staging is close enough to production.

2. Applied case: Demos hide evaluation, security, latency, and rollback problems.
   - A. Remove logging and evaluation to keep the diff small and merge faster.
   - B. Add the work to the capstone as a reviewable artifact that exercises `system boundary` end-to-end, with tests and a trace.
   - C. Hard-code the new behaviour for the first failing case and call it a fix.
   - D. Ship the change without measurement because the most recent demo looked good.

3. Applied case: A serious portfolio needs evidence, not only screenshots.
   - A. Define explicit acceptance criteria, rollback steps, and a reviewer checklist tied to Orientation and Expert Roadmap.
   - B. Ship the change without measurement because the most recent demo looked good.
   - C. Remove logging and evaluation to keep the diff small and merge faster.
   - D. Assume the largest available model will mask the underlying weakness in `AI engineering` so no system change is needed.

4. Applied case: Build a public-style learning roadmap with evidence checkpoints.
   - A. Remove logging and evaluation to keep the diff small and merge faster.
   - B. Assume the largest available model will mask the underlying weakness in `AI engineering` so no system change is needed.
   - C. Skip the rollback plan; staging is close enough to production.
   - D. Compare at least two approaches against a labelled set covering `expert rubric`, then choose on measured quality, latency, cost, and risk.

5. Applied case: Write a capstone proposal with data, users, risks, and success metrics.
   - A. Skip the rollback plan; staging is close enough to production.
   - B. Hard-code the new behaviour for the first failing case and call it a fix.
   - C. Write a one-page design memo naming the assumption, the test that would falsify it, and the metric you'd watch in production.
   - D. Assume the largest available model will mask the underlying weakness in `AI engineering` so no system change is needed.

6. Applied case: Create a decision log template and use it for the first five architecture choices.
   - A. Ship the change without measurement because the most recent demo looked good.
   - B. Set up a controlled experiment isolating `AI engineering`, capture before/after numbers, and write the result to a decision record.
   - C. Skip the rollback plan; staging is close enough to production.
   - D. Hard-code the new behaviour for the first failing case and call it a fix.


## Fill In The Blanks

1. ________ is best summarised as: The practice of building reliable products around AI models, data, APIs, evaluation, and operations. Verification step: Draw the full system boundary and identify every non-model component required for production.
2. On a system review, you find a client depends on an internal vector DB schema and breaks when retrieval changes — the underlying chapter concept is ________.
3. A capstone turns learning into evidence that can be reviewed by others. A common failure looks like: The project shows only a happy-path demo with no evals, limitations, or source references. The concept is ________.
4. Given the production failure "The README says 'production-ready' but provides no traces, tests, or quality report.", the concept being misused is ________.
5. To handle situations where failures are the fastest path to robust AI systems because aggregate metrics hide edge cases, the engineering tool you reach for is ________ (watch for: Repeated hallucinations are fixed ad hoc and never added to regression tests.).
6. ________ is best summarised as: A concise document explaining an engineering choice, alternatives, tradeoffs, and evidence. Verification step: Write a decision record for model, vector DB, chunking, reranking, and security choices.
7. On a system review, you find the curriculum cites blog summaries while official APIs have changed — the underlying chapter concept is ________.
8. It prevents shallow completion and makes progress measurable. A common failure looks like: A learner marks a chapter complete after reading definitions only. The concept is ________.

## Short Answer

1. When would you intentionally *avoid* using `AI engineering`? Name a constraint or tradeoff.
2. What does a healthy log or trace look like for `system boundary`? List the fields you would expect.
3. Explain how `capstone` appears in the capstone, what artifact proves it, and what failure mode you would test.
4. If a reviewer asks 'why does `evidence portfolio` matter here?', what one-paragraph answer do you give? Include a metric.
5. Describe the smallest experiment that would tell you whether `failure log` is correctly implemented in your system.
6. When would you intentionally *avoid* using `decision record`? Name a constraint or tradeoff.
7. What does a healthy log or trace look like for `source map`? List the fields you would expect.
8. Explain how `expert rubric` appears in the capstone, what artifact proves it, and what failure mode you would test.

## Scenario Questions

1. Incident: Many learners collect tools without building an integrated system. What do you inspect first, and which metric would prove the fix?
2. Design review: Demos hide evaluation, security, latency, and rollback problems. Which artifact would you require before approving?
3. Postmortem prompt: A serious portfolio needs evidence, not only screenshots. What regression test would prevent recurrence?
4. A teammate proposes a major change to `expert rubric` with no experiment. Which artifact do you ask for before approving?

## Practical Debug Questions

1. What log or trace fields would help you debug a failure in `AI engineering` in this chapter's context?
2. What single metric would you watch in production when changing `failure log`?
3. You suspect `expert rubric` is degraded. Design the smallest experiment that would falsify or confirm it in under an hour.
4. For the failure 'Many learners collect tools without building an integrated system.', sketch a rollback plan with a clear restore-point definition.
5. What artifact would you put in a portfolio README to prove competence with `AI engineering`, `system boundary`, `capstone`?

## Answer Key

### Multiple Choice

1. A
2. D
3. C
4. B
5. A
6. D
7. C
8. B

### Applied Multiple Choice

1. C
2. B
3. A
4. D
5. C
6. B

### Fill In The Blanks

1. AI engineering
2. system boundary
3. capstone
4. evidence portfolio
5. failure log
6. decision record
7. source map
8. expert rubric

Short-answer, scenario, and debug questions should be graded against the rubric in `../../syllabus/evaluation_rubric.md`.

## References

[1] OpenAI platform documentation: https://platform.openai.com/docs
[2] LangGraph overview: https://docs.langchain.com/oss/python/langgraph/overview
[3] LlamaIndex RAG overview: https://developers.llamaindex.ai/python/framework/understanding/rag/
[4] OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
