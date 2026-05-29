# Dictionary: Orientation and Expert Roadmap

Use this dictionary at the end of the chapter. Add your own examples in `my_work/dictionary_notes.md`.

| Term | Working Definition | Why It Matters | Common Failure Mode | Mastery Check |
| --- | --- | --- | --- | --- |
| `AI engineering` | The practice of building reliable products around AI models, data, APIs, evaluation, and operations. | Without system engineering, model capability remains a demo instead of a dependable service. | The team optimizes a prompt while ignoring retrieval, logging, access control, and evaluation. | Draw the full system boundary and identify every non-model component required for production. |
| `system boundary` | The explicit line separating users, APIs, model providers, data stores, tools, and operations. | Clear boundaries make failures, permissions, contracts, and ownership visible. | A client depends on an internal vector DB schema and breaks when retrieval changes. | Document which components are public contracts and which are replaceable internals. |
| `capstone` | The integrated project that proves your ability to connect concepts into a working AI system. | A capstone turns learning into evidence that can be reviewed by others. | The project shows only a happy-path demo with no evals, limitations, or source references. | Ship a runnable project with architecture, tests, metrics, failure analysis, and references. |
| `evidence portfolio` | A collection of code, diagrams, evaluations, logs, and decision records proving competence. | Hiring and open-source review both reward verifiable artifacts over claims. | The README says 'production-ready' but provides no traces, tests, or quality report. | Map every major skill to a concrete file or demo artifact. |
| `failure log` | A structured record of failed cases, root causes, fixes, and follow-up tests. | Failures are the fastest path to robust AI systems because aggregate metrics hide edge cases. | Repeated hallucinations are fixed ad hoc and never added to regression tests. | Maintain a table of failures and link each fix to a new test or eval case. |
| `decision record` | A concise document explaining an engineering choice, alternatives, tradeoffs, and evidence. | AI systems involve many reversible and irreversible tradeoffs that need review. | A vector DB is chosen because it is popular, not because it met measured requirements. | Write a decision record for model, vector DB, chunking, reranking, and security choices. |
| `source map` | A curated map of official docs, repositories, papers, and standards used for verification. | It prevents unsourced claims and makes the course maintainable as tools change. | The curriculum cites blog summaries while official APIs have changed. | Link claims to official docs, active repositories, or primary papers. |
| `expert rubric` | A scoring system that distinguishes definition, implementation, evaluation, and production judgment. | It prevents shallow completion and makes progress measurable. | A learner marks a chapter complete after reading definitions only. | Grade yourself using evidence at concept, implementation, eval, and production levels. |

<!-- HAND-AUTHORED: do not regenerate -->
## Extended Glossary

Additional terms used in this chapter, each with a concise definition and an authoritative source. Definitions are deliberately short; follow the source for depth.

- **MLOps / LLMOps** — the practice of operating ML/LLM systems in production: data, deployment, monitoring, evaluation, and lifecycle management. Source: [Google, Rules of ML](https://developers.google.com/machine-learning/guides/rules-of-ml)
- **SRE (Site Reliability Engineering)** — Google's discipline of running reliable systems using SLOs, error budgets, and incident response. Source: [Google SRE Book](https://sre.google/books/)
- **SLO (Service Level Objective)** — a measurable reliability/performance target (e.g. p95 latency, quality threshold). Source: [SRE Book — SLOs](https://sre.google/sre-book/service-level-objectives/)
- **Architecture Decision Record (ADR)** — a short document capturing one design decision, its alternatives, and rationale. Source: [ADR](https://adr.github.io/)
- **Technical debt (in ML)** — hidden long-term cost from shortcuts; in ML the non-model infrastructure dominates this debt. Source: [Sculley et al., 2015](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html)
- **Drift** — degradation of quality over time from changes in data, users, or model, with no code change. Source: [Google, Rules of ML](https://developers.google.com/machine-learning/guides/rules-of-ml)
- **STAR method** — Situation, Task, Action, Result: a structure for behavioral interview answers. Source: [Wikipedia](https://en.wikipedia.org/wiki/Situation,_task,_action,_result)
- **Twelve-Factor App** — a methodology for building portable, disposable services (config, dependencies, logs). Source: [12factor.net](https://12factor.net/)

## Dictionary Assignment

For each term:

1. Write a one-sentence definition in your own words.
2. Write a concrete example from your capstone (or planned capstone).
3. Write one failure mode you would test against.
4. Write one metric, test, or review check that would catch the failure.
5. Link one source from `references_numbered.md`.

## References

[1] OpenAI platform documentation: https://platform.openai.com/docs
[2] LangGraph overview: https://docs.langchain.com/oss/python/langgraph/overview
[3] LlamaIndex RAG overview: https://developers.llamaindex.ai/python/framework/understanding/rag/
[4] OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
