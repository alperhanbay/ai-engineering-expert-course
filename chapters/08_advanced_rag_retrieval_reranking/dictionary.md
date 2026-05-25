# Dictionary: Advanced RAG, Retrieval, and Reranking

Use this dictionary at the end of the chapter. Add your own examples in `my_work/dictionary_notes.md`.

| Term | Working Definition | Why It Matters | Common Failure Mode | Mastery Check |
| --- | --- | --- | --- | --- |
| `query rewrite` | Transforming a user query before retrieval. | It can improve recall for ambiguous, underspecified, or domain-specific questions. | The rewrite changes meaning and retrieves the wrong policy. | Evaluate original vs rewritten queries with retrieval metrics. |
| `multi-query` | Generating multiple query variants for retrieval. | It can improve recall by covering synonyms and perspectives. | Multiple queries add noise and cost without measurable gain. | Compare recall and context precision before enabling. |
| `hybrid search` | Combining dense vector search with lexical or sparse search. | It captures both semantic similarity and exact terms. | BM25 dominates and returns exact but irrelevant matches. | Tune fusion and evaluate by query type. |
| `reranking` | Re-scoring retrieved candidates with a stronger ranking model or method. | It improves final context quality when first-stage retrieval is broad. | Reranking adds latency but does not improve answer quality. | Measure quality gain, latency cost, and failure reduction. |
| `cross-encoder` | A model that scores query-document pairs jointly. | It is often more accurate than bi-encoder retrieval but slower. | Using it on every candidate exceeds latency budget. | Use top-N candidate reranking and compare against baseline. |
| `parent-child retrieval` | Retrieving small child chunks while passing larger parent context to generation. | It balances precise search with enough context for reasoning. | The parent context includes irrelevant neighboring sections. | Evaluate answer support and context precision. |
| `context compression` | Reducing retrieved content before generation. | It saves tokens and can remove noise. | Compression removes a critical exception or qualifier. | Test compressed vs uncompressed outputs on high-risk cases. |
| `query routing` | Sending a request to the appropriate retriever, tool, model, or workflow. | It improves accuracy, cost, and safety by matching task to pipeline. | The router sends a legal citation question to general chat. | Create route labels and evaluate routing confusion. |

## Dictionary Assignment

For each term:

1. Write a one-sentence definition in your own words.
2. Write a concrete example from your capstone (or planned capstone).
3. Write one failure mode you would test against.
4. Write one metric, test, or review check that would catch the failure.
5. Link one source from `references_numbered.md`.

## References

[1] RAG Techniques GitHub: https://github.com/NirDiamant/RAG_Techniques
[2] Awesome RAG GitHub: https://github.com/coree/awesome-rag
[3] Qdrant vector concepts: https://qdrant.tech/documentation/concepts/vectors/
[4] Weaviate hybrid search: https://weaviate.io/developers/weaviate/search/hybrid
[5] FlashRAG paper: https://arxiv.org/abs/2405.13576
[6] RAGLAB paper: https://arxiv.org/abs/2408.11381
