# Quiz: RAG Pipeline Basics

## Multiple Choice

1. What does RAG stand for?
   - A. Retrieval-Augmented Generation
   - B. Random Answer Generator
   - C. Runtime API Gateway
   - D. Ranked Agent Graph

2. What is the purpose of chunking?
   - A. Split documents into retrievable units
   - B. Delete metadata
   - C. Replace the model
   - D. Train a database

3. Why is no-answer behavior important?
   - A. It prevents the system from forcing unsupported answers
   - B. It removes the need for retrieval
   - C. It guarantees all answers are long
   - D. It disables citations

4. What should a citation include?
   - A. Source and chunk reference
   - B. Only a random URL
   - C. Nothing
   - D. The system prompt

5. Which is part of ingestion?
   - A. Parsing documents
   - B. Cleaning text
   - C. Chunking
   - D. All of the above

## Fill in the Blanks

1. RAG retrieves external ________ before generation.
2. Metadata helps with filtering, permissions, and ________.
3. Chunk overlap preserves continuity but increases ________.
4. A RAG request should log retrieved chunks and their ________.
5. Basic vector retrieval is a starting point, not a complete ________ system.

## Short Answer

1. Explain the difference between ingestion-time and query-time steps.
2. Why can bad PDF parsing harm RAG quality?
3. What makes a citation useful?

## Answer Key

### Multiple Choice

1. A
2. A
3. A
4. A
5. D

### Fill in the Blanks

1. context
2. citations
3. duplication
4. scores
5. expert

