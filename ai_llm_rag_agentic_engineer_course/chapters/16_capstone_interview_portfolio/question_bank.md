# Expanded Question Bank: Capstone, Portfolio, and Interview

## How To Use This Bank

Answer without looking at the answer key. For every wrong answer, write one sentence explaining the concept in your own words and one sentence explaining how it appears in a production AI system.


## Multiple Choice

1. In production AI work, what is the primary role of `capstone`?
   - A. A set of diagrams and documents explaining system design.
   - B. A document summarizing datasets, metrics, results, failures, and release recommendation.
   - C. A repeatable sequence showing system behavior and edge cases.
   - D. The integrated project that proves your ability to connect concepts into a working AI system.

2. A teammate asks you to define `architecture pack` in one sentence. Which is closest?
   - A. A document summarizing datasets, metrics, results, failures, and release recommendation.
   - B. A repeatable sequence showing system behavior and edge cases.
   - C. A set of diagrams and documents explaining system design.
   - D. The integrated project that proves your ability to connect concepts into a working AI system.

3. Pick the description of `evaluation report` you would put in a `dictionary.md` entry.
   - A. A repeatable sequence showing system behavior and edge cases.
   - B. A document summarizing datasets, metrics, results, failures, and release recommendation.
   - C. The integrated project that proves your ability to connect concepts into a working AI system.
   - D. A set of diagrams and documents explaining system design.

4. Which sentence is the best working definition of `demo script`?
   - A. A repeatable sequence showing system behavior and edge cases.
   - B. The integrated project that proves your ability to connect concepts into a working AI system.
   - C. A set of diagrams and documents explaining system design.
   - D. A document summarizing datasets, metrics, results, failures, and release recommendation.

5. In production AI work, what is the primary role of `system design`?
   - A. The integrated project that proves your ability to connect concepts into a working AI system.
   - B. A set of diagrams and documents explaining system design.
   - C. A document summarizing datasets, metrics, results, failures, and release recommendation.
   - D. The structured explanation of requirements, architecture, data, reliability, security, and tradeoffs.

6. A teammate asks you to define `STAR story` in one sentence. Which is closest?
   - A. A set of diagrams and documents explaining system design.
   - B. A document summarizing datasets, metrics, results, failures, and release recommendation.
   - C. A behavioral interview structure: Situation, Task, Action, Result.
   - D. The integrated project that proves your ability to connect concepts into a working AI system.

7. Pick the description of `tradeoff` you would put in a `dictionary.md` entry.
   - A. A document summarizing datasets, metrics, results, failures, and release recommendation.
   - B. A decision where improving one dimension costs another.
   - C. The integrated project that proves your ability to connect concepts into a working AI system.
   - D. A set of diagrams and documents explaining system design.

8. Which sentence is the best working definition of `portfolio README`?
   - A. The public entry document explaining the project, usage, architecture, results, and limitations.
   - B. The integrated project that proves your ability to connect concepts into a working AI system.
   - C. A set of diagrams and documents explaining system design.
   - D. A document summarizing datasets, metrics, results, failures, and release recommendation.


## Applied Multiple Choice

1. Applied case: Many portfolios show only success paths and omit evaluation or failure cases.
   - A. Remove logging and evaluation to keep the diff small and merge faster.
   - B. Set up a controlled experiment isolating `capstone`, capture before/after numbers, and write the result to a decision record.
   - C. Hard-code the new behaviour for the first failing case and call it a fix.
   - D. Ship the change without measurement because the most recent demo looked good.

2. Applied case: Interview answers fail when candidates cannot connect implementation decisions to metrics.
   - A. Add the work to the capstone as a reviewable artifact that exercises `architecture pack` end-to-end, with tests and a trace.
   - B. Ship the change without measurement because the most recent demo looked good.
   - C. Remove logging and evaluation to keep the diff small and merge faster.
   - D. Assume the largest available model will mask the underlying weakness in `capstone` so no system change is needed.

3. Applied case: Open-source quality requires runnable docs, source references, and transparent limitations.
   - A. Remove logging and evaluation to keep the diff small and merge faster.
   - B. Assume the largest available model will mask the underlying weakness in `capstone` so no system change is needed.
   - C. Skip the rollback plan; staging is close enough to production.
   - D. Define explicit acceptance criteria, rollback steps, and a reviewer checklist tied to Capstone, Portfolio, and Interview.

4. Applied case: Build the full capstone and document how to run, test, evaluate, and inspect it.
   - A. Skip the rollback plan; staging is close enough to production.
   - B. Hard-code the new behaviour for the first failing case and call it a fix.
   - C. Compare at least two approaches against a labelled set covering `portfolio README`, then choose on measured quality, latency, cost, and risk.
   - D. Assume the largest available model will mask the underlying weakness in `capstone` so no system change is needed.

5. Applied case: Create an architecture pack with API, data, RAG, agent, deployment, and threat diagrams.
   - A. Ship the change without measurement because the most recent demo looked good.
   - B. Write a one-page design memo naming the assumption, the test that would falsify it, and the metric you'd watch in production.
   - C. Skip the rollback plan; staging is close enough to production.
   - D. Hard-code the new behaviour for the first failing case and call it a fix.

6. Applied case: Write a public portfolio README with limitations, tradeoffs, metrics, and source references.
   - A. Set up a controlled experiment isolating `capstone`, capture before/after numbers, and write the result to a decision record.
   - B. Hard-code the new behaviour for the first failing case and call it a fix.
   - C. Ship the change without measurement because the most recent demo looked good.
   - D. Remove logging and evaluation to keep the diff small and merge faster.


## Fill In The Blanks

1. On a system review, you find the project shows only a happy-path demo with no evals, limitations, or source references — the underlying chapter concept is ________.
2. It lets reviewers understand APIs, data flow, deployment, security, and operations. A common failure looks like: The project cannot be reviewed because architecture is implicit in code. The concept is ________.
3. Given the production failure "Only average score is shown with no failed examples.", the concept being misused is ________.
4. To handle situations where it makes demos reliable and prevents hiding critical paths, the engineering tool you reach for is ________ (watch for: The demo only shows one successful query.).
5. ________ is best summarised as: The structured explanation of requirements, architecture, data, reliability, security, and tradeoffs. Verification step: Practice drawing and defending the capstone end to end.
6. On a system review, you find a project story lists tools but not impact or decisions — the underlying chapter concept is ________.
7. AI systems constantly trade quality, latency, cost, privacy, and complexity. A common failure looks like: The design claims one approach is best with no context. The concept is ________.
8. Given the production failure "The README has buzzwords but no runnable instructions or metrics.", the concept being misused is ________.

## Short Answer

1. What does a healthy log or trace look like for `capstone`? List the fields you would expect.
2. Explain how `architecture pack` appears in the capstone, what artifact proves it, and what failure mode you would test.
3. If a reviewer asks 'why does `evaluation report` matter here?', what one-paragraph answer do you give? Include a metric.
4. Describe the smallest experiment that would tell you whether `demo script` is correctly implemented in your system.
5. When would you intentionally *avoid* using `system design`? Name a constraint or tradeoff.
6. What does a healthy log or trace look like for `STAR story`? List the fields you would expect.
7. Explain how `tradeoff` appears in the capstone, what artifact proves it, and what failure mode you would test.
8. If a reviewer asks 'why does `portfolio README` matter here?', what one-paragraph answer do you give? Include a metric.

## Scenario Questions

1. Design review: Many portfolios show only success paths and omit evaluation or failure cases. Which artifact would you require before approving?
2. Postmortem prompt: Interview answers fail when candidates cannot connect implementation decisions to metrics. What regression test would prevent recurrence?
3. On-call triage: Open-source quality requires runnable docs, source references, and transparent limitations. Walk through the first three steps you would take.
4. An engineer disables `capstone` to mitigate latency. Quality drops the next day. What evidence reverses the decision?

## Practical Debug Questions

1. What log or trace fields would help you debug a failure in `capstone` in this chapter's context?
2. What single metric would you watch in production when changing `system design`?
3. You suspect `portfolio README` is degraded. Design the smallest experiment that would falsify or confirm it in under an hour.
4. For the failure 'Many portfolios show only success paths and omit evaluation or failure cases.', sketch a rollback plan with a clear restore-point definition.
5. What artifact would you put in a portfolio README to prove competence with `capstone`, `architecture pack`, `evaluation report`?

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

### Applied Multiple Choice

1. B
2. A
3. D
4. C
5. B
6. A

### Fill In The Blanks

1. capstone
2. architecture pack
3. evaluation report
4. demo script
5. system design
6. STAR story
7. tradeoff
8. portfolio README

Short-answer, scenario, and debug questions should be graded against the rubric in `../../syllabus/evaluation_rubric.md`.

## References

[1] OpenAI Cookbook: https://github.com/openai/openai-cookbook
[2] LangGraph GitHub: https://github.com/langchain-ai/langgraph
[3] LlamaIndex GitHub: https://github.com/run-llama/llama_index
[4] RAG Techniques GitHub: https://github.com/NirDiamant/RAG_Techniques
[5] DeepEval GitHub: https://github.com/confident-ai/deepeval
[6] RAGAS GitHub: https://github.com/explodinggradients/ragas
