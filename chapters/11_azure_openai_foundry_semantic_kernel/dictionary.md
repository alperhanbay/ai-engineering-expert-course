# Dictionary: Azure/OpenAI Foundry and Enterprise AI

Use this dictionary at the end of the chapter. Add your own examples in `my_work/dictionary_notes.md`.

| Term | Working Definition | Why It Matters | Common Failure Mode | Mastery Check |
| --- | --- | --- | --- | --- |
| `model deployment` | A configured model endpoint available for inference. | Deployment settings affect availability, cost, quotas, and governance. | The app uses a model name but the platform requires a deployment name. | Document endpoint, model, region, quota, and fallback behavior. |
| `managed identity` | Cloud identity used by services to access resources without embedded secrets. | It reduces secret sprawl and supports enterprise access control. | API keys are stored in config files across environments. | Use identity-based access where supported and document permissions. |
| `RBAC` | Role-based access control. | It maps users or services to permitted actions and resources. | A support user can access admin-only documents. | Define roles, permissions, and tests for protected operations. |
| `Foundry project` | A managed workspace for building, evaluating, and operating AI applications in the Microsoft ecosystem. | It groups models, agents, evals, deployments, and governance assets. | Evaluation data exists only in a platform UI and cannot be reproduced. | Export or mirror critical artifacts in your repository. |
| `agent service` | A managed or application-level runtime for tool-using agents. | It can simplify deployment but must be assessed for observability and control. | The service hides tool traces needed for incident analysis. | Verify tool logs, permissions, state, and evaluation export. |
| `Semantic Kernel` | Microsoft's SDK for AI orchestration with plugins/functions and connectors. | It is useful to compare with LangGraph, LlamaIndex, and OpenAI Agents SDK. | The architecture becomes tightly coupled to one SDK abstraction. | Build a framework comparison and keep domain logic portable. |
| `governance` | Policies and controls for responsible, auditable, and compliant AI use. | Governance connects technical behavior to organizational risk. | Teams deploy model changes without review or documented risk. | Define ownership, review gates, data policy, and monitoring. |
| `vendor lock-in` | Dependence on a provider-specific API, feature, or data store that is hard to replace. | AI platforms change quickly, so portability matters. | Prompts, evals, and tool schemas live only in a vendor console. | Keep provider-neutral contracts and exportable artifacts. |

<!-- HAND-AUTHORED: do not regenerate -->
## Extended Glossary

Additional terms used in this chapter, each with a concise definition and an authoritative source.

- **Managed identity** — cloud identity letting services authenticate without embedded secrets. Source: [Microsoft Entra managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)
- **RBAC** — role-based access control. Source: [Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)
- **Deployment name** — a platform alias over a model id (Azure OpenAI); record the real model for reproducibility. Source: [Azure OpenAI deployments](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource)
- **Vendor lock-in** — dependence on provider-specific features that are costly to leave. Source: [Azure Well-Architected](https://learn.microsoft.com/en-us/azure/well-architected/)
- **Content safety** — platform input/output filtering for harmful content. Source: [Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview)
- **Data residency** — where data is processed/stored (often a regulatory requirement). Source: [Microsoft data residency](https://learn.microsoft.com/en-us/azure/availability-zones/region-types-service-categories-azure)
- **Semantic Kernel** — Microsoft's AI orchestration SDK (plugins/functions). Source: [Semantic Kernel](https://github.com/microsoft/semantic-kernel)
- **Foundry Agent Service** — Azure's managed agent runtime. Source: [Foundry Agent Service](https://learn.microsoft.com/en-gb/azure/ai-foundry/agents/overview)
- **Governance** — policies/controls for responsible, auditable AI use. Source: [Microsoft Responsible AI](https://www.microsoft.com/en-us/ai/principles-and-approach/)

## Dictionary Assignment

For each term:

1. Write a one-sentence definition in your own words.
2. Write a concrete example from your capstone (or planned capstone).
3. Write one failure mode you would test against.
4. Write one metric, test, or review check that would catch the failure.
5. Link one source from `references_numbered.md`.

## References

[1] Microsoft Foundry documentation: https://learn.microsoft.com/en-us/azure/foundry/
[2] Azure AI Foundry Agent Service: https://learn.microsoft.com/en-gb/azure/ai-foundry/agents/overview
[3] Microsoft Foundry evaluation: https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-generative-ai-app
[4] Azure OpenAI responsible AI: https://learn.microsoft.com/en-us/legal/cognitive-services/openai/overview
[5] Semantic Kernel GitHub: https://github.com/microsoft/semantic-kernel
