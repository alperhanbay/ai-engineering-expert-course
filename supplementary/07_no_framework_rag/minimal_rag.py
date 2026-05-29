"""A minimal RAG pipeline with zero frameworks.

No LangChain. No LlamaIndex. No vector DB. The point is to make every
abstraction visible so you can defend "I understand RAG" — not just
"I called a library."

What this uses:
    - Python stdlib
    - numpy (for cosine similarity)
    - the `openai` SDK *only* for the LLM call and the embedding call;
      they are HTTP calls in disguise. You could replace them with `requests`
      and 3 lines of JSON shaping if you wanted.

Run:
    pip install openai numpy
    export OPENAI_API_KEY=sk-...
    python minimal_rag.py
"""
from __future__ import annotations
import json
import os
import re
from dataclasses import dataclass

import numpy as np
from openai import OpenAI


# ---------- 1. The corpus (in-process; no vector DB) ----------

CORPUS: list[tuple[str, str]] = [
    # (doc_id, text)
    ("policy_v1#p3", "Claims must be filed within 30 days of the incident date. "
                    "Filings after 30 days are not eligible for processing."),
    ("policy_v1#p4", "Customers may upload supporting photographs as part of the "
                    "claim. Photographs must be clear and time-stamped."),
    ("policy_v1#p7", "Refunds for premium overpayment may be requested within "
                    "14 days of the payment date."),
    ("policy_v1#p9", "Coverage applies in jurisdictions A and B. Jurisdiction C "
                    "is excluded except where written endorsements apply."),
    ("policy_v1#p12", "If your policy lapses for more than 60 days, you must "
                     "re-apply rather than reinstate."),
]


# ---------- 2. The pieces, each ~10 lines ----------

@dataclass
class Chunk:
    doc_id: str
    text: str
    vec: np.ndarray


def embed(client: OpenAI, texts: list[str]) -> np.ndarray:
    """Call the embeddings endpoint and return a (N, D) numpy array."""
    resp = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts,
    )
    return np.array([d.embedding for d in resp.data], dtype=np.float32)


def index(client: OpenAI) -> list[Chunk]:
    """Embed the corpus once. In a real system this is a separate ingestion job."""
    vectors = embed(client, [text for _, text in CORPUS])
    # normalise so cosine == dot product
    vectors /= np.linalg.norm(vectors, axis=1, keepdims=True)
    return [Chunk(doc_id=doc_id, text=text, vec=v)
            for (doc_id, text), v in zip(CORPUS, vectors)]


def retrieve(query: str, chunks: list[Chunk], client: OpenAI, k: int = 3) -> list[Chunk]:
    """Cosine top-k. No HNSW, no Qdrant, no nothing — just numpy."""
    q = embed(client, [query])[0]
    q /= np.linalg.norm(q)
    sims = np.array([float(np.dot(q, c.vec)) for c in chunks])
    order = np.argsort(-sims)[:k]
    return [chunks[i] for i in order]


def build_prompt(question: str, retrieved: list[Chunk]) -> tuple[str, str]:
    """Render the prompt by hand. No template engine. f-strings only."""
    system = (
        "You answer insurance policy questions. Use ONLY the provided context. "
        "If the context does not contain the answer, respond exactly: "
        '{"answer": null, "citations": [], "reason": "insufficient_context"}. '
        "Otherwise respond with valid JSON matching: "
        '{"answer": string, "citations": [{"doc_id": string}], "reason": null}'
    )
    # most-relevant LAST (attention is strongest near the question)
    ctx = "\n".join(
        f'<document id="{c.doc_id}">{c.text}</document>'
        for c in reversed(retrieved)
    )
    user = (
        f"CONTEXT:\n{ctx}\n\nQUESTION: {question}\n\n"
        "Use only the context. Cite the doc_id of every supporting document."
    )
    return system, user


def generate(client: OpenAI, system: str, user: str) -> dict:
    """One LLM call. Parse JSON. Defend against malformed output."""
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        response_format={"type": "json_object"},  # provider-enforced JSON
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    raw = resp.choices[0].message.content or "{}"
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # one repair attempt — strip code fences if any
        return json.loads(re.sub(r"^```(?:json)?|```$", "", raw.strip(), flags=re.M))


def validate_citations(result: dict, retrieved: list[Chunk]) -> dict:
    """Drop any cited doc_id that was not actually in the retrieved set."""
    ok = {c.doc_id for c in retrieved}
    citations = [c for c in result.get("citations") or [] if c.get("doc_id") in ok]
    if result.get("answer") is not None and not citations:
        # model invented a citation -> treat as unsupported
        return {"answer": None, "citations": [], "reason": "no_supported_citation"}
    result["citations"] = citations
    return result


# ---------- 3. The whole pipeline ----------

def ask(client: OpenAI, chunks: list[Chunk], question: str) -> dict:
    retrieved = retrieve(question, chunks, client, k=3)
    system, user = build_prompt(question, retrieved)
    result = generate(client, system, user)
    result = validate_citations(result, retrieved)
    return {
        "question": question,
        "retrieved_doc_ids": [c.doc_id for c in retrieved],
        **result,
    }


def main() -> None:
    assert os.getenv("OPENAI_API_KEY"), "set OPENAI_API_KEY first"
    client = OpenAI()
    print("indexing corpus...")
    chunks = index(client)
    print(f"indexed {len(chunks)} chunks")

    # 1) a supported question
    print(json.dumps(ask(client, chunks,
                         "How long do I have to file a claim?"), indent=2))
    # 2) an unsupported question (should refuse)
    print(json.dumps(ask(client, chunks,
                         "Does the policy cover earthquakes?"), indent=2))
    # 3) an unrelated question (should refuse)
    print(json.dumps(ask(client, chunks,
                         "What is the weather today?"), indent=2))


if __name__ == "__main__":
    main()
