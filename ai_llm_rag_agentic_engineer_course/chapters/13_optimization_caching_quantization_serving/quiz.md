# Quiz: Optimization, Caching, Quantization, and Serving

## Multiple Choice

1. What should you do before optimizing?
   - A. Measure the baseline
   - B. Randomly change models
   - C. Remove evaluation
   - D. Delete logs

2. What does streaming mainly improve?
   - A. Perceived latency
   - B. SQL schema quality
   - C. Authentication
   - D. Index versioning

3. What is KV-cache used for?
   - A. Reusing attention states during generation
   - B. Storing SQL tables
   - C. Rendering UI
   - D. Running Git commits

4. What is a risk of quantization?
   - A. Quality degradation
   - B. More citations
   - C. Better SQL joins
   - D. Guaranteed accuracy

5. Which serving framework is associated with high-throughput LLM serving?
   - A. vLLM
   - B. pytest
   - C. Alembic only
   - D. Makefile only

## Fill in the Blanks

1. A latency budget breaks total request time into ________.
2. Prompt caching is best for repeated static prompt ________.
3. Batching can improve throughput but may increase per-request ________.
4. ONNX is often useful for smaller classifiers, rerankers, or ________ models.
5. Optimization should be evaluated for both speed and ________.

## Short Answer

1. Explain prompt caching vs KV-cache.
2. Compare hosted API, vLLM, TGI, and Triton.
3. When would you optimize a router with a small ONNX classifier?

## Answer Key

### Multiple Choice

1. A
2. A
3. A
4. A
5. A

### Fill in the Blanks

1. components
2. prefixes
3. latency
4. embedding
5. quality

