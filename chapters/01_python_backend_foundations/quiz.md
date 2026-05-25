# Quiz: Python Backend Foundations

## Multiple Choice

1. Why should API routes not contain the full RAG pipeline?
   - A. Python does not allow it
   - B. It makes the system hard to test, replace, and maintain
   - C. FastAPI cannot call LLMs
   - D. Vector databases require it

2. What is the main purpose of a repository layer?
   - A. Store CSS files
   - B. Hide data-access details behind a stable interface
   - C. Replace all tests
   - D. Generate embeddings

3. When is async Python most useful in an AI service?
   - A. Waiting on network I/O
   - B. Multiplying large matrices locally
   - C. Making CPU-bound parsing faster automatically
   - D. Replacing validation

4. Which error should usually be handled differently from a provider timeout?
   - A. NoRelevantContextError
   - B. ProviderTimeoutError
   - C. ExternalDependencyError
   - D. HTTP 503

5. Why are type hints useful?
   - A. They make every program faster
   - B. They document contracts and help static analysis
   - C. They remove the need for tests
   - D. They replace logging

## Fill in the Blanks

1. The service layer contains business ________.
2. Pydantic provides runtime input and output ________.
3. Provider classes help isolate external dependencies such as LLMs and ________ stores.
4. Unit tests validate code behavior, while eval tests validate model or pipeline ________.
5. A request log should include a request ID so events can be ________.

## Short Answer

1. Explain the difference between a repository and a provider.
2. Give three fields that should appear in a RAG request log.
3. Why should `NoRelevantContextError` not be treated the same as a server crash?

## Answer Key

### Multiple Choice

1. B
2. B
3. A
4. A
5. B

### Fill in the Blanks

1. logic
2. validation
3. vector
4. quality
5. correlated

