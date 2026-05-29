# Examples: Azure/OpenAI Foundry and Enterprise AI

Reusable snippets matching `lesson.md`.

## 1. One Protocol, two platform adapters

```python
class LlmProvider(Protocol):
    async def complete(self, *, system: str, messages: list[dict],
                       max_tokens: int, temperature: float) -> LlmResult: ...

class OpenAiLlmProvider:
    def __init__(self, client, model: str): self._c, self._m = client, model
    async def complete(self, **kw) -> LlmResult: ...   # OpenAI shape

class AzureOpenAiLlmProvider:
    def __init__(self, client, deployment: str):       # NOTE: deployment, not model id
        self._c, self._dep = client, deployment
    async def complete(self, **kw) -> LlmResult:
        r = await self._c.chat.completions.create(model=self._dep, **kw)
        return LlmResult(text=..., model=r.model)       # record REAL model behind alias
```

## 2. Composition root picks the platform (config-only swap)

```python
def build_llm(settings) -> LlmProvider:
    match settings.llm_provider:
        case "openai": return OpenAiLlmProvider(openai_client(), settings.llm_model)
        case "azure":  return AzureOpenAiLlmProvider(azure_client(), settings.azure_deployment)
        case "fake":   return FakeLlmProvider()
        case other:    raise ValueError(other)
```

## 3. Capability → platform mapping table (markdown)

```md
| Capability       | Your contract        | Platform fulfilment   | Owned? | Exit cost |
|------------------|----------------------|-----------------------|--------|-----------|
| LLM completion   | LlmProvider          | Azure OpenAI deploy   | rented | low       |
| Vector search    | VectorStore          | self-hosted Qdrant    | owned  | none      |
| Agent runtime    | graph + state schema | Foundry Agent Service | rented | medium    |
| Evaluation       | golden set + runner  | Foundry eval (export) | owned* | low       |
| Tracing          | OTel spans           | Foundry tracing       | owned* | low       |
| Audit            | audit_log (SQL)      | your Postgres         | owned  | none      |
```

## 4. Managed identity over API key (adapter hides it)

```python
# Azure: credential from managed identity, no key in config
from azure.identity.aio import DefaultAzureCredential

async def azure_client():
    cred = DefaultAzureCredential()           # uses managed identity in prod
    return AsyncAzureOpenAI(azure_ad_token_provider=token_provider(cred),
                            azure_endpoint=settings.azure_endpoint)
```

## 5. Handle platform quota as retryable

```python
try:
    return await provider.complete(**kw)
except RateLimitError as e:           # platform quota hit
    raise ProviderError("platform quota exceeded") from e   # retryable=True
```

## 6. Export evals so they aren't console-only

```python
def export_eval_run(run_id: str, out: Path):
    run = platform.get_eval_run(run_id)
    out.write_text(json.dumps({
        "dataset_version": run.dataset_version,
        "config": run.config,
        "per_case": run.per_case_results,
        "summary": run.summary,
    }, indent=2))
    # commit out/ to the repo: evals now reproducible and migratable
```

## 7. Framework comparison skeleton (markdown)

```md
## Decision criteria (state FIRST)
1. Existing stack: Python, not .NET
2. Need: complex stateful graph with HITL approvals
3. Governance: standard, not heavily regulated
4. Lock-in tolerance: low

## Scoring against criteria
| Option            | Fit to criteria | Notes |
|-------------------|-----------------|-------|
| LangGraph         | high            | explicit state, interrupts, OSS, low lock-in |
| Semantic Kernel   | medium          | shines in .NET; we're Python |
| OpenAI Agents SDK | medium          | OpenAI-centric; medium lock-in |
| Foundry Agent Svc | low-medium      | great if Azure-governed; we're not |

## Recommendation: LangGraph — best fit to criteria 1–4.
```

## 8. Migration plan step (provider swap = adapter + eval + flip)

```md
1. Implement AzureOpenAiLlmProvider (new adapter).
2. Point a dev environment at it via config (llm_provider=azure).
3. Run the chapter-09 eval gate on dev; compare faithfulness/latency/cost vs prod.
4. If gate passes and metrics acceptable -> flip prod config. Product API unchanged.
5. Keep old provider config for a rollback window; flip back if regressions appear.
```

## 9. Reproducibility: record real model behind alias

```python
logger.info("llm_call",
            deployment=settings.azure_deployment,   # the alias we called
            model_id=result.model,                  # the real model the platform used
            prompt_version="rag_v4")
```
