# Supplementary 07: No-Framework RAG

The Karpathy-style version of chapter 7. Implements a complete RAG pipeline
in ~150 lines of Python with **zero retrieval frameworks** — no LangChain,
no LlamaIndex, no vector database. The only external calls are HTTP to an
LLM/embedding API (via the `openai` SDK, for ergonomics).

## Why do this

After this lab you should be able to point at every step of a production
RAG system and say "I know exactly what that does, because I built it." The
SDK boundaries that production stacks hide become visible: a vector store
is `numpy.argsort` over cosine similarities. Prompt rendering is an
f-string. "Structured output" is `response_format={"type":"json_object"}`.

Without doing this once, students can confuse "I called LangChain" with
"I understand RAG."

## Run

```bash
pip install openai numpy
export OPENAI_API_KEY=sk-...
python minimal_rag.py
```

The script prints three answers:
1. a supported question (correct answer with a citation),
2. an unsupported question (correct refusal — the no-answer path),
3. an out-of-scope question (refusal again).

## What the script demonstrates

| Concept (chapter) | Where in `minimal_rag.py` |
| --- | --- |
| corpus + chunks | the `CORPUS` list at the top |
| embedding (ch6) | `embed()` |
| vector index (ch6) | `index()` — just a list of `Chunk` |
| cosine similarity (ch6) | `np.dot(q, c.vec)` in `retrieve()` |
| filtered top-k (ch6/7) | `np.argsort(-sims)[:k]` |
| prompt construction (ch5/7) | `build_prompt()` — instructions first, context last |
| structured output (ch5/7) | `response_format={"type": "json_object"}` |
| no-answer behaviour (ch7) | system prompt's refusal rule + `validate_citations()` |
| citation correctness (ch7) | `validate_citations()` drops cited ids not in retrieved set |

## What to commit (in your chapter-7 `my_work/`)

- `minimal_rag.py` — your own version (don't copy this one verbatim; type it
  out so the abstractions land).
- `notes.md` answering:
  1. The script uses cosine similarity. Why don't you need an ANN index here?
  2. Show one query where this RAG gets the wrong answer. Why does it fail —
     retrieval, prompt, or model?
  3. Add a fourth corpus document on an obscure topic. Verify the refusal
     path still triggers for a question that has no support.
- `comparison.md` — once you've also done the chapter-7 RAG with LangChain
  or LlamaIndex, write two paragraphs comparing the two implementations.
  Where does the SDK help? Where does it hide something that mattered?

## Stretch

- Add hybrid search: implement BM25 in ~40 lines (or import `rank_bm25`),
  fuse with the dense scores using Reciprocal Rank Fusion.
- Add a tiny cross-encoder reranker (e.g. `sentence-transformers`
  `cross-encoder/ms-marco-MiniLM-L-6-v2`). Compare answer quality before
  and after on five queries.
- Add per-chunk `tenant_id` metadata and the cross-tenant test from chapter 6.

## What you should NOT do

Use a vector store or a RAG framework. The point of this lab is that you can
build RAG without one.

## Connection to the main course

This is the optional companion to chapter 7's `homework.md` task #3 ("ask
pipeline"). Do this first; doing the framework version after will feel like
*adding* abstractions to something you already understand, which is the right
order.
