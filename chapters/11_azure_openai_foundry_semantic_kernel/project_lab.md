# Project Lab: Azure/OpenAI Foundry and Enterprise AI

Enterprise AI requires platform literacy without surrendering architecture to one vendor. This lab turns the chapter's projects into concrete, reviewable
deliverables. Pick one project and finish it end-to-end before starting another.
The "Acceptance Criteria" sections are the gate — not the existence of files.

## Project 1: Design a vendor-neutral enterprise AI architecture and map it to Azure/OpenAI-style services.

### Scenario

Decide how a managed enterprise AI platform (Azure AI Foundry, OpenAI Agents SDK, Semantic Kernel) fits into the capstone without surrendering portability. Build a vendor-neutral architecture and map it to one platform, with an explicit exit plan.

### Inputs

- the capstone architecture (API, retriever, generator, agent, eval, audit) at module granularity
- a feature checklist: identity, content safety, evaluation, tracing, agent orchestration, network controls, cost reporting
- two candidate framework/platform options to compare

### Outputs / Artifacts

- `architecture_neutral.md` — modules and contracts that don't name a vendor
- `platform_mapping.md` — which managed service fulfils each module; what would move with you on exit
- `framework_compare.md` — LangGraph vs Semantic Kernel vs OpenAI Agents SDK vs Foundry Agent Service on: state, tools, traces, eval, governance, lock-in
- `migration_plan.md` — replace one provider behind the existing adapter without changing product APIs

### Test Cases

- swap LLM provider via config — service tests still pass; API contract unchanged
- exported eval traces can be re-imported into a non-vendor store
- tool definitions are repo-owned, not platform-only
- an outage of the managed agent service degrades gracefully to a documented fallback path

### Metrics

- % of architecture modules with a vendor-neutral contract (target 100%)
- estimated effort (in days) to replace each platform service in the mapping
- % of evals reproducible outside the platform UI

### Failure Cases To Cover

- Prompts and tool schemas live only in a vendor console and aren't version-controlled
- Compare doc is a feature list with no architectural impact
- Migration plan assumes the new provider has every capability of the old one
- Identity/RBAC is wired to a platform abstraction with no equivalent elsewhere

### Acceptance Criteria

- every product API contract is independent of any specific platform
- framework compare results in a recommendation with measured or specific reasons
- the migration plan has a tested step (at least one provider has been swapped in dev)

### Deliverables Layout

```
my_work/
  project_1_scope.md            # one paragraph + concept list
  project_1_implementation/      # code or design doc
  project_1_report.md            # results, numbers, plots
  project_1_decision_record.md   # alternatives + chosen approach + why
  project_1_tests/               # the test cases above, runnable or scripted
```

### Expected README Section

In your portfolio README, this project should appear under "Projects" with:
a one-sentence summary, the headline metric you measured, the main tradeoff
you made, and a link to the decision record. Avoid screenshots-only entries.

## Project 2: Compare LangGraph, LlamaIndex, Semantic Kernel, OpenAI Agents SDK, and Foundry Agent Service.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `model deployment`, `managed identity`, `RBAC`, `Foundry project`, `agent service`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `model deployment`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_2_implementation/`
- `my_work/project_2_report.md` summarising results with numbers
- `my_work/project_2_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `model deployment`
- an edge case driven by the failure mode of `managed identity`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `model deployment` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Managed platforms simplify deployment but can hide architecture and portability risks.
- Evaluation and traces should be exportable and owned by the engineering team.
- Enterprise systems need identity, content safety, network, audit, and cost governance.
- silent degradation of `vendor lock-in` after a config change goes unnoticed

### Acceptance Criteria

- a reviewer can run or read the artifact and understand what was built without asking you
- every numeric claim is backed by a test, eval result, or measured run logged in the report
- at least one known limitation is named honestly (not a humblebrag)
- the artifact is wired into the capstone, not orphaned in `my_work/`

### Deliverables Layout

```
my_work/
  project_2_scope.md            # one paragraph + concept list
  project_2_implementation/      # code or design doc
  project_2_report.md            # results, numbers, plots
  project_2_decision_record.md   # alternatives + chosen approach + why
  project_2_tests/               # the test cases above, runnable or scripted
```

### Expected README Section

In your portfolio README, this project should appear under "Projects" with:
a one-sentence summary, the headline metric you measured, the main tradeoff
you made, and a link to the decision record. Avoid screenshots-only entries.

## Project 3: Write a migration plan that moves from one model provider to another without changing product APIs.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `model deployment`, `managed identity`, `RBAC`, `Foundry project`, `agent service`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `model deployment`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_3_implementation/`
- `my_work/project_3_report.md` summarising results with numbers
- `my_work/project_3_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `model deployment`
- an edge case driven by the failure mode of `managed identity`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `model deployment` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Managed platforms simplify deployment but can hide architecture and portability risks.
- Evaluation and traces should be exportable and owned by the engineering team.
- Enterprise systems need identity, content safety, network, audit, and cost governance.
- silent degradation of `vendor lock-in` after a config change goes unnoticed

### Acceptance Criteria

- a reviewer can run or read the artifact and understand what was built without asking you
- every numeric claim is backed by a test, eval result, or measured run logged in the report
- at least one known limitation is named honestly (not a humblebrag)
- the artifact is wired into the capstone, not orphaned in `my_work/`

### Deliverables Layout

```
my_work/
  project_3_scope.md            # one paragraph + concept list
  project_3_implementation/      # code or design doc
  project_3_report.md            # results, numbers, plots
  project_3_decision_record.md   # alternatives + chosen approach + why
  project_3_tests/               # the test cases above, runnable or scripted
```

### Expected README Section

In your portfolio README, this project should appear under "Projects" with:
a one-sentence summary, the headline metric you measured, the main tradeoff
you made, and a link to the decision record. Avoid screenshots-only entries.

## Review Rubric

| Dimension | Evidence that passes |
| --- | --- |
| Specificity | scenario, inputs, and outputs match what the artifact actually does |
| Measurement | metrics are numeric, named, and reproducible from the repo |
| Failure handling | at least three failure cases are exercised in tests |
| Tradeoff honesty | decision record names alternatives and a measured reason |
| Source backing | numbered references support every external claim |

## References

[1] Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/foundry/
[2] Azure AI Foundry Agent Service: https://learn.microsoft.com/en-gb/azure/ai-foundry/agents/overview
[3] Microsoft Foundry evaluation: https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-generative-ai-app
[4] Azure OpenAI responsible AI: https://learn.microsoft.com/en-us/legal/cognitive-services/openai/overview
[5] Semantic Kernel GitHub: https://github.com/microsoft/semantic-kernel
