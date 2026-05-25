# Lesson: Agentic AI, LangGraph, and Tool Use

## 1. What Agentic AI Means

An agentic AI system does more than generate a final answer. It can plan, route, call tools, observe tool results, maintain state, ask for human approval, and continue a workflow.

Simple chatbot:

```text
user -> model -> answer
```

Agentic system:

```text
user -> planner/router -> tool calls -> observations -> state updates -> final response/action
```

## 2. Agent Components

| Component | Role |
| --- | --- |
| LLM | reasoning, planning, language interface |
| tools | external capabilities |
| state | accumulated workflow data |
| memory | selected past context |
| router | chooses path or tool |
| guardrails | enforce safety and policy |
| trace | records what happened |
| human approval | controls risky steps |

## 3. Tools

Tools are callable functions exposed to the agent.

Examples:

- search documents;
- query SQL;
- create ticket;
- fetch customer summary;
- calculate risk score;
- send email draft;
- create human review task.

Tool schema should specify:

- name;
- description;
- input schema;
- output schema;
- permissions;
- side effects;
- timeout;
- retry policy.

## 4. Tool Permission Boundary

Never rely only on the model to enforce permissions.

Correct design:

```text
agent requests tool call
  -> application validates user permission
  -> tool executes
  -> result returned to agent
```

The tool service, not the model, must enforce security.

## 5. State

State stores workflow data:

```python
class AgentState(TypedDict):
    user_id: str
    tenant_id: str
    question: str
    intent: str
    retrieved_contexts: list[dict]
    tool_results: list[dict]
    final_answer: str | None
    requires_human_approval: bool
```

State makes workflows debuggable and resumable.

## 6. LangGraph Concepts

LangGraph models workflows as graphs:

- nodes perform work;
- edges connect steps;
- conditional edges route based on state;
- state is passed and updated;
- interrupts can pause for human input.

This is useful when a simple chain is not enough.

## 7. Memory

Memory is not "store everything forever." It must be designed.

Memory types:

- short-term conversation history;
- task state;
- user preferences;
- retrieved case memory;
- long-term summaries.

Risks:

- privacy leakage;
- stale facts;
- context bloat;
- wrong personalization;
- cross-user contamination.

## 8. Human-in-the-Loop

Use human approval for:

- irreversible actions;
- financial operations;
- legal recommendations;
- private data disclosure;
- high-risk classification;
- low-confidence answer;
- policy conflict.

The agent should be able to pause, ask for approval, and resume with the approval result.

## 9. Agent Evaluation

Agent evaluation is more than final answer quality.

Evaluate:

- route selection;
- tool choice;
- tool arguments;
- tool result interpretation;
- state transitions;
- safety behavior;
- refusal correctness;
- human approval triggers.

## 10. Failure Modes

Common failures:

- wrong tool selected;
- wrong arguments;
- unauthorized tool action;
- tool result misread;
- infinite loop;
- stale memory;
- prompt injection through tool output;
- no human approval when required.

## 11. Key Takeaway

Agentic systems are workflow systems. Expertise means designing state, tool boundaries, traces, permissions, evaluation, and human control, not just letting a model call functions freely.
## Numbered References

[1] LangGraph overview: https://docs.langchain.com/oss/python/langgraph/overview
[2] LangGraph StateGraph reference: https://reference.langchain.com/python/langgraph/graph/state/StateGraph
[3] LangGraph human-in-the-loop: https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/wait-user-input/
[4] LangChain tools: https://docs.langchain.com/oss/python/langchain/tools
[5] OpenAI Agents SDK GitHub: https://github.com/openai/openai-agents-python
[6] AutoGen GitHub: https://github.com/microsoft/autogen
