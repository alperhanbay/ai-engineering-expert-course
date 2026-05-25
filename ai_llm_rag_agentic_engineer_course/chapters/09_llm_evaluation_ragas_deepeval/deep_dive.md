# Deep Dive: LLM and RAG Evaluation

## Thesis

Evaluation is the control system for quality, safety, and release confidence. This file expands the chapter beyond the basic lesson and connects it to current practice, project work, and verifiable sources.

## Core Concepts

### `golden dataset`

A curated set of test cases with expected behavior and reference evidence. It provides regression protection for prompts, models, indexes, and retrievers.

Verification: Build versioned cases with question, expected answer, reference chunks, and risk level.

### `faithfulness`

Whether generated claims are supported by provided context. It is a key hallucination-control metric for RAG.

Verification: Score outputs against retrieved context and inspect failures.

### `answer relevance`

Whether the answer addresses the user's question. A faithful answer can still be incomplete or off-task.

Verification: Evaluate alignment between question and answer.

### `context precision`

How much of the retrieved context is actually relevant. Low precision increases noise, cost, and hallucination risk.

Verification: Measure relevance of retrieved chunks used for generation.

### `context recall`

Whether the necessary evidence was retrieved. Low recall means the model lacks the facts needed to answer.

Verification: Use reference context IDs in the golden dataset.

### `human review`

Structured expert evaluation of model or system behavior. It calibrates automated metrics and catches domain-specific risk.

Verification: Create a rubric and convert review outcomes into eval cases.

### `regression gate`

A release check that blocks quality, safety, or latency regressions. It protects production from prompt/model/index changes.

Verification: Define thresholds and required manual review for high-risk failures.

### `failure taxonomy`

A classification scheme for errors and defects. It turns failures into actionable improvement areas.

Verification: Categorize failures by retrieval, generation, citation, safety, tool, and data.


## Implementation Blueprint

Build this chapter as part of the capstone, not as isolated reading. The implementation should produce one or more concrete artifacts: code, schema, benchmark, trace, rubric, threat model, release manifest, or architecture document.

Recommended workflow:

1. Define the exact problem this chapter solves in the capstone.
2. Identify the data or request path affected by `golden dataset`, `faithfulness`, `answer relevance`, `context precision`, `context recall`, `human review`, `regression gate`, `failure taxonomy`.
3. Create a minimal artifact that can be reviewed.
4. Add failure cases before adding complexity.
5. Add measurements, logs, traces, or human review.
6. Document the decision with numbered references.

## Current Engineering Problems To Study

- Aggregate scores hide failure categories that matter to users.
- LLM-as-judge metrics need calibration against human review.
- Evaluation must cover retrieval, generation, citations, tools, and safety.

## Production Failure Modes

Each failure below names the concept, the way it shows up in production, and the check that would have caught it earlier. Treat this section as the source for regression tests and runbook entries.

- `golden dataset` — failure: A new prompt feels better but silently breaks old high-risk cases. Mitigation check: Build versioned cases with question, expected answer, reference chunks, and risk level.
- `faithfulness` — failure: The answer is relevant but includes unsupported details. Mitigation check: Score outputs against retrieved context and inspect failures.
- `answer relevance` — failure: The model cites context but answers a different question. Mitigation check: Evaluate alignment between question and answer.
- `context precision` — failure: The prompt includes many weakly related chunks. Mitigation check: Measure relevance of retrieved chunks used for generation.
- `context recall` — failure: The correct statute section never reaches the prompt. Mitigation check: Use reference context IDs in the golden dataset.
- `human review` — failure: Experts leave comments but no score or failure category. Mitigation check: Create a rubric and convert review outcomes into eval cases.
- `regression gate` — failure: A new reranker lowers latency but hurts citation correctness. Mitigation check: Define thresholds and required manual review for high-risk failures.
- `failure taxonomy` — failure: All bad answers are labeled 'hallucination' even when retrieval failed. Mitigation check: Categorize failures by retrieval, generation, citation, safety, tool, and data.

## Project Directions

- Create a 100-case golden dataset with expected answer, reference context, and risk level.
- Build a RAG evaluation runner that stores traces, metrics, failures, and release recommendation.
- Design a human review workflow that turns expert feedback into new eval cases.

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

[1] RAGAS metrics: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/
[2] RAGAS GitHub: https://github.com/explodinggradients/ragas
[3] DeepEval documentation: https://deepeval.com/docs/introduction
[4] DeepEval GitHub: https://github.com/confident-ai/deepeval
[5] LangSmith evaluation concepts: https://docs.langchain.com/langsmith/evaluation-concepts
[6] RAGAS paper: https://arxiv.org/abs/2309.15217
[7] ARES paper: https://arxiv.org/abs/2311.09476
