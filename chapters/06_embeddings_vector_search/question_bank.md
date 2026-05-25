# Expanded Question Bank: Embeddings and Vector Search

## How To Use This Bank

Answer without looking at the answer key. For every wrong answer, write one sentence explaining the concept in your own words and one sentence explaining how it appears in a production AI system.


## Multiple Choice

1. Pick the description of `embedding` you would put in a `dictionary.md` entry.
   - A. Hierarchical Navigable Small World, a graph-based approximate nearest neighbor index.
   - B. A numeric representation of text or other data used for similarity search.
   - C. A similarity measure based on the angle between vectors.
   - D. A vector similarity score based on element-wise multiplication and summation.

2. Which sentence is the best working definition of `cosine similarity`?
   - A. A similarity measure based on the angle between vectors.
   - B. A numeric representation of text or other data used for similarity search.
   - C. A vector similarity score based on element-wise multiplication and summation.
   - D. Hierarchical Navigable Small World, a graph-based approximate nearest neighbor index.

3. In production AI work, what is the primary role of `dot product`?
   - A. A numeric representation of text or other data used for similarity search.
   - B. A similarity measure based on the angle between vectors.
   - C. Hierarchical Navigable Small World, a graph-based approximate nearest neighbor index.
   - D. A vector similarity score based on element-wise multiplication and summation.

4. A teammate asks you to define `HNSW` in one sentence. Which is closest?
   - A. A similarity measure based on the angle between vectors.
   - B. A vector similarity score based on element-wise multiplication and summation.
   - C. Hierarchical Navigable Small World, a graph-based approximate nearest neighbor index.
   - D. A numeric representation of text or other data used for similarity search.

5. Pick the description of `IVF` you would put in a `dictionary.md` entry.
   - A. A vector similarity score based on element-wise multiplication and summation.
   - B. Inverted File index that partitions vector space into clusters for approximate search.
   - C. A numeric representation of text or other data used for similarity search.
   - D. A similarity measure based on the angle between vectors.

6. Which sentence is the best working definition of `PQ`?
   - A. Product Quantization, a compression technique for vectors.
   - B. A numeric representation of text or other data used for similarity search.
   - C. A similarity measure based on the angle between vectors.
   - D. A vector similarity score based on element-wise multiplication and summation.

7. In production AI work, what is the primary role of `metadata filter`?
   - A. A numeric representation of text or other data used for similarity search.
   - B. A similarity measure based on the angle between vectors.
   - C. A vector similarity score based on element-wise multiplication and summation.
   - D. A predicate restricting retrieval by fields such as tenant, type, date, or permission.

8. A teammate asks you to define `Recall@k` in one sentence. Which is closest?
   - A. A similarity measure based on the angle between vectors.
   - B. A vector similarity score based on element-wise multiplication and summation.
   - C. The fraction of queries where a relevant item appears in the top k results.
   - D. A numeric representation of text or other data used for similarity search.

9. Pick the description of `MRR` you would put in a `dictionary.md` entry.
   - A. A vector similarity score based on element-wise multiplication and summation.
   - B. Mean Reciprocal Rank, measuring how high the first relevant result appears.
   - C. A numeric representation of text or other data used for similarity search.
   - D. A similarity measure based on the angle between vectors.

10. Which sentence is the best working definition of `NDCG`?
   - A. Normalized Discounted Cumulative Gain, a ranking metric with graded relevance.
   - B. A numeric representation of text or other data used for similarity search.
   - C. A similarity measure based on the angle between vectors.
   - D. A vector similarity score based on element-wise multiplication and summation.


## Applied Multiple Choice

1. Applied case: Popular embedding models may underperform on domain-specific terminology.
   - A. Hard-code the new behaviour for the first failing case and call it a fix.
   - B. Ship the change without measurement because the most recent demo looked good.
   - C. Remove logging and evaluation to keep the diff small and merge faster.
   - D. Set up a controlled experiment isolating `embedding`, capture before/after numbers, and write the result to a decision record.

2. Applied case: Filtering after retrieval can create privacy risk and misleading metrics.
   - A. Remove logging and evaluation to keep the diff small and merge faster.
   - B. Assume the largest available model will mask the underlying weakness in `embedding` so no system change is needed.
   - C. Add the work to the capstone as a reviewable artifact that exercises `cosine similarity` end-to-end, with tests and a trace.
   - D. Ship the change without measurement because the most recent demo looked good.

3. Applied case: Index migrations can silently break retrieval unless they are versioned and evaluated.
   - A. Skip the rollback plan; staging is close enough to production.
   - B. Define explicit acceptance criteria, rollback steps, and a reviewer checklist tied to Embeddings and Vector Search.
   - C. Remove logging and evaluation to keep the diff small and merge faster.
   - D. Assume the largest available model will mask the underlying weakness in `embedding` so no system change is needed.

4. Applied case: Benchmark vector-only, keyword-only, and hybrid retrieval on a labeled dataset.
   - A. Compare at least two approaches against a labelled set covering `NDCG`, then choose on measured quality, latency, cost, and risk.
   - B. Assume the largest available model will mask the underlying weakness in `embedding` so no system change is needed.
   - C. Skip the rollback plan; staging is close enough to production.
   - D. Hard-code the new behaviour for the first failing case and call it a fix.

5. Applied case: Create a multi-tenant metadata filter lab and prove unauthorized chunks are never retrieved.
   - A. Skip the rollback plan; staging is close enough to production.
   - B. Hard-code the new behaviour for the first failing case and call it a fix.
   - C. Ship the change without measurement because the most recent demo looked good.
   - D. Write a one-page design memo naming the assumption, the test that would falsify it, and the metric you'd watch in production.

6. Applied case: Write an embedding migration plan with dual indexes, evaluation, and rollback.
   - A. Ship the change without measurement because the most recent demo looked good.
   - B. Remove logging and evaluation to keep the diff small and merge faster.
   - C. Set up a controlled experiment isolating `embedding`, capture before/after numbers, and write the result to a decision record.
   - D. Hard-code the new behaviour for the first failing case and call it a fix.


## Fill In The Blanks

1. On a system review, you find domain terms map poorly and relevant chunks are not retrieved — the underlying chapter concept is ________.
2. It is common in semantic search when vector magnitude should matter less. A common failure looks like: The vector DB uses a metric that does not match the embedding model expectation. The concept is ________.
3. Given the production failure "Scores are misinterpreted because vectors are not normalized.", the concept being misused is ________.
4. To handle situations where it offers fast vector search with tunable recall/latency tradeoffs, the engineering tool you reach for is ________ (watch for: High filter selectivity reduces recall or latency stability.).
5. ________ is best summarised as: Inverted File index that partitions vector space into clusters for approximate search. Verification step: Tune partition/probe settings with Recall@k and latency.
6. On a system review, you find memory improves while recall drops on high-risk queries — the underlying chapter concept is ________.
7. It combines relevance with access control and operational scoping. A common failure looks like: Filtering after retrieval exposes unauthorized candidates in logs or prompts. The concept is ________.
8. Given the production failure "Recall looks good at k=50 but generation only receives top 5.", the concept being misused is ________.
9. To handle situations where it captures ranking quality beyond simple presence, the engineering tool you reach for is ________ (watch for: Correct chunks appear but too low to be used.).
10. ________ is best summarised as: Normalized Discounted Cumulative Gain, a ranking metric with graded relevance. Verification step: Label graded relevance and compare ranking strategies.

## Short Answer

1. What does a healthy log or trace look like for `embedding`? List the fields you would expect.
2. Explain how `cosine similarity` appears in the capstone, what artifact proves it, and what failure mode you would test.
3. If a reviewer asks 'why does `dot product` matter here?', what one-paragraph answer do you give? Include a metric.
4. Describe the smallest experiment that would tell you whether `HNSW` is correctly implemented in your system.
5. When would you intentionally *avoid* using `IVF`? Name a constraint or tradeoff.
6. What does a healthy log or trace look like for `PQ`? List the fields you would expect.
7. Explain how `metadata filter` appears in the capstone, what artifact proves it, and what failure mode you would test.
8. If a reviewer asks 'why does `Recall@k` matter here?', what one-paragraph answer do you give? Include a metric.
9. Describe the smallest experiment that would tell you whether `MRR` is correctly implemented in your system.
10. When would you intentionally *avoid* using `NDCG`? Name a constraint or tradeoff.

## Scenario Questions

1. On-call triage: Popular embedding models may underperform on domain-specific terminology. Walk through the first three steps you would take.
2. Incident: Filtering after retrieval can create privacy risk and misleading metrics. What do you inspect first, and which metric would prove the fix?
3. Design review: Index migrations can silently break retrieval unless they are versioned and evaluated. Which artifact would you require before approving?
4. An engineer disables `dot product` to mitigate latency. Quality drops the next day. What evidence reverses the decision?

## Practical Debug Questions

1. What log or trace fields would help you debug a failure in `embedding` in this chapter's context?
2. What single metric would you watch in production when changing `PQ`?
3. You suspect `NDCG` is degraded. Design the smallest experiment that would falsify or confirm it in under an hour.
4. For the failure 'Popular embedding models may underperform on domain-specific terminology.', sketch a rollback plan with a clear restore-point definition.
5. What artifact would you put in a portfolio README to prove competence with `embedding`, `cosine similarity`, `dot product`?

## Answer Key

### Multiple Choice

1. B
2. A
3. D
4. C
5. B
6. A
7. D
8. C
9. B
10. A

### Applied Multiple Choice

1. D
2. C
3. B
4. A
5. D
6. C

### Fill In The Blanks

1. embedding
2. cosine similarity
3. dot product
4. HNSW
5. IVF
6. PQ
7. metadata filter
8. Recall@k
9. MRR
10. NDCG

Short-answer, scenario, and debug questions should be graded against the rubric in `../../syllabus/evaluation_rubric.md`.

## References

[1] Qdrant search documentation: https://qdrant.tech/documentation/search/
[2] Qdrant indexing documentation: https://qdrant.tech/documentation/manage-data/indexing/
[3] Milvus documentation: https://milvus.io/docs/
[4] Weaviate hybrid search: https://weaviate.io/developers/weaviate/search/hybrid
[5] FAISS index guidelines: https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index
[6] pgvector GitHub: https://github.com/pgvector/pgvector
