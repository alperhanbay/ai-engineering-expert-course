# Dictionary: Embeddings and Vector Search

Use this dictionary at the end of the chapter. Add your own examples in `my_work/dictionary_notes.md`.

| Term | Working Definition | Why It Matters | Common Failure Mode | Mastery Check |
| --- | --- | --- | --- | --- |
| `embedding` | A numeric representation of text or other data used for similarity search. | Embeddings enable semantic retrieval over large corpora. | Domain terms map poorly and relevant chunks are not retrieved. | Benchmark embeddings on your own labeled retrieval cases. |
| `cosine similarity` | A similarity measure based on the angle between vectors. | It is common in semantic search when vector magnitude should matter less. | The vector DB uses a metric that does not match the embedding model expectation. | Verify the distance metric recommended for the embedding model. |
| `dot product` | A vector similarity score based on element-wise multiplication and summation. | Some embedding systems are optimized for dot-product search. | Scores are misinterpreted because vectors are not normalized. | Document metric choice and score interpretation. |
| `HNSW` | Hierarchical Navigable Small World, a graph-based approximate nearest neighbor index. | It offers fast vector search with tunable recall/latency tradeoffs. | High filter selectivity reduces recall or latency stability. | Evaluate recall and latency under your metadata filters. |
| `IVF` | Inverted File index that partitions vector space into clusters for approximate search. | It can improve scale by searching selected partitions. | Too few probes miss relevant vectors. | Tune partition/probe settings with Recall@k and latency. |
| `PQ` | Product Quantization, a compression technique for vectors. | It reduces memory but can reduce retrieval accuracy. | Memory improves while recall drops on high-risk queries. | Compare exact or high-precision baseline against PQ results. |
| `metadata filter` | A predicate restricting retrieval by fields such as tenant, type, date, or permission. | It combines relevance with access control and operational scoping. | Filtering after retrieval exposes unauthorized candidates in logs or prompts. | Apply filters inside the retrieval system and test cross-tenant cases. |
| `Recall@k` | The fraction of queries where a relevant item appears in the top k results. | It measures whether retrieval finds necessary evidence. | Recall looks good at k=50 but generation only receives top 5. | Measure Recall@k at the same k used by context packing. |
| `MRR` | Mean Reciprocal Rank, measuring how high the first relevant result appears. | It captures ranking quality beyond simple presence. | Correct chunks appear but too low to be used. | Use MRR when first relevant rank matters for context selection. |
| `NDCG` | Normalized Discounted Cumulative Gain, a ranking metric with graded relevance. | It is useful when relevance is not binary. | A somewhat relevant chunk outranks a highly relevant source. | Label graded relevance and compare ranking strategies. |

<!-- HAND-AUTHORED: do not regenerate -->
## Extended Glossary

Additional terms used in this chapter, each with a concise definition and an authoritative source.

- **Cosine similarity / dot product / L2** — vector similarity metrics; use the one your embedding model was trained for. Source: [pgvector](https://github.com/pgvector/pgvector)
- **Normalization** — scaling vectors to unit length; makes cosine and dot product agree. Source: [Sentence-Transformers](https://www.sbert.net/)
- **ANN (approximate nearest neighbour)** — trading a little recall for large speed gains at scale. Source: [FAISS wiki](https://github.com/facebookresearch/faiss/wiki)
- **HNSW** — graph-based ANN index; tune m / ef_search. Source: [Malkov & Yashunin, 2016](https://arxiv.org/abs/1603.09320)
- **IVF / PQ** — inverted-file partitioning / product quantization for scale and memory. Source: [FAISS index guidelines](https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index)
- **Recall@k / MRR / NDCG / Precision@k** — retrieval-quality metrics; measure Recall@k at the production k. Source: [Sebastian Hofstätter, IR metrics](https://github.com/sebastian-hofstaetter/teaching)
- **BM25** — the classic lexical ranking function. Source: [Wikipedia, Okapi BM25](https://en.wikipedia.org/wiki/Okapi_BM25)
- **Hybrid search** — fusing dense and lexical retrieval. Source: [Weaviate hybrid search](https://weaviate.io/developers/weaviate/search/hybrid)
- **Reciprocal Rank Fusion (RRF)** — combining ranked lists without comparable scores. Source: [Cormack et al., 2009](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf)
- **Metadata filter** — a predicate (tenant/access/date) applied during retrieval. Source: [Qdrant filtering](https://qdrant.tech/documentation/concepts/filtering/)
- **MTEB** — benchmark for comparing embedding models. Source: [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard)

## Dictionary Assignment

For each term:

1. Write a one-sentence definition in your own words.
2. Write a concrete example from your capstone (or planned capstone).
3. Write one failure mode you would test against.
4. Write one metric, test, or review check that would catch the failure.
5. Link one source from `references_numbered.md`.

## References

[1] Qdrant search documentation: https://qdrant.tech/documentation/search/
[2] Qdrant indexing documentation: https://qdrant.tech/documentation/manage-data/indexing/
[3] Milvus documentation: https://milvus.io/docs/
[4] Weaviate hybrid search: https://weaviate.io/developers/weaviate/search/hybrid
[5] FAISS index guidelines: https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index
[6] pgvector GitHub: https://github.com/pgvector/pgvector
