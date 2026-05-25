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
