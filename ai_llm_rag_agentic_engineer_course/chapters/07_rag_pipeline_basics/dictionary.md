# Dictionary: RAG Pipeline Basics

Use this dictionary at the end of the chapter. Add your own examples in `my_work/dictionary_notes.md`.

| Term | Working Definition | Why It Matters | Common Failure Mode | Mastery Check |
| --- | --- | --- | --- | --- |
| `ingestion` | The process of bringing source data into the AI system. | Ingestion determines what can be searched, cited, evaluated, and governed. | Documents are indexed without source or permission metadata. | Build an ingestion trace from raw file to indexed chunk. |
| `parsing` | Extracting structured text and metadata from source formats. | Bad parsing creates broken chunks and unreliable citations. | PDF headers, footers, and tables pollute retrieval. | Inspect parsed output and add parsing quality checks. |
| `cleaning` | Removing or normalizing noise from extracted data. | Clean text improves chunking, embedding, search, and generation. | Cleaning removes legal numbering needed for citations. | Define safe cleaning rules and preserve source anchors. |
| `chunking` | Splitting documents into retrievable units. | It shapes retrieval precision, recall, citations, and context quality. | Chunks are too small to contain complete obligations. | Run chunking experiments and inspect retrieval failures. |
| `metadata enrichment` | Adding useful structured fields to chunks or documents. | It supports filters, citations, routing, and analysis. | Chunks lack page or section, making citations unhelpful. | Enrich chunks with source, page, section, tenant, version, and access fields. |
| `retrieval` | Finding relevant data for a query before generation or action. | Retrieval quality often dominates RAG answer quality. | The model hallucinates because the required evidence was never retrieved. | Measure retrieval separately from generation. |
| `citation` | A reference connecting an answer claim to source evidence. | Citations create user trust and auditability. | The cited chunk is related but does not support the specific answer. | Evaluate citation correctness, not just citation presence. |
| `no-answer behavior` | A designed refusal when sources are insufficient. | It prevents forced unsupported answers in high-risk settings. | The system fabricates an answer when retrieval is empty. | Test unsupported questions and track no-answer correctness. |

## Dictionary Assignment

For each term:

1. Write a one-sentence definition in your own words.
2. Write a concrete example from your capstone (or planned capstone).
3. Write one failure mode you would test against.
4. Write one metric, test, or review check that would catch the failure.
5. Link one source from `references_numbered.md`.

## References

[1] LangChain RAG guide: https://docs.langchain.com/oss/python/langchain/rag
[2] LlamaIndex RAG overview: https://developers.llamaindex.ai/python/framework/understanding/rag/
[3] Haystack pipelines: https://docs.haystack.deepset.ai/docs/pipelines
[4] OpenAI File Search: https://platform.openai.com/docs/guides/tools-file-search
[5] RAG Survey paper: https://arxiv.org/abs/2312.10997
