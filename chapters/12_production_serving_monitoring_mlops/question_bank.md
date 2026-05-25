# Expanded Question Bank: Production Serving, Monitoring, and MLOps

## How To Use This Bank

Answer without looking at the answer key. For every wrong answer, write one sentence explaining the concept in your own words and one sentence explaining how it appears in a production AI system.


## Multiple Choice

1. A teammate asks you to define `observability` in one sentence. Which is closest?
   - A. A recorded execution path with spans, inputs, outputs, and timings.
   - B. A recorded event emitted by a system.
   - C. The ability to understand system behavior through logs, metrics, and traces.
   - D. A numeric measurement of system behavior or quality.

2. Pick the description of `metric` you would put in a `dictionary.md` entry.
   - A. A recorded event emitted by a system.
   - B. A numeric measurement of system behavior or quality.
   - C. The ability to understand system behavior through logs, metrics, and traces.
   - D. A recorded execution path with spans, inputs, outputs, and timings.

3. Which sentence is the best working definition of `trace`?
   - A. A recorded execution path with spans, inputs, outputs, and timings.
   - B. The ability to understand system behavior through logs, metrics, and traces.
   - C. A numeric measurement of system behavior or quality.
   - D. A recorded event emitted by a system.

4. In production AI work, what is the primary role of `log`?
   - A. The ability to understand system behavior through logs, metrics, and traces.
   - B. A numeric measurement of system behavior or quality.
   - C. A recorded execution path with spans, inputs, outputs, and timings.
   - D. A recorded event emitted by a system.

5. A teammate asks you to define `SLO` in one sentence. Which is closest?
   - A. A numeric measurement of system behavior or quality.
   - B. A recorded execution path with spans, inputs, outputs, and timings.
   - C. Service Level Objective, a target for reliability or performance.
   - D. The ability to understand system behavior through logs, metrics, and traces.

6. Pick the description of `incident` you would put in a `dictionary.md` entry.
   - A. A recorded execution path with spans, inputs, outputs, and timings.
   - B. An event where system behavior harms reliability, safety, cost, or users.
   - C. The ability to understand system behavior through logs, metrics, and traces.
   - D. A numeric measurement of system behavior or quality.

7. Which sentence is the best working definition of `rollback`?
   - A. Returning a system or artifact to a previous known-good version.
   - B. The ability to understand system behavior through logs, metrics, and traces.
   - C. A numeric measurement of system behavior or quality.
   - D. A recorded execution path with spans, inputs, outputs, and timings.

8. In production AI work, what is the primary role of `feedback loop`?
   - A. The ability to understand system behavior through logs, metrics, and traces.
   - B. A numeric measurement of system behavior or quality.
   - C. A recorded execution path with spans, inputs, outputs, and timings.
   - D. A process that turns user or expert feedback into improvements and regression tests.

9. A teammate asks you to define `drift` in one sentence. Which is closest?
   - A. A numeric measurement of system behavior or quality.
   - B. A recorded execution path with spans, inputs, outputs, and timings.
   - C. A change in data, user behavior, or model behavior over time.
   - D. The ability to understand system behavior through logs, metrics, and traces.


## Applied Multiple Choice

1. Applied case: AI quality can regress even when API uptime looks healthy.
   - A. Set up a controlled experiment isolating `observability`, capture before/after numbers, and write the result to a decision record.
   - B. Ship the change without measurement because the most recent demo looked good.
   - C. Remove logging and evaluation to keep the diff small and merge faster.
   - D. Assume the largest available model will mask the underlying weakness in `observability` so no system change is needed.

2. Applied case: A bad release may come from prompt, model, index, data, or tool schema changes.
   - A. Remove logging and evaluation to keep the diff small and merge faster.
   - B. Assume the largest available model will mask the underlying weakness in `observability` so no system change is needed.
   - C. Skip the rollback plan; staging is close enough to production.
   - D. Add the work to the capstone as a reviewable artifact that exercises `metric` end-to-end, with tests and a trace.

3. Applied case: Feedback is wasted unless it becomes labeled data and regression coverage.
   - A. Skip the rollback plan; staging is close enough to production.
   - B. Hard-code the new behaviour for the first failing case and call it a fix.
   - C. Define explicit acceptance criteria, rollback steps, and a reviewer checklist tied to Production Serving, Monitoring, and MLOps.
   - D. Assume the largest available model will mask the underlying weakness in `observability` so no system change is needed.

4. Applied case: Design observability for API, retrieval, generation, agent tools, evaluation, cost, and security.
   - A. Ship the change without measurement because the most recent demo looked good.
   - B. Compare at least two approaches against a labelled set covering `drift`, then choose on measured quality, latency, cost, and risk.
   - C. Skip the rollback plan; staging is close enough to production.
   - D. Hard-code the new behaviour for the first failing case and call it a fix.

5. Applied case: Write incident runbooks for hallucination, provider outage, latency spike, data leakage, and cost spike.
   - A. Write a one-page design memo naming the assumption, the test that would falsify it, and the metric you'd watch in production.
   - B. Hard-code the new behaviour for the first failing case and call it a fix.
   - C. Ship the change without measurement because the most recent demo looked good.
   - D. Remove logging and evaluation to keep the diff small and merge faster.

6. Applied case: Build a version registry that connects releases to eval results and rollback artifacts.
   - A. Ship the change without measurement because the most recent demo looked good.
   - B. Remove logging and evaluation to keep the diff small and merge faster.
   - C. Assume the largest available model will mask the underlying weakness in `observability` so no system change is needed.
   - D. Set up a controlled experiment isolating `observability`, capture before/after numbers, and write the result to a decision record.


## Fill In The Blanks

1. AI failures require visibility into retrieval, generation, tools, and safety checks. A common failure looks like: Only final answers are logged, so failures cannot be traced. The concept is ________.
2. Given the production failure "The team debates quality without data.", the concept being misused is ________.
3. To handle situations where traces reveal latency, state transitions, tool calls, and failures, the engineering tool you reach for is ________ (watch for: A bad answer cannot be debugged because intermediate retrieval is missing.).
4. ________ is best summarised as: A recorded event emitted by a system. Verification step: Use structured logs and apply data minimization.
5. On a system review, you find latency is optimized without a clear target — the underlying chapter concept is ________.
6. AI incidents can involve quality and policy failures, not only outages. A common failure looks like: A hallucinated legal answer is treated as a normal bug. The concept is ________.
7. Given the production failure "Code is rolled back but the bad prompt remains active.", the concept being misused is ________.
8. To handle situations where it keeps production learning connected to development, the engineering tool you reach for is ________ (watch for: Feedback is stored but never labeled or reviewed.).
9. ________ is best summarised as: A change in data, user behavior, or model behavior over time. Verification step: Monitor distributions, failure rates, and eval performance over time.

## Short Answer

1. Explain how `observability` appears in the capstone, what artifact proves it, and what failure mode you would test.
2. If a reviewer asks 'why does `metric` matter here?', what one-paragraph answer do you give? Include a metric.
3. Describe the smallest experiment that would tell you whether `trace` is correctly implemented in your system.
4. When would you intentionally *avoid* using `log`? Name a constraint or tradeoff.
5. What does a healthy log or trace look like for `SLO`? List the fields you would expect.
6. Explain how `incident` appears in the capstone, what artifact proves it, and what failure mode you would test.
7. If a reviewer asks 'why does `rollback` matter here?', what one-paragraph answer do you give? Include a metric.
8. Describe the smallest experiment that would tell you whether `feedback loop` is correctly implemented in your system.
9. When would you intentionally *avoid* using `drift`? Name a constraint or tradeoff.

## Scenario Questions

1. Postmortem prompt: AI quality can regress even when API uptime looks healthy. What regression test would prevent recurrence?
2. On-call triage: A bad release may come from prompt, model, index, data, or tool schema changes. Walk through the first three steps you would take.
3. Incident: Feedback is wasted unless it becomes labeled data and regression coverage. What do you inspect first, and which metric would prove the fix?
4. A pull request modifies `rollback` and a downstream quality metric drops. What rollback, evaluation, and documentation do you require before merge?

## Practical Debug Questions

1. What log or trace fields would help you debug a failure in `observability` in this chapter's context?
2. What single metric would you watch in production when changing `SLO`?
3. You suspect `drift` is degraded. Design the smallest experiment that would falsify or confirm it in under an hour.
4. For the failure 'AI quality can regress even when API uptime looks healthy.', sketch a rollback plan with a clear restore-point definition.
5. What artifact would you put in a portfolio README to prove competence with `observability`, `metric`, `trace`?

## Answer Key

### Multiple Choice

1. C
2. B
3. A
4. D
5. C
6. B
7. A
8. D
9. C

### Applied Multiple Choice

1. A
2. D
3. C
4. B
5. A
6. D

### Fill In The Blanks

1. observability
2. metric
3. trace
4. log
5. SLO
6. incident
7. rollback
8. feedback loop
9. drift

Short-answer, scenario, and debug questions should be graded against the rubric in `../../syllabus/evaluation_rubric.md`.

## References

[1] MLflow tracking: https://www.mlflow.org/docs/latest/ml/tracking
[2] MLflow GenAI eval and monitoring: https://www.mlflow.org/docs/latest/genai/eval-monitor
[3] MLflow tracing: https://mlflow.org/docs/latest/genai/tracing/
[4] OpenTelemetry documentation: https://opentelemetry.io/docs/
[5] Prometheus documentation: https://prometheus.io/docs/
[6] Grafana documentation: https://grafana.com/docs/
