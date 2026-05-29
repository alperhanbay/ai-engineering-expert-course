# Homework: Azure/OpenAI Foundry and Enterprise AI

Graded against `../../syllabus/evaluation_rubric.md`. Outputs under `my_work/`.

## Required

1. **Vendor-neutral architecture.** Write `my_work/architecture_neutral.md`
   describing your capstone in capabilities and contracts (LLM, embeddings,
   vector search, agent orchestration, eval, tracing, identity, content
   safety, audit) — naming no vendor.

2. **Platform mapping.** Write `my_work/platform_mapping.md` mapping each
   capability to a managed-platform service, marking each as self-owned or
   rented, with an exit-cost estimate (none/low/medium/high) and what would
   move with you on exit.

3. **Provider adapter.** Implement (or stub) two adapters for the same
   `LlmProvider` Protocol — e.g. a hosted-API adapter and an Azure-deployment
   adapter. Prove your service tests pass against both by swapping config only.

4. **Framework comparison.** Write `my_work/framework_compare.md` comparing
   LangGraph, Semantic Kernel, OpenAI Agents SDK, and Foundry Agent Service on
   state, tools, HITL, tracing, eval, and lock-in. State your decision criteria
   first, then recommend one for your capstone with reasons.

5. **Migration plan.** Write `my_work/migration_plan.md` for swapping the model
   provider behind your adapter without changing the product API, including the
   chapter-09 eval-gate step and a rollback. Actually swap the provider in dev
   as proof and note what broke.

## Stretch

6. **Export proof.** Demonstrate that your golden set and at least one eval run
   can be exported from any platform tooling and re-imported / version
   controlled (not console-only).

7. **Deployment-name reproducibility.** Show how you record the real model id
   behind a deployment alias so a past answer is reproducible.

8. **Governance checklist.** Write `my_work/governance.md` covering data
   residency, data-usage terms, network isolation, identity, and cost
   governance for your chosen platform — marking which are verified facts vs
   assumptions.

## Acceptance

- Service tests pass against two providers with only a config change.
- The mapping marks every capability self-owned vs rented with an exit cost.
- The framework comparison states decision criteria before recommending.
- The migration plan has at least one rehearsed (dev) provider swap.
