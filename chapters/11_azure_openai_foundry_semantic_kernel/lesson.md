# Lesson: Azure/OpenAI Foundry and Enterprise AI

## 1. Why Enterprise AI Platforms Matter

Large organizations often need managed AI platforms for:

- identity and access control;
- network isolation;
- model deployment management;
- monitoring;
- evaluation;
- governance;
- compliance;
- billing and quota control;
- integration with existing cloud services.

You should learn Azure/OpenAI-style enterprise patterns without becoming dependent on a single vendor.

## 2. Platform-Agnostic Architecture

Enterprise AI systems usually contain:

```text
client application
  -> API gateway
  -> AI application service
  -> identity and access control
  -> model endpoint
  -> search/vector index
  -> storage
  -> SQL metadata
  -> tracing and monitoring
  -> evaluation service
```

The specific product names may change, but the architecture remains.

## 3. Azure/OpenAI Concepts

Important concepts:

- model endpoint;
- deployment name;
- API key or identity-based auth;
- content filtering;
- evaluation;
- tracing;
- data storage;
- responsible AI controls;
- region and data residency;
- quotas and rate limits.

## 4. Foundry-Style Workflow

An enterprise AI platform may support:

- project/workspace organization;
- model selection;
- prompt development;
- agent creation;
- tool configuration;
- evaluation datasets;
- deployment;
- observability.

Use the platform for managed capabilities, but keep your own architecture clear.

## 5. Semantic Kernel

Semantic Kernel is a Microsoft orchestration SDK for building AI agents and workflows using plugins/functions, planners, and connectors.

Study it to understand:

- plugin/function abstraction;
- planner/workflow ideas;
- Microsoft ecosystem integration;
- differences from LangChain/LangGraph/LlamaIndex.

## 6. Enterprise Security

Enterprise AI must consider:

- RBAC;
- managed identity;
- private networking;
- encryption;
- audit logs;
- PII handling;
- content safety;
- data retention;
- third-party model data policy.

## 7. Evaluation in Enterprise Platforms

Managed platforms may provide evaluation workflows, but you still need your own quality strategy:

- golden datasets;
- domain-specific rubric;
- human review;
- regression gates;
- production feedback loop;
- release criteria.

## 8. Vendor Lock-In

Vendor-managed tools accelerate development but can create lock-in.

Reduce lock-in by:

- keeping API contracts provider-neutral;
- abstracting model providers;
- storing your own evaluation data;
- documenting prompt/model/index versions;
- avoiding platform-only concepts in core domain logic.

## 9. Key Takeaway

Enterprise AI expertise means understanding cloud platforms while preserving system architecture, governance, portability, and production quality.
## Numbered References

[1] Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/foundry/
[2] Azure AI Foundry Agent Service: https://learn.microsoft.com/en-gb/azure/ai-foundry/agents/overview
[3] Microsoft Foundry evaluation: https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-generative-ai-app
[4] Azure OpenAI responsible AI: https://learn.microsoft.com/en-us/legal/cognitive-services/openai/overview
[5] Semantic Kernel GitHub: https://github.com/microsoft/semantic-kernel
