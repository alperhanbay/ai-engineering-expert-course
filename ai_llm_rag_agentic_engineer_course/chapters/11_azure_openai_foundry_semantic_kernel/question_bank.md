# Expanded Question Bank: Azure/OpenAI Foundry and Enterprise AI

## How To Use This Bank

Answer without looking at the answer key. For every wrong answer, write one sentence explaining the concept in your own words and one sentence explaining how it appears in a production AI system.


## Multiple Choice

1. In production AI work, what is the primary role of `model deployment`?
   - A. Cloud identity used by services to access resources without embedded secrets.
   - B. Role-based access control.
   - C. A managed workspace for building, evaluating, and operating AI applications in the Microsoft ecosystem.
   - D. A configured model endpoint available for inference.

2. A teammate asks you to define `managed identity` in one sentence. Which is closest?
   - A. Role-based access control.
   - B. A managed workspace for building, evaluating, and operating AI applications in the Microsoft ecosystem.
   - C. Cloud identity used by services to access resources without embedded secrets.
   - D. A configured model endpoint available for inference.

3. Pick the description of `RBAC` you would put in a `dictionary.md` entry.
   - A. A managed workspace for building, evaluating, and operating AI applications in the Microsoft ecosystem.
   - B. Role-based access control.
   - C. A configured model endpoint available for inference.
   - D. Cloud identity used by services to access resources without embedded secrets.

4. Which sentence is the best working definition of `Foundry project`?
   - A. A managed workspace for building, evaluating, and operating AI applications in the Microsoft ecosystem.
   - B. A configured model endpoint available for inference.
   - C. Cloud identity used by services to access resources without embedded secrets.
   - D. Role-based access control.

5. In production AI work, what is the primary role of `agent service`?
   - A. A configured model endpoint available for inference.
   - B. Cloud identity used by services to access resources without embedded secrets.
   - C. Role-based access control.
   - D. A managed or application-level runtime for tool-using agents.

6. A teammate asks you to define `Semantic Kernel` in one sentence. Which is closest?
   - A. Cloud identity used by services to access resources without embedded secrets.
   - B. Role-based access control.
   - C. Microsoft's SDK for AI orchestration with plugins/functions and connectors.
   - D. A configured model endpoint available for inference.

7. Pick the description of `governance` you would put in a `dictionary.md` entry.
   - A. Role-based access control.
   - B. Policies and controls for responsible, auditable, and compliant AI use.
   - C. A configured model endpoint available for inference.
   - D. Cloud identity used by services to access resources without embedded secrets.

8. Which sentence is the best working definition of `vendor lock-in`?
   - A. Dependence on a provider-specific API, feature, or data store that is hard to replace.
   - B. A configured model endpoint available for inference.
   - C. Cloud identity used by services to access resources without embedded secrets.
   - D. Role-based access control.


## Applied Multiple Choice

1. Applied case: Managed platforms simplify deployment but can hide architecture and portability risks.
   - A. Remove logging and evaluation to keep the diff small and merge faster.
   - B. Set up a controlled experiment isolating `model deployment`, capture before/after numbers, and write the result to a decision record.
   - C. Hard-code the new behaviour for the first failing case and call it a fix.
   - D. Ship the change without measurement because the most recent demo looked good.

2. Applied case: Evaluation and traces should be exportable and owned by the engineering team.
   - A. Add the work to the capstone as a reviewable artifact that exercises `managed identity` end-to-end, with tests and a trace.
   - B. Ship the change without measurement because the most recent demo looked good.
   - C. Remove logging and evaluation to keep the diff small and merge faster.
   - D. Assume the largest available model will mask the underlying weakness in `model deployment` so no system change is needed.

3. Applied case: Enterprise systems need identity, content safety, network, audit, and cost governance.
   - A. Remove logging and evaluation to keep the diff small and merge faster.
   - B. Assume the largest available model will mask the underlying weakness in `model deployment` so no system change is needed.
   - C. Skip the rollback plan; staging is close enough to production.
   - D. Define explicit acceptance criteria, rollback steps, and a reviewer checklist tied to Azure/OpenAI Foundry and Enterprise AI.

4. Applied case: Design a vendor-neutral enterprise AI architecture and map it to Azure/OpenAI-style services.
   - A. Skip the rollback plan; staging is close enough to production.
   - B. Hard-code the new behaviour for the first failing case and call it a fix.
   - C. Compare at least two approaches against a labelled set covering `vendor lock-in`, then choose on measured quality, latency, cost, and risk.
   - D. Assume the largest available model will mask the underlying weakness in `model deployment` so no system change is needed.

5. Applied case: Compare LangGraph, LlamaIndex, Semantic Kernel, OpenAI Agents SDK, and Foundry Agent Service.
   - A. Ship the change without measurement because the most recent demo looked good.
   - B. Write a one-page design memo naming the assumption, the test that would falsify it, and the metric you'd watch in production.
   - C. Skip the rollback plan; staging is close enough to production.
   - D. Hard-code the new behaviour for the first failing case and call it a fix.

6. Applied case: Write a migration plan that moves from one model provider to another without changing product APIs.
   - A. Set up a controlled experiment isolating `model deployment`, capture before/after numbers, and write the result to a decision record.
   - B. Hard-code the new behaviour for the first failing case and call it a fix.
   - C. Ship the change without measurement because the most recent demo looked good.
   - D. Remove logging and evaluation to keep the diff small and merge faster.


## Fill In The Blanks

1. On a system review, you find the app uses a model name but the platform requires a deployment name — the underlying chapter concept is ________.
2. It reduces secret sprawl and supports enterprise access control. A common failure looks like: API keys are stored in config files across environments. The concept is ________.
3. Given the production failure "A support user can access admin-only documents.", the concept being misused is ________.
4. To handle situations where it groups models, agents, evals, deployments, and governance assets, the engineering tool you reach for is ________ (watch for: Evaluation data exists only in a platform UI and cannot be reproduced.).
5. ________ is best summarised as: A managed or application-level runtime for tool-using agents. Verification step: Verify tool logs, permissions, state, and evaluation export.
6. On a system review, you find the architecture becomes tightly coupled to one SDK abstraction — the underlying chapter concept is ________.
7. Governance connects technical behavior to organizational risk. A common failure looks like: Teams deploy model changes without review or documented risk. The concept is ________.
8. Given the production failure "Prompts, evals, and tool schemas live only in a vendor console.", the concept being misused is ________.

## Short Answer

1. What does a healthy log or trace look like for `model deployment`? List the fields you would expect.
2. Explain how `managed identity` appears in the capstone, what artifact proves it, and what failure mode you would test.
3. If a reviewer asks 'why does `RBAC` matter here?', what one-paragraph answer do you give? Include a metric.
4. Describe the smallest experiment that would tell you whether `Foundry project` is correctly implemented in your system.
5. When would you intentionally *avoid* using `agent service`? Name a constraint or tradeoff.
6. What does a healthy log or trace look like for `Semantic Kernel`? List the fields you would expect.
7. Explain how `governance` appears in the capstone, what artifact proves it, and what failure mode you would test.
8. If a reviewer asks 'why does `vendor lock-in` matter here?', what one-paragraph answer do you give? Include a metric.

## Scenario Questions

1. Design review: Managed platforms simplify deployment but can hide architecture and portability risks. Which artifact would you require before approving?
2. Postmortem prompt: Evaluation and traces should be exportable and owned by the engineering team. What regression test would prevent recurrence?
3. On-call triage: Enterprise systems need identity, content safety, network, audit, and cost governance. Walk through the first three steps you would take.
4. A pull request modifies `model deployment` and a downstream quality metric drops. What rollback, evaluation, and documentation do you require before merge?

## Practical Debug Questions

1. What log or trace fields would help you debug a failure in `model deployment` in this chapter's context?
2. What single metric would you watch in production when changing `agent service`?
3. You suspect `vendor lock-in` is degraded. Design the smallest experiment that would falsify or confirm it in under an hour.
4. For the failure 'Managed platforms simplify deployment but can hide architecture and portability risks.', sketch a rollback plan with a clear restore-point definition.
5. What artifact would you put in a portfolio README to prove competence with `model deployment`, `managed identity`, `RBAC`?

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

1. model deployment
2. managed identity
3. RBAC
4. Foundry project
5. agent service
6. Semantic Kernel
7. governance
8. vendor lock-in

Short-answer, scenario, and debug questions should be graded against the rubric in `../../syllabus/evaluation_rubric.md`.

## References

[1] Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/foundry/
[2] Azure AI Foundry Agent Service: https://learn.microsoft.com/en-gb/azure/ai-foundry/agents/overview
[3] Microsoft Foundry evaluation: https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-generative-ai-app
[4] Azure OpenAI responsible AI: https://learn.microsoft.com/en-us/legal/cognitive-services/openai/overview
[5] Semantic Kernel GitHub: https://github.com/microsoft/semantic-kernel
