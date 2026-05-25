# Quiz: SQL and Data Management

## Multiple Choice

1. Why does SQL remain important when using a vector database?
   - A. SQL always stores the final vector index
   - B. SQL manages metadata, permissions, logs, feedback, and evaluation data
   - C. Vector databases cannot search text
   - D. SQL replaces embeddings

2. What should an embedding metadata table track?
   - A. Only the final answer
   - B. Embedding model, vector ID, index version, and chunk ID
   - C. CSS style names
   - D. Browser history

3. What is the safer approach for tenant isolation?
   - A. Retrieve all chunks and filter in the UI
   - B. Apply tenant/access filters before or during retrieval
   - C. Trust the model to ignore private data
   - D. Remove logging

4. What is the main purpose of a golden dataset?
   - A. Store production passwords
   - B. Provide known test cases for evaluation and regression testing
   - C. Replace all user feedback
   - D. Speed up Docker builds

5. Audit logs are mainly used for:
   - A. compliance and traceability
   - B. prompt creativity
   - C. chunk splitting
   - D. CSS debugging

## Fill in the Blanks

1. SQL often acts as the ________ plane of an AI system.
2. A chunk table should usually reference its parent ________.
3. A golden dataset should be ________ so results can be compared over time.
4. Application logs help debugging; audit logs provide ________ evidence.
5. Data deletion policies must consider raw documents, chunks, embeddings, logs, and ________.

## Short Answer

1. Explain the difference between a document and a chunk.
2. Name five fields you would include in a RAG request table.
3. Why is filtering unauthorized results after retrieval risky?

## Answer Key

### Multiple Choice

1. B
2. B
3. B
4. B
5. A

### Fill in the Blanks

1. control
2. document
3. versioned
4. compliance
5. traces

