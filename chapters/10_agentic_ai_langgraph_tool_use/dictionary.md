# Dictionary: Agentic AI, LangGraph, and Tool Use

Use this dictionary at the end of the chapter. Add your own examples in `my_work/dictionary_notes.md`.

| Term | Working Definition | Why It Matters | Common Failure Mode | Mastery Check |
| --- | --- | --- | --- | --- |
| `agent` | An LLM-based system that uses state, tools, and workflow to pursue a task. | Agents can perform multi-step work but expand operational and safety risk. | The agent loops or calls tools without sufficient evidence. | Trace state transitions and evaluate route/tool decisions. |
| `tool schema` | The typed definition of a callable tool's inputs and outputs. | Schemas constrain tool calls and make validation possible. | The model sends malformed arguments to a business API. | Validate tool arguments before execution. |
| `state` | The structured data carried through an agent workflow. | State makes agent behavior inspectable, resumable, and testable. | A node overwrites previous retrieval evidence unexpectedly. | Define a state schema and trace state changes. |
| `routing` | Choosing the next step or component based on input or state. | Routing controls which model, retriever, tool, or safety path handles a request. | A risky action bypasses approval because routing is ambiguous. | Test route decisions with labeled scenarios. |
| `memory` | Selected persisted or short-term context used across turns or sessions. | Memory can improve continuity but creates privacy and staleness risk. | Old user preference influences a different user's answer. | Define memory scope, retention, deletion, and retrieval rules. |
| `human-in-the-loop` | A workflow pattern where humans review, approve, edit, or decide during execution. | It controls risky actions and improves quality in uncertain cases. | Human approval happens after the irreversible action already executed. | Insert approval before side effects and preserve resumable state. |
| `interrupt` | A mechanism that pauses workflow execution for external input. | It enables review and approval in stateful agent graphs. | The graph cannot resume because state was not checkpointed. | Test pause/resume behavior and state persistence. |
| `tool permission` | A policy determining which user or workflow may invoke a tool. | Tool permissions prevent excessive agency and unauthorized actions. | The model decides permission based on prompt text. | Enforce permissions in application code before tool execution. |
| `trace` | A recorded execution path with spans, inputs, outputs, and timings. | Traces reveal latency, state transitions, tool calls, and failures. | A bad answer cannot be debugged because intermediate retrieval is missing. | Trace API, retrieval, reranking, LLM, guardrail, and tool spans. |

<!-- HAND-AUTHORED: do not regenerate -->
## Extended Glossary

Additional terms used in this chapter, each with a concise definition and an authoritative source.

- **Agent** — an LLM that loops over decisions (answer/retrieve/tool/ask) using state until a stop condition. Source: [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)
- **ReAct** — interleaving reasoning and acting in agents. Source: [Yao et al., 2022](https://arxiv.org/abs/2210.03629)
- **Tool / tool schema** — a callable with typed, validated arguments. Source: [LangChain tools](https://docs.langchain.com/oss/python/langchain/tools)
- **State** — the typed data flowing through the workflow; append-only history. Source: [LangGraph StateGraph](https://reference.langchain.com/python/langgraph/graph/state/StateGraph)
- **Routing** — choosing the next node/tool based on state. Source: [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)
- **Memory** — persisted short/long-term context across turns. Source: [LangGraph memory](https://langchain-ai.github.io/langgraph/concepts/memory/)
- **Human-in-the-loop / interrupt** — pausing for approval before side effects; resumable from a checkpoint. Source: [LangGraph HITL](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/)
- **Checkpointer** — persistence enabling pause/resume of a graph. Source: [LangGraph persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/)
- **Tool permission / least privilege** — code-enforced authorization for tools. Source: [OWASP LLM06](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- **Excessive agency** — the risk of granting an agent too much autonomy/permission. Source: [OWASP LLM06](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- **Stopping condition** — max iterations / tool calls / repeat detection to bound the loop. Source: [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)

## Dictionary Assignment

For each term:

1. Write a one-sentence definition in your own words.
2. Write a concrete example from your capstone (or planned capstone).
3. Write one failure mode you would test against.
4. Write one metric, test, or review check that would catch the failure.
5. Link one source from `references_numbered.md`.

## References

[1] LangGraph overview: https://docs.langchain.com/oss/python/langgraph/overview
[2] LangGraph StateGraph reference: https://reference.langchain.com/python/langgraph/graph/state/StateGraph
[3] LangGraph human-in-the-loop: https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/
[4] LangChain tools: https://docs.langchain.com/oss/python/langchain/tools
[5] OpenAI Agents SDK GitHub: https://github.com/openai/openai-agents-python
[6] AutoGen GitHub: https://github.com/microsoft/autogen
