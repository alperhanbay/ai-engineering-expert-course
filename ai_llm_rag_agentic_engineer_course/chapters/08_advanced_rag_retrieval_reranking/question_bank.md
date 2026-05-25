# Expanded Question Bank: Advanced RAG, Retrieval, and Reranking

## How To Use This Bank

Answer without looking at the answer key. For every wrong answer, write one sentence explaining the concept in your own words and one sentence explaining how it appears in a production AI system.


## Multiple Choice

1. Which sentence is the best working definition of `query rewrite`?
   - A. Transforming a user query before retrieval.
   - B. Generating multiple query variants for retrieval.
   - C. Combining dense vector search with lexical or sparse search.
   - D. Re-scoring retrieved candidates with a stronger ranking model or method.

2. In production AI work, what is the primary role of `multi-query`?
   - A. Transforming a user query before retrieval.
   - B. Combining dense vector search with lexical or sparse search.
   - C. Re-scoring retrieved candidates with a stronger ranking model or method.
   - D. Generating multiple query variants for retrieval.

3. A teammate asks you to define `hybrid search` in one sentence. Which is closest?
   - A. Generating multiple query variants for retrieval.
   - B. Re-scoring retrieved candidates with a stronger ranking model or method.
   - C. Combining dense vector search with lexical or sparse search.
   - D. Transforming a user query before retrieval.

4. Pick the description of `reranking` you would put in a `dictionary.md` entry.
   - A. Combining dense vector search with lexical or sparse search.
   - B. Re-scoring retrieved candidates with a stronger ranking model or method.
   - C. Transforming a user query before retrieval.
   - D. Generating multiple query variants for retrieval.

5. Which sentence is the best working definition of `cross-encoder`?
   - A. A model that scores query-document pairs jointly.
   - B. Transforming a user query before retrieval.
   - C. Generating multiple query variants for retrieval.
   - D. Combining dense vector search with lexical or sparse search.

6. In production AI work, what is the primary role of `parent-child retrieval`?
   - A. Transforming a user query before retrieval.
   - B. Generating multiple query variants for retrieval.
   - C. Combining dense vector search with lexical or sparse search.
   - D. Retrieving small child chunks while passing larger parent context to generation.

7. A teammate asks you to define `context compression` in one sentence. Which is closest?
   - A. Generating multiple query variants for retrieval.
   - B. Combining dense vector search with lexical or sparse search.
   - C. Reducing retrieved content before generation.
   - D. Transforming a user query before retrieval.

8. Pick the description of `query routing` you would put in a `dictionary.md` entry.
   - A. Combining dense vector search with lexical or sparse search.
   - B. Sending a request to the appropriate retriever, tool, model, or workflow.
   - C. Transforming a user query before retrieval.
   - D. Generating multiple query variants for retrieval.


## Applied Multiple Choice

1. Applied case: Basic vector search often misses exact domain references and rare terms.
   - A. Assume the largest available model will mask the underlying weakness in `query rewrite` so no system change is needed.
   - B. Skip the rollback plan; staging is close enough to production.
   - C. Set up a controlled experiment isolating `query rewrite`, capture before/after numbers, and write the result to a decision record.
   - D. Remove logging and evaluation to keep the diff small and merge faster.

2. Applied case: Reranking improves precision but consumes latency budget.
   - A. Hard-code the new behaviour for the first failing case and call it a fix.
   - B. Add the work to the capstone as a reviewable artifact that exercises `multi-query` end-to-end, with tests and a trace.
   - C. Assume the largest available model will mask the underlying weakness in `query rewrite` so no system change is needed.
   - D. Skip the rollback plan; staging is close enough to production.

3. Applied case: Advanced techniques can degrade quality if they are not evaluated against a baseline.
   - A. Define explicit acceptance criteria, rollback steps, and a reviewer checklist tied to Advanced RAG, Retrieval, and Reranking.
   - B. Skip the rollback plan; staging is close enough to production.
   - C. Hard-code the new behaviour for the first failing case and call it a fix.
   - D. Ship the change without measurement because the most recent demo looked good.

4. Applied case: Run a retrieval experiment suite comparing chunking, hybrid search, reranking, and query rewriting.
   - A. Hard-code the new behaviour for the first failing case and call it a fix.
   - B. Ship the change without measurement because the most recent demo looked good.
   - C. Remove logging and evaluation to keep the diff small and merge faster.
   - D. Compare at least two approaches against a labelled set covering `query routing`, then choose on measured quality, latency, cost, and risk.

5. Applied case: Implement a confidence-aware reranking policy that reranks only selected requests.
   - A. Remove logging and evaluation to keep the diff small and merge faster.
   - B. Assume the largest available model will mask the underlying weakness in `query rewrite` so no system change is needed.
   - C. Write a one-page design memo naming the assumption, the test that would falsify it, and the metric you'd watch in production.
   - D. Ship the change without measurement because the most recent demo looked good.

6. Applied case: Design a query router that chooses RAG, SQL analytics, tool workflow, or safe refusal.
   - A. Skip the rollback plan; staging is close enough to production.
   - B. Set up a controlled experiment isolating `query rewrite`, capture before/after numbers, and write the result to a decision record.
   - C. Remove logging and evaluation to keep the diff small and merge faster.
   - D. Assume the largest available model will mask the underlying weakness in `query rewrite` so no system change is needed.


## Fill In The Blanks

1. Given the production failure "The rewrite changes meaning and retrieves the wrong policy.", the concept being misused is ________.
2. To handle situations where it can improve recall by covering synonyms and perspectives, the engineering tool you reach for is ________ (watch for: Multiple queries add noise and cost without measurable gain.).
3. ________ is best summarised as: Combining dense vector search with lexical or sparse search. Verification step: Tune fusion and evaluate by query type.
4. On a system review, you find reranking adds latency but does not improve answer quality — the underlying chapter concept is ________.
5. It is often more accurate than bi-encoder retrieval but slower. A common failure looks like: Using it on every candidate exceeds latency budget. The concept is ________.
6. Given the production failure "The parent context includes irrelevant neighboring sections.", the concept being misused is ________.
7. To handle situations where it saves tokens and can remove noise, the engineering tool you reach for is ________ (watch for: Compression removes a critical exception or qualifier.).
8. ________ is best summarised as: Sending a request to the appropriate retriever, tool, model, or workflow. Verification step: Create route labels and evaluate routing confusion.

## Short Answer

1. If a reviewer asks 'why does `query rewrite` matter here?', what one-paragraph answer do you give? Include a metric.
2. Describe the smallest experiment that would tell you whether `multi-query` is correctly implemented in your system.
3. When would you intentionally *avoid* using `hybrid search`? Name a constraint or tradeoff.
4. What does a healthy log or trace look like for `reranking`? List the fields you would expect.
5. Explain how `cross-encoder` appears in the capstone, what artifact proves it, and what failure mode you would test.
6. If a reviewer asks 'why does `parent-child retrieval` matter here?', what one-paragraph answer do you give? Include a metric.
7. Describe the smallest experiment that would tell you whether `context compression` is correctly implemented in your system.
8. When would you intentionally *avoid* using `query routing`? Name a constraint or tradeoff.

## Scenario Questions

1. Incident: Basic vector search often misses exact domain references and rare terms. What do you inspect first, and which metric would prove the fix?
2. Design review: Reranking improves precision but consumes latency budget. Which artifact would you require before approving?
3. Postmortem prompt: Advanced techniques can degrade quality if they are not evaluated against a baseline. What regression test would prevent recurrence?
4. An engineer disables `query routing` to mitigate latency. Quality drops the next day. What evidence reverses the decision?

## Practical Debug Questions

1. What log or trace fields would help you debug a failure in `query rewrite` in this chapter's context?
2. What single metric would you watch in production when changing `cross-encoder`?
3. You suspect `query routing` is degraded. Design the smallest experiment that would falsify or confirm it in under an hour.
4. For the failure 'Basic vector search often misses exact domain references and rare terms.', sketch a rollback plan with a clear restore-point definition.
5. What artifact would you put in a portfolio README to prove competence with `query rewrite`, `multi-query`, `hybrid search`?

## Answer Key

### Multiple Choice

1. A
2. D
3. C
4. B
5. A
6. D
7. C
8. B

### Applied Multiple Choice

1. C
2. B
3. A
4. D
5. C
6. B

### Fill In The Blanks

1. query rewrite
2. multi-query
3. hybrid search
4. reranking
5. cross-encoder
6. parent-child retrieval
7. context compression
8. query routing

Short-answer, scenario, and debug questions should be graded against the rubric in `../../syllabus/evaluation_rubric.md`.

## References

[1] RAG Techniques GitHub: https://github.com/NirDiamant/RAG_Techniques
[2] Awesome RAG GitHub: https://github.com/coree/awesome-rag
[3] Qdrant vector concepts: https://qdrant.tech/documentation/concepts/vectors/
[4] Weaviate hybrid search: https://weaviate.io/developers/weaviate/search/hybrid
[5] FlashRAG paper: https://arxiv.org/abs/2405.13576
[6] RAGLAB paper: https://arxiv.org/abs/2408.11381
