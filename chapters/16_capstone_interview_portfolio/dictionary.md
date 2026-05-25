# Dictionary: Capstone, Portfolio, and Interview

Use this dictionary at the end of the chapter. Add your own examples in `my_work/dictionary_notes.md`.

| Term | Working Definition | Why It Matters | Common Failure Mode | Mastery Check |
| --- | --- | --- | --- | --- |
| `capstone` | The integrated project that proves your ability to connect concepts into a working AI system. | A capstone turns learning into evidence that can be reviewed by others. | The project shows only a happy-path demo with no evals, limitations, or source references. | Ship a runnable project with architecture, tests, metrics, failure analysis, and references. |
| `architecture pack` | A set of diagrams and documents explaining system design. | It lets reviewers understand APIs, data flow, deployment, security, and operations. | The project cannot be reviewed because architecture is implicit in code. | Include API, data, sequence, deployment, and threat diagrams. |
| `evaluation report` | A document summarizing datasets, metrics, results, failures, and release recommendation. | It turns quality claims into reviewable evidence. | Only average score is shown with no failed examples. | Report metrics, failure categories, and representative traces. |
| `demo script` | A repeatable sequence showing system behavior and edge cases. | It makes demos reliable and prevents hiding critical paths. | The demo only shows one successful query. | Include ingestion, supported answer, unsupported answer, eval run, and security case. |
| `system design` | The structured explanation of requirements, architecture, data, reliability, security, and tradeoffs. | It demonstrates senior-level reasoning beyond code snippets. | The design ignores failure modes and operational constraints. | Practice drawing and defending the capstone end to end. |
| `STAR story` | A behavioral interview structure: Situation, Task, Action, Result. | It turns project work into clear interview narratives. | A project story lists tools but not impact or decisions. | Prepare STAR stories for failure, tradeoff, incident, and collaboration cases. |
| `tradeoff` | A decision where improving one dimension costs another. | AI systems constantly trade quality, latency, cost, privacy, and complexity. | The design claims one approach is best with no context. | Document alternatives, constraints, evidence, and consequences. |
| `portfolio README` | The public entry document explaining the project, usage, architecture, results, and limitations. | It determines whether others can understand and trust the work. | The README has buzzwords but no runnable instructions or metrics. | Include setup, architecture, eval report, sources, limitations, and roadmap. |

## Dictionary Assignment

For each term:

1. Write a one-sentence definition in your own words.
2. Write a concrete example from your capstone (or planned capstone).
3. Write one failure mode you would test against.
4. Write one metric, test, or review check that would catch the failure.
5. Link one source from `references_numbered.md`.

## References

[1] OpenAI Cookbook: https://github.com/openai/openai-cookbook
[2] LangGraph GitHub: https://github.com/langchain-ai/langgraph
[3] LlamaIndex GitHub: https://github.com/run-llama/llama_index
[4] RAG Techniques GitHub: https://github.com/NirDiamant/RAG_Techniques
[5] DeepEval GitHub: https://github.com/confident-ai/deepeval
[6] RAGAS GitHub: https://github.com/explodinggradients/ragas
