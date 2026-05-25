# Lesson: RAG Pipeline Basics

## 1. What RAG Is

RAG stands for Retrieval-Augmented Generation. It combines retrieval from external sources with LLM generation.

The key idea:

> Instead of relying only on the model's internal parameters, retrieve relevant external context and ask the model to answer from that context.

## 2. Why RAG Exists

RAG helps with:

- private knowledge;
- changing knowledge;
- long documents;
- citations;
- reducing unsupported answers;
- domain-specific information;
- auditability.

RAG does not automatically guarantee correctness. It must be designed, evaluated, and monitored.

## 3. Basic RAG Architecture

```text
documents
  -> parse
  -> clean
  -> chunk
  -> enrich metadata
  -> embed
  -> index

question
  -> embed query
  -> retrieve chunks
  -> construct prompt
  -> generate answer
  -> return citations
  -> log trace
```

## 4. Ingestion

Ingestion turns source documents into retrievable data.

Steps:

- load file or URL;
- extract text;
- remove noise;
- preserve structure;
- split into chunks;
- attach metadata;
- embed;
- index.

Parsing quality matters. Bad parsing creates bad chunks.

## 5. Chunking

Chunking splits documents into smaller units for retrieval.

Common strategies:

- fixed-size chunking;
- recursive chunking;
- semantic chunking;
- section-aware chunking;
- parent-child chunking.

Tradeoffs:

- small chunks: precise but may miss context;
- large chunks: more context but more noise;
- overlap: preserves continuity but increases storage and duplication.

## 6. Metadata

Metadata should preserve retrieval context:

- source;
- page;
- section;
- title;
- document type;
- tenant;
- date;
- permissions;
- version.

Citations depend on metadata.

## 7. Retrieval

At question time, the system retrieves candidate chunks.

Basic retrieval:

```text
question -> embedding -> vector search top-k -> chunks
```

This is a starting point, not the final expert system.

## 8. Prompt Construction

The RAG prompt should include:

- task instruction;
- answer format;
- no-answer rule;
- retrieved context;
- citation instruction;
- user question.

Never mix source content and system instructions ambiguously.

## 9. Citation Design

A useful citation should include:

- document ID;
- chunk ID;
- source name;
- page or section;
- score;
- possibly quote span.

Citation correctness must be evaluated. A citation that points to a loosely related chunk is not enough.

## 10. No-Answer Handling

The system should be allowed to say:

```text
The available sources do not contain enough information to answer.
```

No-answer behavior is critical in legal, financial, insurance, medical-like, and compliance-sensitive domains.

## 11. Logging

Each request should record:

- question;
- retrieved chunks;
- scores;
- prompt version;
- model version;
- answer;
- citations;
- latency;
- error or no-answer flag.

## 12. Key Takeaway

A basic RAG pipeline is easy to demo but hard to make reliable. The basics are ingestion, chunking, embedding, retrieval, generation, citations, no-answer behavior, and logging.
## Numbered References

[1] LangChain RAG guide: https://docs.langchain.com/oss/python/langchain/rag
[2] LlamaIndex RAG overview: https://developers.llamaindex.ai/python/framework/understanding/rag/
[3] Haystack pipelines: https://docs.haystack.deepset.ai/docs/pipelines
[4] OpenAI File Search: https://platform.openai.com/docs/guides/tools-file-search
[5] RAG Survey paper: https://arxiv.org/abs/2312.10997
