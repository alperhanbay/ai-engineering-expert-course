# Lesson: Embeddings and Vector Search

## 1. What Embeddings Are

An embedding is a numeric representation of data. For text, embeddings map sentences, paragraphs, or documents into vectors so that semantically similar texts are close in vector space.

Example:

```text
"claim deadline" and "time limit for filing a claim"
```

These may use different words but represent related meaning. Embeddings help retrieve them.

## 2. Similarity

Common similarity/distance choices:

- cosine similarity;
- dot product;
- Euclidean distance.

The correct choice depends on the embedding model and vector database configuration.

## 3. Vector Search

Naive exact nearest-neighbor search compares the query vector with every stored vector. This becomes expensive at scale. Vector databases use approximate nearest neighbor methods to search faster.

Common index ideas:

- HNSW;
- IVF;
- PQ;
- flat/exact search;
- hybrid sparse+dense search.

## 4. Vector Database vs Vector Library

FAISS is a vector similarity search library. It is powerful but does not provide all database features by itself.

Vector databases such as Qdrant, Milvus, Weaviate, Chroma, and pgvector provide higher-level features:

- collections;
- metadata/payload;
- filtering;
- persistence;
- APIs;
- replication or distributed deployment depending on product;
- operational tooling.

## 5. Metadata Filtering

Metadata filtering limits search to eligible records.

Examples:

- tenant ID;
- document type;
- user permission group;
- date range;
- jurisdiction;
- language;
- source system.

In regulated systems, filtering is not just relevance optimization. It is a security requirement.

## 6. Top-k Retrieval

Top-k means returning the k most similar candidates.

Tradeoff:

- low k: faster, less context, higher miss risk;
- high k: better recall, more noise, higher reranking/generation cost.

## 7. Retrieval Metrics

Important metrics:

| Metric | Meaning |
| --- | --- |
| Recall@k | whether the correct item appears in the top k |
| Precision@k | how many returned items are relevant |
| MRR | how high the first relevant item appears |
| NDCG | ranking quality with graded relevance |
| latency | how fast retrieval completes |

## 8. Embedding Model Selection

Consider:

- language support;
- domain vocabulary;
- embedding dimension;
- cost;
- latency;
- hosted vs self-hosted;
- privacy constraints;
- benchmark performance;
- reranker compatibility.

Do not choose based only on popularity. Evaluate on your own queries.

## 9. Hybrid Search

Dense vector search captures semantic similarity. Keyword search captures exact terms, IDs, citations, legal phrases, product codes, and abbreviations.

Hybrid search combines both.

It is especially important when:

- exact terms matter;
- domain language is specialized;
- queries contain numbers or article references;
- abbreviations are common;
- embeddings confuse similar concepts.

## 10. Index Maintenance

Production systems need:

- incremental inserts;
- updates;
- deletes;
- re-embedding strategy;
- index versioning;
- migration plans;
- backfills;
- monitoring for index freshness.

## 11. Key Takeaway

Vector search is not "put text into a vector DB and hope." It is an engineered retrieval system with model choices, indexing tradeoffs, metadata policy, metrics, and operational maintenance.
## Numbered References

[1] Qdrant search documentation: https://qdrant.tech/documentation/search/
[2] Qdrant indexing documentation: https://qdrant.tech/documentation/manage-data/indexing/
[3] Milvus documentation: https://milvus.io/docs/
[4] Weaviate hybrid search: https://weaviate.io/developers/weaviate/search/hybrid
[5] FAISS index guidelines: https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index
[6] pgvector GitHub: https://github.com/pgvector/pgvector
