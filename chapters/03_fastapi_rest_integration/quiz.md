# Quiz: FastAPI, REST, and Integration

## Multiple Choice

1. Why should product clients not depend on the internal vector DB implementation?
   - A. Vector databases are illegal in APIs
   - B. Internal implementation should be replaceable without breaking clients
   - C. REST does not support vectors
   - D. OpenAPI cannot document it

2. Which endpoint is most appropriate for running a RAG question-answer operation?
   - A. `POST /ask`
   - B. `DELETE /ask`
   - C. `GET /delete-all`
   - D. `PATCH /health`

3. What does streaming mainly improve?
   - A. Perceived latency
   - B. Database normalization
   - C. Password hashing
   - D. SQL joins

4. Why should document indexing often be a background job?
   - A. It is always instant
   - B. It can be long-running and should not block one HTTP request
   - C. It does not need status tracking
   - D. It cannot fail

5. Which HTTP status usually fits unauthorized access to a document?
   - A. 200
   - B. 201
   - C. 403
   - D. 503

## Fill in the Blanks

1. FastAPI uses Pydantic for request and response ________.
2. OpenAPI helps document the API ________.
3. Long-running indexing should return a job ________.
4. Streaming complicates output validation and ________ placement.
5. A stable API contract allows internal implementation ________.

## Short Answer

1. What fields should a production RAG API response include?
2. Explain why `500` should not be used for every AI failure.
3. When would you use streaming, and what is one risk?

## Answer Key

### Multiple Choice

1. B
2. A
3. A
4. B
5. C

### Fill in the Blanks

1. validation
2. contract
3. ID
4. citation
5. changes

