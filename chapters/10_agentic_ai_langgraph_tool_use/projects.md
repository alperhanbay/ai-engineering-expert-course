# Projects: Agentic AI, LangGraph, and Tool Use

## Project 1: Stateful Agent Workflow

Build a graph with:

- classify intent;
- retrieve context;
- decide tool;
- call tool;
- validate result;
- generate response;
- human approval if needed.

Deliverables:

- state schema;
- graph diagram;
- tool schemas;
- trace examples;
- tests for each route.

## Project 2: Tool Safety Lab

Create three tools:

- `search_documents`;
- `get_case_summary`;
- `create_review_task`.

For each tool, define:

- required permission;
- allowed input;
- side effects;
- audit event;
- failure behavior.

## Project 3: Agent Evaluation Dataset

Create 30 agent test cases:

- correct tool required;
- no tool required;
- unauthorized tool request;
- high-risk action requiring approval;
- prompt injection in tool output;
- tool timeout.

