# Deep Dive: Orientation and Expert Roadmap

## Thesis

Expert AI engineering is the discipline of turning model capability into reliable, observable, secure, and useful systems. This file expands the chapter beyond the basic lesson and connects it to current practice, project work, and verifiable sources.

## Core Concepts

### `AI engineering`

The practice of building reliable products around AI models, data, APIs, evaluation, and operations. Without system engineering, model capability remains a demo instead of a dependable service.

Verification: Draw the full system boundary and identify every non-model component required for production.

### `system boundary`

The explicit line separating users, APIs, model providers, data stores, tools, and operations. Clear boundaries make failures, permissions, contracts, and ownership visible.

Verification: Document which components are public contracts and which are replaceable internals.

### `capstone`

The integrated project that proves your ability to connect concepts into a working AI system. A capstone turns learning into evidence that can be reviewed by others.

Verification: Ship a runnable project with architecture, tests, metrics, failure analysis, and references.

### `evidence portfolio`

A collection of code, diagrams, evaluations, logs, and decision records proving competence. Hiring and open-source review both reward verifiable artifacts over claims.

Verification: Map every major skill to a concrete file or demo artifact.

### `failure log`

A structured record of failed cases, root causes, fixes, and follow-up tests. Failures are the fastest path to robust AI systems because aggregate metrics hide edge cases.

Verification: Maintain a table of failures and link each fix to a new test or eval case.

### `decision record`

A concise document explaining an engineering choice, alternatives, tradeoffs, and evidence. AI systems involve many reversible and irreversible tradeoffs that need review.

Verification: Write a decision record for model, vector DB, chunking, reranking, and security choices.

### `source map`

A curated map of official docs, repositories, papers, and standards used for verification. It prevents unsourced claims and makes the course maintainable as tools change.

Verification: Link claims to official docs, active repositories, or primary papers.

### `expert rubric`

A scoring system that distinguishes definition, implementation, evaluation, and production judgment. It prevents shallow completion and makes progress measurable.

Verification: Grade yourself using evidence at concept, implementation, eval, and production levels.


## Implementation Blueprint

Build this chapter as part of the capstone, not as isolated reading. The implementation should produce one or more concrete artifacts: code, schema, benchmark, trace, rubric, threat model, release manifest, or architecture document.

Recommended workflow:

1. Define the exact problem this chapter solves in the capstone.
2. Identify the data or request path affected by `AI engineering`, `system boundary`, `capstone`, `evidence portfolio`, `failure log`, `decision record`, `source map`, `expert rubric`.
3. Create a minimal artifact that can be reviewed.
4. Add failure cases before adding complexity.
5. Add measurements, logs, traces, or human review.
6. Document the decision with numbered references.

## Current Engineering Problems To Study

- Many learners collect tools without building an integrated system.
- Demos hide evaluation, security, latency, and rollback problems.
- A serious portfolio needs evidence, not only screenshots.

## Production Failure Modes

Each failure below names the concept, the way it shows up in production, and the check that would have caught it earlier. Treat this section as the source for regression tests and runbook entries.

- `AI engineering` — failure: The team optimizes a prompt while ignoring retrieval, logging, access control, and evaluation. Mitigation check: Draw the full system boundary and identify every non-model component required for production.
- `system boundary` — failure: A client depends on an internal vector DB schema and breaks when retrieval changes. Mitigation check: Document which components are public contracts and which are replaceable internals.
- `capstone` — failure: The project shows only a happy-path demo with no evals, limitations, or source references. Mitigation check: Ship a runnable project with architecture, tests, metrics, failure analysis, and references.
- `evidence portfolio` — failure: The README says 'production-ready' but provides no traces, tests, or quality report. Mitigation check: Map every major skill to a concrete file or demo artifact.
- `failure log` — failure: Repeated hallucinations are fixed ad hoc and never added to regression tests. Mitigation check: Maintain a table of failures and link each fix to a new test or eval case.
- `decision record` — failure: A vector DB is chosen because it is popular, not because it met measured requirements. Mitigation check: Write a decision record for model, vector DB, chunking, reranking, and security choices.
- `source map` — failure: The curriculum cites blog summaries while official APIs have changed. Mitigation check: Link claims to official docs, active repositories, or primary papers.
- `expert rubric` — failure: A learner marks a chapter complete after reading definitions only. Mitigation check: Grade yourself using evidence at concept, implementation, eval, and production levels.

## Project Directions

- Build a public-style learning roadmap with evidence checkpoints.
- Write a capstone proposal with data, users, risks, and success metrics.
- Create a decision log template and use it for the first five architecture choices.

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

[1] OpenAI platform documentation: https://platform.openai.com/docs
[2] LangGraph overview: https://docs.langchain.com/oss/python/langgraph/overview
[3] LlamaIndex RAG overview: https://developers.llamaindex.ai/python/framework/understanding/rag/
[4] OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
