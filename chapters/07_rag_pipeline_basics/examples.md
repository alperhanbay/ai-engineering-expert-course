# Examples: RAG Pipeline Basics

Reusable snippets matching `lesson.md`.

## 1. Idempotent ingestion (sha256 dedup)

```python
async def ingest(path: str, tenant_id: str) -> str:
    raw = read_bytes(path)
    sha = hashlib.sha256(raw).digest()
    doc_id = await documents.upsert(tenant_id=tenant_id, sha256=sha, source_uri=path, ...)
    if await chunks.exists(doc_id, chunking_version=CHUNKER_VERSION):
        return doc_id                      # already ingested with this chunker
    text = clean(parse(raw))
    pieces = chunk(text, version=CHUNKER_VERSION)
    vectors = await embedder.embed_batch([p.text for p in pieces])
    await chunks.bulk_insert(doc_id, pieces)
    await store.upsert(doc_id, pieces, vectors, index_version=INDEX_VERSION)
    return doc_id
```

## 2. Section-aware chunker (sketch)

```python
def chunk_section_aware(text: str, max_tokens: int = 512) -> list[Chunk]:
    sections = split_on_headings(text)        # respect the doc's own structure
    out = []
    for sec in sections:
        if count_tokens(sec.body) <= max_tokens:
            out.append(Chunk(text=sec.body, section=sec.title))
        else:
            for sub in recursive_split(sec.body, max_tokens):
                out.append(Chunk(text=sub, section=sec.title))
    return out
```

## 3. Parse-quality flag

```python
def parse_quality_warnings(parsed: ParsedDoc) -> list[str]:
    warns = []
    if parsed.char_count < 200:
        warns.append("suspiciously little text extracted")
    if parsed.table_char_ratio > 0.6:
        warns.append("table-heavy; check column alignment in chunks")
    if parsed.repeated_line_ratio > 0.3:
        warns.append("likely header/footer pollution")
    return warns
```

## 4. RAG prompt rendering (best chunk last)

```python
def render_rag_prompt(question: str, chunks: list[Chunk], prompt_version: str) -> str:
    # chunks are ranked best-first; reverse so the best sits nearest the question
    ctx = "\n".join(
        f'<document id="{c.document_id}" page="{c.page}">{c.text}</document>'
        for c in reversed(chunks)
    )
    return RAG_TEMPLATES[prompt_version].format(context=ctx, question=question)
```

## 5. No-answer guard

```python
if not chunks:
    await audit.record_no_answer(ctx, question)
    return AskResponse(answer=None, citations=[], reason="insufficient_context",
                       requires_review=True, request_id=ctx.request_id)
```

## 6. Validate citations against retrieved chunks

```python
def drop_unsupported_citations(result: PolicyAnswer, retrieved: list[Chunk]) -> PolicyAnswer:
    retrieved_ids = {c.id for c in retrieved}
    kept = [c for c in result.citations if c.chunk_id in retrieved_ids]
    if not kept and result.answer is not None:
        # model cited only chunks it never received -> treat as unsupported
        return result.model_copy(update={"answer": None, "citations": [],
                                          "reason": "no_supported_citation"})
    return result.model_copy(update={"citations": kept})
```

## 7. Citation-correctness eval

```python
def citation_correct(answer: PolicyAnswer, gold_chunk_id: str) -> bool:
    return any(c.chunk_id == gold_chunk_id for c in answer.citations)

rate = sum(citation_correct(run(q), gold) for q, gold in cases) / len(cases)
```

## 8. Per-request chain log

```python
logger.info("rag_answer",
            request_id=ctx.request_id, tenant_id=ctx.tenant_id,
            retrieved=[(c.id, round(c.score, 3)) for c in chunks],
            used=[c.id for c in used_chunks],
            prompt_version="rag_v4", model_id=MODEL, index_version=INDEX_VERSION,
            cited=[c.chunk_id for c in result.citations],
            no_answer=result.answer is None,
            latency_ms=latency, input_tokens=it, output_tokens=ot)
```

## 9. No-answer test set

```python
UNANSWERABLE = [
    "What is the CEO's home address?",        # not in corpus, and shouldn't be
    "What will the policy say in 2030?",      # future, unknowable
    "Summarise chapter 12 of a book we don't have.",
    "What is the refund policy?",             # corpus has no refund content
    "Who won the match last night?",          # out of domain
]

@pytest.mark.parametrize("q", UNANSWERABLE)
def test_refuses(q, ask):
    out = ask(q)
    assert out.answer is None and out.reason == "insufficient_context"
```

## 10. Chunking experiment harness

```python
async def compare_chunkers(corpus, eval_cases, chunkers):
    rows = []
    for name, chunker in chunkers.items():
        await reindex(corpus, chunker, index_version=f"exp_{name}")
        cc = sum(citation_correct(run(q, index=f"exp_{name}"), gold)
                 for q, gold in eval_cases) / len(eval_cases)
        rows.append({"chunker": name, "citation_correctness": cc})
    return rows   # change ONE variable; embedding model held constant
```
