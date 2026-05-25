# Expanded Question Bank: Agentic AI, LangGraph, and Tool Use

## How To Use This Bank

Answer without looking at the answer key. For every wrong answer, write one sentence explaining the concept in your own words and one sentence explaining how it appears in a production AI system.


## Multiple Choice

1. In production AI work, what is the primary role of `agent`?
   - A. The typed definition of a callable tool's inputs and outputs.
   - B. The structured data carried through an agent workflow.
   - C. Choosing the next step or component based on input or state.
   - D. An LLM-based system that uses state, tools, and workflow to pursue a task.

2. A teammate asks you to define `tool schema` in one sentence. Which is closest?
   - A. The structured data carried through an agent workflow.
   - B. Choosing the next step or component based on input or state.
   - C. The typed definition of a callable tool's inputs and outputs.
   - D. An LLM-based system that uses state, tools, and workflow to pursue a task.

3. Pick the description of `state` you would put in a `dictionary.md` entry.
   - A. Choosing the next step or component based on input or state.
   - B. The structured data carried through an agent workflow.
   - C. An LLM-based system that uses state, tools, and workflow to pursue a task.
   - D. The typed definition of a callable tool's inputs and outputs.

4. Which sentence is the best working definition of `routing`?
   - A. Choosing the next step or component based on input or state.
   - B. An LLM-based system that uses state, tools, and workflow to pursue a task.
   - C. The typed definition of a callable tool's inputs and outputs.
   - D. The structured data carried through an agent workflow.

5. In production AI work, what is the primary role of `memory`?
   - A. An LLM-based system that uses state, tools, and workflow to pursue a task.
   - B. The typed definition of a callable tool's inputs and outputs.
   - C. The structured data carried through an agent workflow.
   - D. Selected persisted or short-term context used across turns or sessions.

6. A teammate asks you to define `human-in-the-loop` in one sentence. Which is closest?
   - A. The typed definition of a callable tool's inputs and outputs.
   - B. The structured data carried through an agent workflow.
   - C. A workflow pattern where humans review, approve, edit, or decide during execution.
   - D. An LLM-based system that uses state, tools, and workflow to pursue a task.

7. Pick the description of `interrupt` you would put in a `dictionary.md` entry.
   - A. The structured data carried through an agent workflow.
   - B. A mechanism that pauses workflow execution for external input.
   - C. An LLM-based system that uses state, tools, and workflow to pursue a task.
   - D. The typed definition of a callable tool's inputs and outputs.

8. Which sentence is the best working definition of `tool permission`?
   - A. A policy determining which user or workflow may invoke a tool.
   - B. An LLM-based system that uses state, tools, and workflow to pursue a task.
   - C. The typed definition of a callable tool's inputs and outputs.
   - D. The structured data carried through an agent workflow.

9. In production AI work, what is the primary role of `trace`?
   - A. An LLM-based system that uses state, tools, and workflow to pursue a task.
   - B. The typed definition of a callable tool's inputs and outputs.
   - C. The structured data carried through an agent workflow.
   - D. A recorded execution path with spans, inputs, outputs, and timings.


## Applied Multiple Choice

1. Applied case: Agents can call the wrong tool or take unauthorized actions if boundaries are weak.
   - A. Ship the change without measurement because the most recent demo looked good.
   - B. Set up a controlled experiment isolating `agent`, capture before/after numbers, and write the result to a decision record.
   - C. Skip the rollback plan; staging is close enough to production.
   - D. Hard-code the new behaviour for the first failing case and call it a fix.

2. Applied case: Memory improves continuity but creates privacy and stale-context risks.
   - A. Add the work to the capstone as a reviewable artifact that exercises `tool schema` end-to-end, with tests and a trace.
   - B. Hard-code the new behaviour for the first failing case and call it a fix.
   - C. Ship the change without measurement because the most recent demo looked good.
   - D. Remove logging and evaluation to keep the diff small and merge faster.

3. Applied case: Final-answer evaluation is not enough for agent workflows.
   - A. Ship the change without measurement because the most recent demo looked good.
   - B. Remove logging and evaluation to keep the diff small and merge faster.
   - C. Assume the largest available model will mask the underlying weakness in `agent` so no system change is needed.
   - D. Define explicit acceptance criteria, rollback steps, and a reviewer checklist tied to Agentic AI, LangGraph, and Tool Use.

4. Applied case: Build a stateful agent graph with classify, retrieve, tool-call, approval, and final-answer nodes.
   - A. Assume the largest available model will mask the underlying weakness in `agent` so no system change is needed.
   - B. Skip the rollback plan; staging is close enough to production.
   - C. Compare at least two approaches against a labelled set covering `trace`, then choose on measured quality, latency, cost, and risk.
   - D. Remove logging and evaluation to keep the diff small and merge faster.

5. Applied case: Create a tool safety lab with permissions, audit events, retries, and timeout behavior.
   - A. Hard-code the new behaviour for the first failing case and call it a fix.
   - B. Write a one-page design memo naming the assumption, the test that would falsify it, and the metric you'd watch in production.
   - C. Assume the largest available model will mask the underlying weakness in `agent` so no system change is needed.
   - D. Skip the rollback plan; staging is close enough to production.

6. Applied case: Build an agent evaluation dataset for route choice, tool arguments, approval triggers, and unsafe requests.
   - A. Set up a controlled experiment isolating `agent`, capture before/after numbers, and write the result to a decision record.
   - B. Skip the rollback plan; staging is close enough to production.
   - C. Hard-code the new behaviour for the first failing case and call it a fix.
   - D. Ship the change without measurement because the most recent demo looked good.


## Fill In The Blanks

1. ________ is best summarised as: An LLM-based system that uses state, tools, and workflow to pursue a task. Verification step: Trace state transitions and evaluate route/tool decisions.
2. On a system review, you find the model sends malformed arguments to a business API — the underlying chapter concept is ________.
3. State makes agent behavior inspectable, resumable, and testable. A common failure looks like: A node overwrites previous retrieval evidence unexpectedly. The concept is ________.
4. Given the production failure "A risky action bypasses approval because routing is ambiguous.", the concept being misused is ________.
5. To handle situations where memory can improve continuity but creates privacy and staleness risk, the engineering tool you reach for is ________ (watch for: Old user preference influences a different user's answer.).
6. ________ is best summarised as: A workflow pattern where humans review, approve, edit, or decide during execution. Verification step: Insert approval before side effects and preserve resumable state.
7. On a system review, you find the graph cannot resume because state was not checkpointed — the underlying chapter concept is ________.
8. Tool permissions prevent excessive agency and unauthorized actions. A common failure looks like: The model decides permission based on prompt text. The concept is ________.
9. Given the production failure "A bad answer cannot be debugged because intermediate retrieval is missing.", the concept being misused is ________.

## Short Answer

1. When would you intentionally *avoid* using `agent`? Name a constraint or tradeoff.
2. What does a healthy log or trace look like for `tool schema`? List the fields you would expect.
3. Explain how `state` appears in the capstone, what artifact proves it, and what failure mode you would test.
4. If a reviewer asks 'why does `routing` matter here?', what one-paragraph answer do you give? Include a metric.
5. Describe the smallest experiment that would tell you whether `memory` is correctly implemented in your system.
6. When would you intentionally *avoid* using `human-in-the-loop`? Name a constraint or tradeoff.
7. What does a healthy log or trace look like for `interrupt`? List the fields you would expect.
8. Explain how `tool permission` appears in the capstone, what artifact proves it, and what failure mode you would test.
9. If a reviewer asks 'why does `trace` matter here?', what one-paragraph answer do you give? Include a metric.

## Scenario Questions

1. Design review: Agents can call the wrong tool or take unauthorized actions if boundaries are weak. Which artifact would you require before approving?
2. Postmortem prompt: Memory improves continuity but creates privacy and stale-context risks. What regression test would prevent recurrence?
3. On-call triage: Final-answer evaluation is not enough for agent workflows. Walk through the first three steps you would take.
4. A teammate proposes a major change to `human-in-the-loop` with no experiment. Which artifact do you ask for before approving?

## Practical Debug Questions

1. What log or trace fields would help you debug a failure in `agent` in this chapter's context?
2. What single metric would you watch in production when changing `memory`?
3. You suspect `trace` is degraded. Design the smallest experiment that would falsify or confirm it in under an hour.
4. For the failure 'Agents can call the wrong tool or take unauthorized actions if boundaries are weak.', sketch a rollback plan with a clear restore-point definition.
5. What artifact would you put in a portfolio README to prove competence with `agent`, `tool schema`, `state`?

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

1. agent
2. tool schema
3. state
4. routing
5. memory
6. human-in-the-loop
7. interrupt
8. tool permission
9. trace

Short-answer, scenario, and debug questions should be graded against the rubric in `../../syllabus/evaluation_rubric.md`.

## References

[1] LangGraph overview: https://docs.langchain.com/oss/python/langgraph/overview
[2] LangGraph StateGraph reference: https://reference.langchain.com/python/langgraph/graph/state/StateGraph
[3] LangGraph human-in-the-loop: https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/
[4] LangChain tools: https://docs.langchain.com/oss/python/langchain/tools
[5] OpenAI Agents SDK GitHub: https://github.com/openai/openai-agents-python
[6] AutoGen GitHub: https://github.com/microsoft/autogen
