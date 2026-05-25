# Lesson: Advanced RAG, Retrieval, and Reranking

## 1. Why Basic RAG Is Not Enough

Basic RAG often fails when:

- the correct chunk is not retrieved;
- too many irrelevant chunks are retrieved;
- the query uses synonyms;
- exact legal or policy terms matter;
- documents are long and structured;
- multiple sources conflict;
- permissions filter out relevant content;
- the model receives noisy context.

Advanced RAG improves retrieval quality before generation.

## 2. Failure Taxonomy

| Failure | Meaning | Typical fix |
| --- | --- | --- |
| retrieval miss | correct context absent | better chunking, query rewrite, hybrid search |
| low rank | correct context appears too low | reranking |
| context noise | irrelevant chunks included | filtering, reranking, compression |
| stale index | old document retrieved | index freshness monitoring |
| permission miss | relevant but inaccessible content | access model review |
| citation mismatch | answer cites wrong chunk | citation validation |

## 3. Query Transformation

Query transformation modifies the user query before retrieval.

Techniques:

- query rewriting;
- multi-query retrieval;
- hypothetical document expansion;
- acronym expansion;
- domain synonym expansion;
- decomposition into subquestions.

Use with evaluation. Query rewriting can also introduce errors.

## 4. Hybrid Search

Hybrid search combines dense vector search and sparse/keyword search.

Why it helps:

- exact terms matter;
- numbers and article references matter;
- embeddings may blur domain distinctions;
- keyword search catches rare terms.

Example:

```text
dense score + BM25 score -> combined rank
```

## 5. Reranking

Reranking takes candidate chunks from a first-stage retriever and scores them more carefully.

Pipeline:

```text
retrieve top 50
  -> rerank top 50
  -> keep top 5
  -> generate answer
```

### Bi-Encoder

Encodes query and document separately. Fast and scalable.

### Cross-Encoder

Scores query and document together. More accurate but slower.

Use reranking when:

- recall is acceptable but ranking is poor;
- relevance is subtle;
- exact answer must be high in context;
- latency budget allows it.

## 6. Parent-Child Retrieval

Retrieve small child chunks for precision, then pass larger parent context for generation.

This helps when:

- small chunks find exact facts;
- larger context is needed for reasoning;
- citations need structure.

## 7. Context Compression

Context compression reduces retrieved content before generation.

Approaches:

- remove irrelevant sentences;
- summarize retrieved chunks;
- extract answer-bearing spans;
- rerank paragraphs inside documents.

Risk:

- compression can remove important nuance.

## 8. Routing

Query routing sends different queries to different pipelines:

- legal statute search;
- case file search;
- policy search;
- SQL analytics;
- tool-based workflow;
- no-answer/safety route.

Routing can be:

- rule-based;
- classifier-based;
- LLM-based;
- hybrid.

## 9. Incremental Indexing

Production systems need updates without full reindex every time.

Track:

- document version;
- chunk version;
- embedding model;
- index version;
- deleted records;
- stale records;
- backfill jobs.

## 10. Evaluation of Advanced RAG

Compare variants:

- chunk strategy;
- embedding model;
- top-k;
- hybrid weights;
- reranker;
- context compression;
- query rewrite.

Measure:

- Recall@k;
- MRR;
- NDCG;
- context precision;
- faithfulness;
- latency;
- cost.

## 11. Key Takeaway

Advanced RAG is search engineering plus LLM engineering. The model cannot compensate for a weak retrieval system in high-accuracy domains.
## Numbered References

[1] RAG Techniques GitHub: https://github.com/NirDiamant/RAG_Techniques
[2] Awesome RAG GitHub: https://github.com/coree/awesome-rag
[3] Qdrant vector concepts: https://qdrant.tech/documentation/concepts/vectors/
[4] Weaviate hybrid search: https://weaviate.io/developers/weaviate/search/hybrid
[5] FlashRAG paper: https://arxiv.org/abs/2405.13576
[6] RAGLAB paper: https://arxiv.org/abs/2408.11381
