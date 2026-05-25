# Expanded Question Bank: RAG Pipeline Basics

## How To Use This Bank

Answer without looking at the answer key. For every wrong answer, write one sentence explaining the concept in your own words and one sentence explaining how it appears in a production AI system.


## Multiple Choice

1. A teammate asks you to define `ingestion` in one sentence. Which is closest?
   - A. Removing or normalizing noise from extracted data.
   - B. Splitting documents into retrievable units.
   - C. The process of bringing source data into the AI system.
   - D. Extracting structured text and metadata from source formats.

2. Pick the description of `parsing` you would put in a `dictionary.md` entry.
   - A. Splitting documents into retrievable units.
   - B. Extracting structured text and metadata from source formats.
   - C. The process of bringing source data into the AI system.
   - D. Removing or normalizing noise from extracted data.

3. Which sentence is the best working definition of `cleaning`?
   - A. Removing or normalizing noise from extracted data.
   - B. The process of bringing source data into the AI system.
   - C. Extracting structured text and metadata from source formats.
   - D. Splitting documents into retrievable units.

4. In production AI work, what is the primary role of `chunking`?
   - A. The process of bringing source data into the AI system.
   - B. Extracting structured text and metadata from source formats.
   - C. Removing or normalizing noise from extracted data.
   - D. Splitting documents into retrievable units.

5. A teammate asks you to define `metadata enrichment` in one sentence. Which is closest?
   - A. Extracting structured text and metadata from source formats.
   - B. Removing or normalizing noise from extracted data.
   - C. Adding useful structured fields to chunks or documents.
   - D. The process of bringing source data into the AI system.

6. Pick the description of `retrieval` you would put in a `dictionary.md` entry.
   - A. Removing or normalizing noise from extracted data.
   - B. Finding relevant data for a query before generation or action.
   - C. The process of bringing source data into the AI system.
   - D. Extracting structured text and metadata from source formats.

7. Which sentence is the best working definition of `citation`?
   - A. A reference connecting an answer claim to source evidence.
   - B. The process of bringing source data into the AI system.
   - C. Extracting structured text and metadata from source formats.
   - D. Removing or normalizing noise from extracted data.

8. In production AI work, what is the primary role of `no-answer behavior`?
   - A. The process of bringing source data into the AI system.
   - B. Extracting structured text and metadata from source formats.
   - C. Removing or normalizing noise from extracted data.
   - D. A designed refusal when sources are insufficient.


## Applied Multiple Choice

1. Applied case: Bad parsing and chunking cause failures before the model is called.
   - A. Set up a controlled experiment isolating `ingestion`, capture before/after numbers, and write the result to a decision record.
   - B. Remove logging and evaluation to keep the diff small and merge faster.
   - C. Assume the largest available model will mask the underlying weakness in `ingestion` so no system change is needed.
   - D. Skip the rollback plan; staging is close enough to production.

2. Applied case: Citations are only useful when they point to actually supporting context.
   - A. Assume the largest available model will mask the underlying weakness in `ingestion` so no system change is needed.
   - B. Skip the rollback plan; staging is close enough to production.
   - C. Hard-code the new behaviour for the first failing case and call it a fix.
   - D. Add the work to the capstone as a reviewable artifact that exercises `parsing` end-to-end, with tests and a trace.

3. Applied case: No-answer behavior must be designed, tested, and measured.
   - A. Hard-code the new behaviour for the first failing case and call it a fix.
   - B. Ship the change without measurement because the most recent demo looked good.
   - C. Define explicit acceptance criteria, rollback steps, and a reviewer checklist tied to RAG Pipeline Basics.
   - D. Skip the rollback plan; staging is close enough to production.

4. Applied case: Build an end-to-end RAG pipeline with citations and request traces.
   - A. Remove logging and evaluation to keep the diff small and merge faster.
   - B. Compare at least two approaches against a labelled set covering `no-answer behavior`, then choose on measured quality, latency, cost, and risk.
   - C. Hard-code the new behaviour for the first failing case and call it a fix.
   - D. Ship the change without measurement because the most recent demo looked good.

5. Applied case: Create a chunk quality report with broken chunks, metadata gaps, and fixes.
   - A. Write a one-page design memo naming the assumption, the test that would falsify it, and the metric you'd watch in production.
   - B. Ship the change without measurement because the most recent demo looked good.
   - C. Remove logging and evaluation to keep the diff small and merge faster.
   - D. Assume the largest available model will mask the underlying weakness in `ingestion` so no system change is needed.

6. Applied case: Build a citation correctness test set with supported and unsupported questions.
   - A. Remove logging and evaluation to keep the diff small and merge faster.
   - B. Assume the largest available model will mask the underlying weakness in `ingestion` so no system change is needed.
   - C. Skip the rollback plan; staging is close enough to production.
   - D. Set up a controlled experiment isolating `ingestion`, capture before/after numbers, and write the result to a decision record.


## Fill In The Blanks

1. Given the production failure "Documents are indexed without source or permission metadata.", the concept being misused is ________.
2. To handle situations where bad parsing creates broken chunks and unreliable citations, the engineering tool you reach for is ________ (watch for: PDF headers, footers, and tables pollute retrieval.).
3. ________ is best summarised as: Removing or normalizing noise from extracted data. Verification step: Define safe cleaning rules and preserve source anchors.
4. On a system review, you find chunks are too small to contain complete obligations — the underlying chapter concept is ________.
5. It supports filters, citations, routing, and analysis. A common failure looks like: Chunks lack page or section, making citations unhelpful. The concept is ________.
6. Given the production failure "The model hallucinates because the required evidence was never retrieved.", the concept being misused is ________.
7. To handle situations where citations create user trust and auditability, the engineering tool you reach for is ________ (watch for: The cited chunk is related but does not support the specific answer.).
8. ________ is best summarised as: A designed refusal when sources are insufficient. Verification step: Test unsupported questions and track no-answer correctness.

## Short Answer

1. If a reviewer asks 'why does `ingestion` matter here?', what one-paragraph answer do you give? Include a metric.
2. Describe the smallest experiment that would tell you whether `parsing` is correctly implemented in your system.
3. When would you intentionally *avoid* using `cleaning`? Name a constraint or tradeoff.
4. What does a healthy log or trace look like for `chunking`? List the fields you would expect.
5. Explain how `metadata enrichment` appears in the capstone, what artifact proves it, and what failure mode you would test.
6. If a reviewer asks 'why does `retrieval` matter here?', what one-paragraph answer do you give? Include a metric.
7. Describe the smallest experiment that would tell you whether `citation` is correctly implemented in your system.
8. When would you intentionally *avoid* using `no-answer behavior`? Name a constraint or tradeoff.

## Scenario Questions

1. Postmortem prompt: Bad parsing and chunking cause failures before the model is called. What regression test would prevent recurrence?
2. On-call triage: Citations are only useful when they point to actually supporting context. Walk through the first three steps you would take.
3. Incident: No-answer behavior must be designed, tested, and measured. What do you inspect first, and which metric would prove the fix?
4. A teammate proposes a major change to `retrieval` with no experiment. Which artifact do you ask for before approving?

## Practical Debug Questions

1. What log or trace fields would help you debug a failure in `ingestion` in this chapter's context?
2. What single metric would you watch in production when changing `metadata enrichment`?
3. You suspect `no-answer behavior` is degraded. Design the smallest experiment that would falsify or confirm it in under an hour.
4. For the failure 'Bad parsing and chunking cause failures before the model is called.', sketch a rollback plan with a clear restore-point definition.
5. What artifact would you put in a portfolio README to prove competence with `ingestion`, `parsing`, `cleaning`?

## Answer Key

### Multiple Choice

1. C
2. B
3. A
4. D
5. C
6. B
7. A
8. D

### Applied Multiple Choice

1. A
2. D
3. C
4. B
5. A
6. D

### Fill In The Blanks

1. ingestion
2. parsing
3. cleaning
4. chunking
5. metadata enrichment
6. retrieval
7. citation
8. no-answer behavior

Short-answer, scenario, and debug questions should be graded against the rubric in `../../syllabus/evaluation_rubric.md`.

## References

[1] LangChain RAG guide: https://docs.langchain.com/oss/python/langchain/rag
[2] LlamaIndex RAG overview: https://developers.llamaindex.ai/python/framework/understanding/rag/
[3] Haystack pipelines: https://docs.haystack.deepset.ai/docs/pipelines
[4] OpenAI File Search: https://platform.openai.com/docs/guides/tools-file-search
[5] RAG Survey paper: https://arxiv.org/abs/2312.10997
