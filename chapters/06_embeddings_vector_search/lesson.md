# Lesson: Embeddings and Vector Search for Production Retrieval

## 1. Retrieval Quality Starts Here

A RAG system's answer quality is capped by its retrieval quality. The most capable model in the world cannot answer correctly from context it never received. And retrieval quality is determined long before the search query runs — it starts with how you *represent* text as vectors, how you *index* those vectors, how you *filter* them by metadata, and crucially, whether you *measure* any of it.

This chapter is about representation, indexing, filtering, and measurement. The unifying theme: vector search feels like magic until you measure it, at which point it becomes an engineering problem with knobs, tradeoffs, and failure modes like any other. The teams that ship good RAG are the ones who treat retrieval as a measurable subsystem with its own metrics and regression tests — not as "we plugged in a vector database and it works."

## 2. What an Embedding Is

An embedding is a fixed-length vector of floating-point numbers that represents the *meaning* of a piece of text (or image, or audio). An embedding model is trained so that texts with similar meaning produce vectors that are close together in the vector space, and dissimilar texts produce vectors that are far apart.

The practical consequence: you can search by *meaning* instead of by *keyword*. A query "how long do I have to report a crash?" can retrieve a chunk that says "claims must be filed within 30 days of the incident" even though they share almost no words. That semantic matching is the entire reason vector search exists.

Key properties you must know for engineering:

- **Dimensionality.** Common embedding models output 384, 768, 1024, 1536, or 3072 dimensions. Higher dimensions can capture more nuance but cost more memory and compute. Some models support "Matryoshka" truncation — you can use a prefix of the vector at reduced quality for cheaper storage.
- **The model defines the space.** Two different embedding models produce incompatible vectors. You cannot mix vectors from `text-embedding-3-small` and `bge-large` in the same index and compare them. Changing the embedding model means re-embedding everything (a re-indexing event — chapter 02's `index_version`).
- **Normalisation.** Many models output normalised vectors (unit length); some don't. This determines which distance metric is correct (next section). Getting this wrong silently degrades retrieval.

## 3. Distance Metrics: Cosine, Dot Product, Euclidean

Vector search ranks candidates by a distance (or similarity) metric. The three you'll meet:

- **Cosine similarity** measures the angle between vectors, ignoring magnitude. It's the default for text embeddings because meaning is encoded in direction, not length. Range: -1 (opposite) to 1 (identical).
- **Dot product (inner product)** considers both direction and magnitude. For *normalised* vectors, dot product and cosine give the same ranking. Some models are trained/optimised for dot-product search.
- **Euclidean (L2) distance** measures straight-line distance. Less common for text but used by some models.

The single most important rule: **use the metric the embedding model was trained for.** The model card tells you. If a model expects cosine and you configure your vector store for L2 on unnormalised vectors, retrieval will be subtly wrong — not broken-with-an-error wrong, but quietly-ranking-things-badly wrong, which is worse because nothing alerts you.

```python
# If the model outputs normalised vectors, cosine and dot product agree.
# Verify normalisation once:
import numpy as np
v = embed("test")
assert abs(np.linalg.norm(v) - 1.0) < 1e-3, "vectors are not normalised; check metric config"
```

## 4. Approximate Nearest Neighbour: HNSW, IVF, PQ

Exact nearest-neighbour search (compare the query to every vector) is accurate but scales linearly — fine for 10k vectors, far too slow for 10M. Production vector search uses *approximate* nearest neighbour (ANN) indexes that trade a little recall for a lot of speed.

The three families you'll configure:

- **HNSW (Hierarchical Navigable Small World)** builds a layered graph; search navigates from coarse to fine. It's the most common default (Qdrant, Weaviate, pgvector, FAISS all support it). Tunable: `m` (graph connectivity — higher = better recall, more memory) and `ef_construction`/`ef_search` (search breadth — higher = better recall, slower). Excellent recall/latency tradeoff; higher memory.
- **IVF (Inverted File)** partitions the space into clusters; search probes only the nearest few clusters. Tunable: `nlist` (number of clusters) and `nprobe` (clusters searched). Lower memory than HNSW; recall depends heavily on `nprobe`. Too few probes silently misses relevant vectors.
- **PQ (Product Quantization)** compresses vectors into compact codes, drastically reducing memory at some accuracy cost. Often combined with IVF (IVF-PQ) for billion-scale indexes.

The engineering point: ANN indexes have a recall/latency/memory tradeoff you *tune*, and tuning is meaningless without measurement. "We use HNSW" is not an answer; "we use HNSW with `m=16`, `ef_search=64`, which gives Recall@10 of 0.94 at p95 latency 8ms on our 2M-vector index" is.

## 5. The Metric That Matters: Recall@k (at the Right k)

The defining retrieval metric is **Recall@k**: of the queries for which a relevant chunk exists, what fraction have a relevant chunk in the top-k results. It directly answers "did retrieval find the evidence the model needs?"

The trap that catches almost everyone: measuring Recall@50 when generation only receives the top 5. Recall@50 might be 0.98 — looks great — while Recall@5 (the chunks that actually reach the prompt) is 0.71. The model only ever sees what fits in the context budget. **Always measure Recall@k at the same k you actually pass to generation.**

Companion metrics:

- **MRR (Mean Reciprocal Rank)**: how high the *first* relevant result ranks. Captures "the right chunk was retrieved but ranked 9th, below the cutoff." High Recall@k with low MRR means reranking (chapter 08) will help.
- **NDCG (Normalized Discounted Cumulative Gain)**: a graded-relevance ranking metric for when relevance isn't binary (some chunks are highly relevant, some partly). Use it when you have graded labels.
- **Precision@k**: of the retrieved chunks, how many are relevant. Low precision means noise in the context, which costs tokens and can distract the model (the attention point from chapter 05).

You cannot improve what you don't measure. Building a small labelled retrieval set (queries + the chunk ids that answer them) is the highest-leverage thing in this chapter. Everything else — embedding model choice, hybrid search, reranking — is tuned against that set.

## 6. Lexical, Dense, and Hybrid Search

Dense (vector) search captures semantic similarity but can miss exact matches: a query for a specific policy code `"ART-2024-§7b"` may retrieve semantically related text while missing the exact clause, because rare tokens and identifiers don't embed well.

**Lexical search** (BM25, the classic keyword-ranking algorithm) is the opposite: excellent at exact terms, identifiers, names, and rare words; blind to paraphrase and synonyms.

**Hybrid search** combines both, usually by fusing the two ranked lists. The common fusion method is **Reciprocal Rank Fusion (RRF)**, which combines rankings without needing the scores to be on the same scale:

```
RRF_score(doc) = sum over each ranker of  1 / (k + rank_in_that_ranker)
# k is a constant, commonly 60
```

When hybrid wins: domains with lots of exact identifiers, codes, names, acronyms — legal, medical, finance, technical docs. When dense alone is enough: conversational, paraphrase-heavy queries over prose.

The engineering discipline, again: don't assume hybrid is better. Measure dense-only, lexical-only, and hybrid on your labelled set. Often hybrid wins overall but loses on a query subset; knowing *which* queries each method wins lets you route (chapter 08).

## 7. Metadata Filtering: Where Correctness and Security Meet

Real retrieval is almost never "search all vectors." It's "search the vectors this user is allowed to see, of this document type, effective on this date." Metadata filtering combines relevance with access control and scoping.

The critical correctness rule: **filter during retrieval, not after.** Two designs:

1. **Pre-filter / filtered search** (correct): the vector store applies the metadata predicate as part of the search, so only authorised candidates are ever considered. Qdrant, Weaviate, Milvus, and pgvector all support filtered vector search.
2. **Post-filter** (dangerous): retrieve top-k by vector similarity, then drop the ones the user can't see. This is wrong for two reasons: (a) unauthorised chunks were briefly in your result set and may have been logged, and (b) if 4 of your top-5 were unauthorised, you return 1 result when 5 relevant authorised ones existed below the cutoff — silent recall collapse.

```python
# Filtered search (Qdrant-style): tenant + access filter applied during search
results = await client.search(
    collection_name="chunks",
    query_vector=query_vec,
    query_filter={
        "must": [
            {"key": "tenant_id", "match": {"value": tenant_id}},
            {"key": "access_level", "match": {"any": allowed_levels}},
        ]
    },
    limit=top_k,
)
```

This is where the chapter-02 discipline (`tenant_id` on every chunk, denormalised) pays off: the filter is cheap and correct. The most common multi-tenant data leak in RAG systems is a post-filter design or a missing filter. Test cross-tenant retrieval explicitly and assert zero leakage.

A subtlety: heavily filtered HNSW search can lose recall, because the graph navigation may walk through many filtered-out nodes. Vector stores handle this differently (payload indexes, filterable HNSW). Measure Recall@k *under your real filters*, not on the unfiltered index.

## 8. Chunking's Role in Retrieval

Chunking (covered more in chapter 07) is upstream of embeddings but determines what you can retrieve. The key interactions:

- **Chunk size vs precision/recall.** Small chunks are precise (a retrieved chunk is tightly on-topic) but may not contain enough context to answer; large chunks have context but dilute the embedding (a chunk about ten topics has a muddy "average" vector that matches nothing well).
- **One embedding per chunk represents the whole chunk.** If a chunk covers two distinct facts, its single vector is a compromise that may rank below a chunk that's purely about one of them.
- **Overlap** between chunks preserves continuity across boundaries but increases storage and creates near-duplicate retrievals.

The takeaway for this chapter: chunking strategy is an input to your retrieval benchmark. When you compare embedding models, hold chunking constant; when you compare chunking, hold the embedding model constant. Change one variable at a time or your benchmark tells you nothing.

## 9. Embedding Model Selection

The default (a strong general-purpose model like `text-embedding-3-small/large`) is a reasonable start, but "popular" is not "best for your domain." Domain-specific terminology — legal Latin, medical abbreviations, internal product names — may embed poorly in a general model.

The selection process:

1. Build the labelled retrieval set (section 5).
2. Embed the corpus with each candidate model (general-purpose, a domain-tuned model, maybe a multilingual one if relevant).
3. Measure Recall@k and MRR on the labelled set for each.
4. Factor in dimensionality (storage cost), inference cost/latency, and whether it's hosted or self-hosted.
5. Pick on measured retrieval quality, not leaderboard rank.

Re-embedding is expensive (every chunk, through the model, into a new index), so this is a decision you want to get reasonably right and not churn on. But it's also reversible with discipline: dual indexes and a config-flip cutover (next section).

## 10. Index Migrations Without Downtime

You will change the embedding model or chunking strategy. When you do, the old vectors are incompatible with the new query vectors — it's a full re-index. Done carelessly, this breaks retrieval silently. Done with discipline, it's a config flip.

The dual-index pattern:

1. Build the new index (`index_version = v18`) alongside the live one (`v17`). This runs in the background; production keeps serving from `v17`.
2. Evaluate `v18` against the labelled retrieval set *and* the chapter-09 golden set. Compare to `v17`.
3. If `v18` wins (or ties and is cheaper), flip the `index_version` config so retrieval reads from `v18`. The flip is instant; no downtime.
4. Keep `v17` for a rollback window. If `v18` regresses in production, flip back.
5. After the window, delete `v17`.

The `embeddings` catalog table from chapter 02 (with `index_version`) is what makes this auditable: every answer records which index it used, so a regression is attributable to a specific version.

Never do an in-place re-index of the live index. There's no rollback and a window where retrieval is half-old, half-new and inconsistent.

## 11. Common Mistakes and Anti-Patterns

1. **No labelled retrieval set.** Retrieval is then unmeasurable; every change is a guess.
2. **Recall@k measured at the wrong k.** Looks great at k=50; generation gets k=5.
3. **Wrong distance metric for the model.** Silent quality loss, no error.
4. **Post-filtering for access control.** Leak risk + silent recall collapse.
5. **Mixing vectors from different embedding models in one index.** Meaningless comparisons.
6. **Tuning ANN parameters with no recall measurement.** "We set ef_search=200" with no idea if 64 was already enough — wasted latency.
7. **In-place re-index of the live index.** No rollback, inconsistent window.
8. **Assuming hybrid > dense without measuring.** Sometimes BM25 dominates and returns exact-but-irrelevant matches.
9. **Chunks too large.** Muddy embeddings that match nothing well.
10. **Ignoring recall loss under filtering.** Unfiltered recall is great; the real, filtered recall is poor.

## 12. Production Failure Modes

- **A domain term ("force majeure", a drug name) never retrieves the right clause.** Cause: general embedding model embeds rare domain tokens poorly. Defensive: hybrid search; domain-tuned embeddings; measure per-query-type.
- **A new tenant's documents are retrievable by another tenant.** Cause: missing or post-filter. Defensive: filtered search; nightly cross-tenant leak query (chapter 02 example 5).
- **Recall silently drops after an embedding model "upgrade."** Cause: in-place re-index, no eval. Defensive: dual index + eval gate + config flip.
- **p95 latency triples after enabling heavy metadata filters.** Cause: filtered HNSW walks many filtered nodes. Defensive: payload indexes; measure latency under real filters; consider IVF for high-selectivity filters.
- **The vector store and SQL disagree about which chunks exist.** Cause: a chunk deleted in SQL but not in the vector store. Defensive: the deletion job touches both; a reconciliation query.
- **Memory blows up at 5M vectors.** Cause: HNSW with high `m` and full-precision vectors. Defensive: measure memory per million; consider PQ/quantized vectors or a dedicated store.

## 13. Security and Privacy

1. **Embeddings are derived data and can leak information.** A deleted document's embedding still encodes its content and can be retrieved. Deletion (chapter 02) must remove vectors, not just SQL rows.
2. **Metadata filters are access control.** Treat the filter logic with the same rigor as an authorization check — test it, and prefer enforcing it in the vector store rather than trusting application code alone.
3. **Don't log query vectors with raw query text at default verbosity** if the query contains PII. The vector itself is hard to invert but the paired text isn't.
4. **Multi-tenant isolation is the headline risk.** The single most important test in this chapter is "tenant A can never retrieve tenant B's chunk." Make it a regression test, not a one-time check.

## 14. The Capstone Checklist

By the end of chapter 06, the following should exist in `chapters/06_embeddings_vector_search/my_work/`:

- A labelled retrieval set: at least 50 queries, each with the ground-truth chunk id(s) that answer it, plus a few "no relevant chunk exists" queries.
- A benchmark script comparing at minimum dense-only vs hybrid (and ideally two embedding models) on Recall@1, Recall@5, MRR, and p95 latency — at the k you actually use.
- A `bench_report.md` recommending one configuration with measured deltas and the tradeoffs.
- A metadata-filter test proving cross-tenant retrieval returns zero unauthorised chunks, under filtered search.
- An index migration plan (`migration_plan.md`) using the dual-index + eval + config-flip + rollback pattern.
- A README in `my_work/` documenting the distance metric used and *why* (matched to the embedding model).

If a teammate can run your benchmark, see the recommended config with numbers, and confirm the cross-tenant test passes — without asking you — the chapter is done.

## 15. Key Takeaway

Retrieval quality is the ceiling on RAG quality, and it is fully measurable. Represent text with a model matched to your domain and metric; index with ANN parameters you've tuned against real recall numbers; filter during search for correctness and security; and migrate indexes with dual-index discipline. The labelled retrieval set is the single most valuable artifact you'll build here — everything downstream is tuned against it.

## Numbered References

[1] Qdrant search documentation: https://qdrant.tech/documentation/search/
[2] Qdrant indexing documentation: https://qdrant.tech/documentation/manage-data/indexing/
[3] Milvus documentation: https://milvus.io/docs/
[4] Weaviate hybrid search: https://weaviate.io/developers/weaviate/search/hybrid
[5] FAISS index guidelines: https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index
[6] pgvector GitHub: https://github.com/pgvector/pgvector
