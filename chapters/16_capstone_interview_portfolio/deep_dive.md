# Deep Dive: Capstone, Portfolio, and Interview

## Thesis

A strong portfolio demonstrates working systems, measured quality, honest failure analysis, and defensible tradeoffs. This file expands the chapter beyond the basic lesson and connects it to current practice, project work, and verifiable sources.

## Core Concepts

### `capstone`

The integrated project that proves your ability to connect concepts into a working AI system. A capstone turns learning into evidence that can be reviewed by others.

Verification: Ship a runnable project with architecture, tests, metrics, failure analysis, and references.

### `architecture pack`

A set of diagrams and documents explaining system design. It lets reviewers understand APIs, data flow, deployment, security, and operations.

Verification: Include API, data, sequence, deployment, and threat diagrams.

### `evaluation report`

A document summarizing datasets, metrics, results, failures, and release recommendation. It turns quality claims into reviewable evidence.

Verification: Report metrics, failure categories, and representative traces.

### `demo script`

A repeatable sequence showing system behavior and edge cases. It makes demos reliable and prevents hiding critical paths.

Verification: Include ingestion, supported answer, unsupported answer, eval run, and security case.

### `system design`

The structured explanation of requirements, architecture, data, reliability, security, and tradeoffs. It demonstrates senior-level reasoning beyond code snippets.

Verification: Practice drawing and defending the capstone end to end.

### `STAR story`

A behavioral interview structure: Situation, Task, Action, Result. It turns project work into clear interview narratives.

Verification: Prepare STAR stories for failure, tradeoff, incident, and collaboration cases.

### `tradeoff`

A decision where improving one dimension costs another. AI systems constantly trade quality, latency, cost, privacy, and complexity.

Verification: Document alternatives, constraints, evidence, and consequences.

### `portfolio README`

The public entry document explaining the project, usage, architecture, results, and limitations. It determines whether others can understand and trust the work.

Verification: Include setup, architecture, eval report, sources, limitations, and roadmap.


## Implementation Blueprint

Build this chapter as part of the capstone, not as isolated reading. The implementation should produce one or more concrete artifacts: code, schema, benchmark, trace, rubric, threat model, release manifest, or architecture document.

Recommended workflow:

1. Define the exact problem this chapter solves in the capstone.
2. Identify the data or request path affected by `capstone`, `architecture pack`, `evaluation report`, `demo script`, `system design`, `STAR story`, `tradeoff`, `portfolio README`.
3. Create a minimal artifact that can be reviewed.
4. Add failure cases before adding complexity.
5. Add measurements, logs, traces, or human review.
6. Document the decision with numbered references.

## Current Engineering Problems To Study

- Many portfolios show only success paths and omit evaluation or failure cases.
- Interview answers fail when candidates cannot connect implementation decisions to metrics.
- Open-source quality requires runnable docs, source references, and transparent limitations.

## Production Failure Modes

Each failure below names the concept, the way it shows up in production, and the check that would have caught it earlier. Treat this section as the source for regression tests and runbook entries.

- `capstone` — failure: The project shows only a happy-path demo with no evals, limitations, or source references. Mitigation check: Ship a runnable project with architecture, tests, metrics, failure analysis, and references.
- `architecture pack` — failure: The project cannot be reviewed because architecture is implicit in code. Mitigation check: Include API, data, sequence, deployment, and threat diagrams.
- `evaluation report` — failure: Only average score is shown with no failed examples. Mitigation check: Report metrics, failure categories, and representative traces.
- `demo script` — failure: The demo only shows one successful query. Mitigation check: Include ingestion, supported answer, unsupported answer, eval run, and security case.
- `system design` — failure: The design ignores failure modes and operational constraints. Mitigation check: Practice drawing and defending the capstone end to end.
- `STAR story` — failure: A project story lists tools but not impact or decisions. Mitigation check: Prepare STAR stories for failure, tradeoff, incident, and collaboration cases.
- `tradeoff` — failure: The design claims one approach is best with no context. Mitigation check: Document alternatives, constraints, evidence, and consequences.
- `portfolio README` — failure: The README has buzzwords but no runnable instructions or metrics. Mitigation check: Include setup, architecture, eval report, sources, limitations, and roadmap.

## Project Directions

- Build the full capstone and document how to run, test, evaluate, and inspect it.
- Create an architecture pack with API, data, RAG, agent, deployment, and threat diagrams.
- Write a public portfolio README with limitations, tradeoffs, metrics, and source references.

## Verification Artifacts

- A short concept summary with citations.
- A capstone artifact that uses at least three chapter concepts.
- A test, metric, evaluation, or review checklist.
- A failure analysis table.
- A decision record comparing at least two alternatives.
- A reference section using `[1]`, `[2]` style citations.

## How This Chapter Connects To The Capstone

In the capstone, this chapter should leave a visible artifact. Examples include a module, schema, benchmark, design memo, evaluation result, threat model, release manifest, or demo step. Do not mark the chapter complete until the artifact is connected to the capstone.

## References

[1] OpenAI Cookbook: https://github.com/openai/openai-cookbook
[2] LangGraph GitHub: https://github.com/langchain-ai/langgraph
[3] LlamaIndex GitHub: https://github.com/run-llama/llama_index
[4] RAG Techniques GitHub: https://github.com/NirDiamant/RAG_Techniques
[5] DeepEval GitHub: https://github.com/confident-ai/deepeval
[6] RAGAS GitHub: https://github.com/explodinggradients/ragas
