# Quiz: Embeddings and Vector Search

## Multiple Choice

1. What is an embedding?
   - A. A numeric representation of data
   - B. A SQL index only
   - C. A Docker image
   - D. A human-written citation

2. Why is metadata filtering important in regulated RAG?
   - A. It only changes UI colors
   - B. It helps enforce relevance and access control
   - C. It replaces authentication
   - D. It removes the need for evaluation

3. What does Recall@k measure?
   - A. Whether relevant items appear in the top k results
   - B. How much a model costs
   - C. How long a prompt is
   - D. Whether JSON is valid

4. Why use hybrid search?
   - A. To combine exact keyword signals with semantic vector signals
   - B. To remove all metadata
   - C. To make every query slower for no reason
   - D. To avoid citations

5. Which is a vector similarity search library rather than a full database product?
   - A. FAISS
   - B. PostgreSQL table only
   - C. GitHub Actions
   - D. pytest

## Fill in the Blanks

1. Top-k retrieval returns the k most ________ candidates.
2. Dense retrieval uses embeddings; sparse retrieval often uses ________ signals.
3. HNSW is an approximate nearest neighbor ________ type.
4. Embedding model selection should be evaluated on your own ________.
5. Re-embedding may be required when changing the embedding ________.

## Short Answer

1. Explain the difference between FAISS and Qdrant.
2. Why can increasing top-k both help and hurt RAG quality?
3. Give three metadata fields that matter for access control.

## Answer Key

### Multiple Choice

1. A
2. B
3. A
4. A
5. A

### Fill in the Blanks

1. similar
2. keyword
3. index
4. queries
5. model

