# Dictionary: LLM and RAG Evaluation

Use this dictionary at the end of the chapter. Add your own examples in `my_work/dictionary_notes.md`.

| Term | Working Definition | Why It Matters | Common Failure Mode | Mastery Check |
| --- | --- | --- | --- | --- |
| `golden dataset` | A curated set of test cases with expected behavior and reference evidence. | It provides regression protection for prompts, models, indexes, and retrievers. | A new prompt feels better but silently breaks old high-risk cases. | Build versioned cases with question, expected answer, reference chunks, and risk level. |
| `faithfulness` | Whether generated claims are supported by provided context. | It is a key hallucination-control metric for RAG. | The answer is relevant but includes unsupported details. | Score outputs against retrieved context and inspect failures. |
| `answer relevance` | Whether the answer addresses the user's question. | A faithful answer can still be incomplete or off-task. | The model cites context but answers a different question. | Evaluate alignment between question and answer. |
| `context precision` | How much of the retrieved context is actually relevant. | Low precision increases noise, cost, and hallucination risk. | The prompt includes many weakly related chunks. | Measure relevance of retrieved chunks used for generation. |
| `context recall` | Whether the necessary evidence was retrieved. | Low recall means the model lacks the facts needed to answer. | The correct statute section never reaches the prompt. | Use reference context IDs in the golden dataset. |
| `human review` | Structured expert evaluation of model or system behavior. | It calibrates automated metrics and catches domain-specific risk. | Experts leave comments but no score or failure category. | Create a rubric and convert review outcomes into eval cases. |
| `regression gate` | A release check that blocks quality, safety, or latency regressions. | It protects production from prompt/model/index changes. | A new reranker lowers latency but hurts citation correctness. | Define thresholds and required manual review for high-risk failures. |
| `failure taxonomy` | A classification scheme for errors and defects. | It turns failures into actionable improvement areas. | All bad answers are labeled 'hallucination' even when retrieval failed. | Categorize failures by retrieval, generation, citation, safety, tool, and data. |

## Dictionary Assignment

For each term:

1. Write a one-sentence definition in your own words.
2. Write a concrete example from your capstone (or planned capstone).
3. Write one failure mode you would test against.
4. Write one metric, test, or review check that would catch the failure.
5. Link one source from `references_numbered.md`.

## References

[1] RAGAS metrics: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/
[2] RAGAS GitHub: https://github.com/explodinggradients/ragas
[3] DeepEval documentation: https://deepeval.com/docs/introduction
[4] DeepEval GitHub: https://github.com/confident-ai/deepeval
[5] LangSmith evaluation concepts: https://docs.langchain.com/langsmith/evaluation-concepts
[6] RAGAS paper: https://arxiv.org/abs/2309.15217
[7] ARES paper: https://arxiv.org/abs/2311.09476
