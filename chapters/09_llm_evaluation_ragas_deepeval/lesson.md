# Lesson: LLM and RAG Evaluation

## 1. Why Evaluation Is Central

Production AI cannot be managed by intuition. You need evaluation to answer:

- Did the new prompt improve quality?
- Did the new embedding model improve retrieval?
- Did the index update break old behavior?
- Is the model hallucinating?
- Are citations correct?
- Are users satisfied?
- Are high-risk answers reviewed?

Evaluation turns subjective quality into measurable signals.

## 2. Evaluation Layers

| Layer | Example |
| --- | --- |
| unit tests | parser handles empty document |
| integration tests | API can query vector DB |
| retrieval eval | correct chunk appears in top k |
| generation eval | answer is faithful and relevant |
| agent eval | correct tool chosen and used safely |
| human review | domain expert scores correctness |
| production monitoring | live feedback and drift |

## 3. Golden Dataset

A golden dataset is a set of test cases with known expected behavior.

For RAG, each case should include:

- question;
- expected answer;
- reference context IDs;
- accepted citation sources;
- domain;
- difficulty;
- risk level;
- reviewer;
- dataset version.

Without reference contexts, you cannot reliably measure retrieval recall.

## 4. Retrieval Metrics

### Recall@k

Whether the correct context appears in the top k results.

### Precision@k

How many retrieved results are relevant.

### MRR

How high the first relevant result appears.

### NDCG

Ranking metric that handles graded relevance.

Retrieval metrics should be computed before generation metrics. If retrieval fails, answer generation is already compromised.

## 5. Generation Metrics

Important dimensions:

- faithfulness: answer supported by context;
- relevance: answer addresses the question;
- completeness: answer covers required facts;
- citation correctness;
- safety;
- format correctness;
- refusal/no-answer correctness.

## 6. RAGAS

RAGAS is a framework for evaluating RAG systems. It includes metrics such as faithfulness, answer relevance, context precision, and context recall.

Use RAGAS as a tool, not as an unquestioned truth. Automated evals should be calibrated against human review, especially in domain-specific tasks.

## 7. DeepEval

DeepEval provides test-style LLM evaluation. It can be used for:

- unit-like LLM tests;
- RAG metrics;
- custom criteria;
- regression tests;
- CI integration.

## 8. Human-in-the-Loop Evaluation

Human review is required when:

- domain correctness matters;
- automated metrics are weak;
- risk is high;
- safety or compliance is involved;
- business impact is large.

Human review should be structured:

```text
0 = dangerous or unsupported
1 = mostly wrong
2 = partially correct
3 = correct and cited
4 = correct, cited, nuanced, production-ready
```

## 9. Regression Gates

A regression gate blocks release when quality drops.

Example:

```text
release blocked if:
- faithfulness < 0.85
- context recall < 0.80
- critical human error > 0
- citation correctness < 0.90
- p95 latency > target
```

## 10. Failure Analysis

Do not only compute scores. Read failures.

Common categories:

- retrieval miss;
- wrong rank;
- context noise;
- hallucination;
- wrong citation;
- unsafe answer;
- format failure;
- tool misuse;
- no-answer failure.

## 11. Key Takeaway

Evaluation is the quality control system of AI engineering. It must cover retrieval, generation, agents, safety, human review, and production behavior.
## Numbered References

[1] RAGAS metrics: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/
[2] RAGAS GitHub: https://github.com/explodinggradients/ragas
[3] DeepEval documentation: https://deepeval.com/docs/introduction
[4] DeepEval GitHub: https://github.com/confident-ai/deepeval
[5] LangSmith evaluation concepts: https://docs.langchain.com/langsmith/evaluation-concepts
[6] RAGAS paper: https://arxiv.org/abs/2309.15217
[7] ARES paper: https://arxiv.org/abs/2311.09476
