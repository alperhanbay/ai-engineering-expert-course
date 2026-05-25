# Expanded Question Bank: LLM and RAG Evaluation

## How To Use This Bank

Answer without looking at the answer key. For every wrong answer, write one sentence explaining the concept in your own words and one sentence explaining how it appears in a production AI system.


## Multiple Choice

1. Pick the description of `golden dataset` you would put in a `dictionary.md` entry.
   - A. How much of the retrieved context is actually relevant.
   - B. A curated set of test cases with expected behavior and reference evidence.
   - C. Whether generated claims are supported by provided context.
   - D. Whether the answer addresses the user's question.

2. Which sentence is the best working definition of `faithfulness`?
   - A. Whether generated claims are supported by provided context.
   - B. A curated set of test cases with expected behavior and reference evidence.
   - C. Whether the answer addresses the user's question.
   - D. How much of the retrieved context is actually relevant.

3. In production AI work, what is the primary role of `answer relevance`?
   - A. A curated set of test cases with expected behavior and reference evidence.
   - B. Whether generated claims are supported by provided context.
   - C. How much of the retrieved context is actually relevant.
   - D. Whether the answer addresses the user's question.

4. A teammate asks you to define `context precision` in one sentence. Which is closest?
   - A. Whether generated claims are supported by provided context.
   - B. Whether the answer addresses the user's question.
   - C. How much of the retrieved context is actually relevant.
   - D. A curated set of test cases with expected behavior and reference evidence.

5. Pick the description of `context recall` you would put in a `dictionary.md` entry.
   - A. Whether the answer addresses the user's question.
   - B. Whether the necessary evidence was retrieved.
   - C. A curated set of test cases with expected behavior and reference evidence.
   - D. Whether generated claims are supported by provided context.

6. Which sentence is the best working definition of `human review`?
   - A. Structured expert evaluation of model or system behavior.
   - B. A curated set of test cases with expected behavior and reference evidence.
   - C. Whether generated claims are supported by provided context.
   - D. Whether the answer addresses the user's question.

7. In production AI work, what is the primary role of `regression gate`?
   - A. A curated set of test cases with expected behavior and reference evidence.
   - B. Whether generated claims are supported by provided context.
   - C. Whether the answer addresses the user's question.
   - D. A release check that blocks quality, safety, or latency regressions.

8. A teammate asks you to define `failure taxonomy` in one sentence. Which is closest?
   - A. Whether generated claims are supported by provided context.
   - B. Whether the answer addresses the user's question.
   - C. A classification scheme for errors and defects.
   - D. A curated set of test cases with expected behavior and reference evidence.


## Applied Multiple Choice

1. Applied case: Aggregate scores hide failure categories that matter to users.
   - A. Ship the change without measurement because the most recent demo looked good.
   - B. Remove logging and evaluation to keep the diff small and merge faster.
   - C. Assume the largest available model will mask the underlying weakness in `golden dataset` so no system change is needed.
   - D. Set up a controlled experiment isolating `golden dataset`, capture before/after numbers, and write the result to a decision record.

2. Applied case: LLM-as-judge metrics need calibration against human review.
   - A. Assume the largest available model will mask the underlying weakness in `golden dataset` so no system change is needed.
   - B. Skip the rollback plan; staging is close enough to production.
   - C. Add the work to the capstone as a reviewable artifact that exercises `faithfulness` end-to-end, with tests and a trace.
   - D. Remove logging and evaluation to keep the diff small and merge faster.

3. Applied case: Evaluation must cover retrieval, generation, citations, tools, and safety.
   - A. Hard-code the new behaviour for the first failing case and call it a fix.
   - B. Define explicit acceptance criteria, rollback steps, and a reviewer checklist tied to LLM and RAG Evaluation.
   - C. Assume the largest available model will mask the underlying weakness in `golden dataset` so no system change is needed.
   - D. Skip the rollback plan; staging is close enough to production.

4. Applied case: Create a 100-case golden dataset with expected answer, reference context, and risk level.
   - A. Compare at least two approaches against a labelled set covering `failure taxonomy`, then choose on measured quality, latency, cost, and risk.
   - B. Skip the rollback plan; staging is close enough to production.
   - C. Hard-code the new behaviour for the first failing case and call it a fix.
   - D. Ship the change without measurement because the most recent demo looked good.

5. Applied case: Build a RAG evaluation runner that stores traces, metrics, failures, and release recommendation.
   - A. Hard-code the new behaviour for the first failing case and call it a fix.
   - B. Ship the change without measurement because the most recent demo looked good.
   - C. Remove logging and evaluation to keep the diff small and merge faster.
   - D. Write a one-page design memo naming the assumption, the test that would falsify it, and the metric you'd watch in production.

6. Applied case: Design a human review workflow that turns expert feedback into new eval cases.
   - A. Remove logging and evaluation to keep the diff small and merge faster.
   - B. Assume the largest available model will mask the underlying weakness in `golden dataset` so no system change is needed.
   - C. Set up a controlled experiment isolating `golden dataset`, capture before/after numbers, and write the result to a decision record.
   - D. Ship the change without measurement because the most recent demo looked good.


## Fill In The Blanks

1. It provides regression protection for prompts, models, indexes, and retrievers. A common failure looks like: A new prompt feels better but silently breaks old high-risk cases. The concept is ________.
2. Given the production failure "The answer is relevant but includes unsupported details.", the concept being misused is ________.
3. To handle situations where a faithful answer can still be incomplete or off-task, the engineering tool you reach for is ________ (watch for: The model cites context but answers a different question.).
4. ________ is best summarised as: How much of the retrieved context is actually relevant. Verification step: Measure relevance of retrieved chunks used for generation.
5. On a system review, you find the correct statute section never reaches the prompt — the underlying chapter concept is ________.
6. It calibrates automated metrics and catches domain-specific risk. A common failure looks like: Experts leave comments but no score or failure category. The concept is ________.
7. Given the production failure "A new reranker lowers latency but hurts citation correctness.", the concept being misused is ________.
8. To handle situations where it turns failures into actionable improvement areas, the engineering tool you reach for is ________ (watch for: All bad answers are labeled 'hallucination' even when retrieval failed.).

## Short Answer

1. Explain how `golden dataset` appears in the capstone, what artifact proves it, and what failure mode you would test.
2. If a reviewer asks 'why does `faithfulness` matter here?', what one-paragraph answer do you give? Include a metric.
3. Describe the smallest experiment that would tell you whether `answer relevance` is correctly implemented in your system.
4. When would you intentionally *avoid* using `context precision`? Name a constraint or tradeoff.
5. What does a healthy log or trace look like for `context recall`? List the fields you would expect.
6. Explain how `human review` appears in the capstone, what artifact proves it, and what failure mode you would test.
7. If a reviewer asks 'why does `regression gate` matter here?', what one-paragraph answer do you give? Include a metric.
8. Describe the smallest experiment that would tell you whether `failure taxonomy` is correctly implemented in your system.

## Scenario Questions

1. On-call triage: Aggregate scores hide failure categories that matter to users. Walk through the first three steps you would take.
2. Incident: LLM-as-judge metrics need calibration against human review. What do you inspect first, and which metric would prove the fix?
3. Design review: Evaluation must cover retrieval, generation, citations, tools, and safety. Which artifact would you require before approving?
4. A pull request modifies `answer relevance` and a downstream quality metric drops. What rollback, evaluation, and documentation do you require before merge?

## Practical Debug Questions

1. What log or trace fields would help you debug a failure in `golden dataset` in this chapter's context?
2. What single metric would you watch in production when changing `context recall`?
3. You suspect `failure taxonomy` is degraded. Design the smallest experiment that would falsify or confirm it in under an hour.
4. For the failure 'Aggregate scores hide failure categories that matter to users.', sketch a rollback plan with a clear restore-point definition.
5. What artifact would you put in a portfolio README to prove competence with `golden dataset`, `faithfulness`, `answer relevance`?

## Answer Key

### Multiple Choice

1. B
2. A
3. D
4. C
5. B
6. A
7. D
8. C

### Applied Multiple Choice

1. D
2. C
3. B
4. A
5. D
6. C

### Fill In The Blanks

1. golden dataset
2. faithfulness
3. answer relevance
4. context precision
5. context recall
6. human review
7. regression gate
8. failure taxonomy

Short-answer, scenario, and debug questions should be graded against the rubric in `../../syllabus/evaluation_rubric.md`.

## References

[1] RAGAS metrics: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/
[2] RAGAS GitHub: https://github.com/explodinggradients/ragas
[3] DeepEval documentation: https://deepeval.com/docs/introduction
[4] DeepEval GitHub: https://github.com/confident-ai/deepeval
[5] LangSmith evaluation concepts: https://docs.langchain.com/langsmith/evaluation-concepts
[6] RAGAS paper: https://arxiv.org/abs/2309.15217
[7] ARES paper: https://arxiv.org/abs/2311.09476
