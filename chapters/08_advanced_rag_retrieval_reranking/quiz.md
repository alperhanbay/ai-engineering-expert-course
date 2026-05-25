# Quiz: Advanced RAG, Retrieval, and Reranking

## Multiple Choice

1. What does a reranker do?
   - A. Reorders retrieved candidates using a more precise scoring method
   - B. Deletes the vector database
   - C. Writes the final UI
   - D. Replaces metadata

2. Why can hybrid search help in legal or policy domains?
   - A. Exact terms, numbers, and references matter
   - B. It removes all keyword matching
   - C. It prevents evaluation
   - D. It disables filtering

3. What is a cross-encoder?
   - A. A model that scores query and document together
   - B. A database migration tool
   - C. A Docker feature
   - D. A prompt template

4. What is parent-child retrieval?
   - A. Retrieve smaller chunks, then provide larger parent context
   - B. Use only one giant chunk
   - C. Delete child documents
   - D. Store vectors in CSS

5. Which metric evaluates ranking quality with graded relevance?
   - A. NDCG
   - B. Token count only
   - C. Docker build time
   - D. HTTP status code

## Fill in the Blanks

1. Query transformation can include rewriting, expansion, decomposition, or ________ retrieval.
2. Reranking usually improves quality but increases ________.
3. Hybrid search combines dense vector search with sparse or ________ search.
4. Incremental indexing avoids rebuilding the entire ________ every time.
5. Context compression can remove important ________ if used carelessly.

## Short Answer

1. Explain when reranking is worth the latency cost.
2. Give an example of query routing in a domain assistant.
3. How would you compare two chunking strategies?

## Answer Key

### Multiple Choice

1. A
2. A
3. A
4. A
5. A

### Fill in the Blanks

1. multi-query
2. latency
3. keyword
4. index
5. nuance

