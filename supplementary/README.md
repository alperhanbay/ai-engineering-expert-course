# Supplementary Labs

Optional, Karpathy-style "build it from scratch" labs. They are deliberately
*outside* the standard chapter structure (no quiz, no project lab, no
dictionary) because the point is implementation, not the templated learning
loop. They are graded only when the instructor opts into them.

| Lab | Companion to | What you build |
| --- | --- | --- |
| [`05b_build_tiny_transformer/`](05b_build_tiny_transformer/) | ch05 | BPE tokenizer + scaled dot-product attention + a tiny decoder-only LLM + a training loop + decoding controls. ~600 lines total. |
| [`06_embedding_geometry/`](06_embedding_geometry/) | ch06 | Compute embeddings locally, inspect the cosine matrix, and t-SNE the space. Gives you the *feel* the API hides. |
| [`07_no_framework_rag/`](07_no_framework_rag/) | ch07 | A complete RAG pipeline in ~150 lines with **no framework** — numpy cosine, f-string prompts, structured-output JSON, citation validation. |

## Suggested order

1. **`07_no_framework_rag/`** first — easiest, biggest immediate
   first-principles payoff, no GPU needed.
2. **`06_embedding_geometry/`** — quick (30 min), grounds the chapter-6
   metrics in numbers you've inspected.
3. **`05b_build_tiny_transformer/`** — longest (4-8 hours), best for the
   Karpathy mind-shift. Worth it if you want to interview as someone who
   understands transformers, not someone who imports them.

## What these labs deliberately do NOT include

- Quizzes, question banks, dictionaries, project labs, references_numbered —
  the structured templated chapter materials.
- A capstone tie-in. These are stand-alone understanding artifacts.

## How to use them as an instructor

Standard cohorts: leave them as extra credit (up to 5%).
Research/advanced cohorts: make `07_no_framework_rag/` a required deliverable
for ch07, and `05b_build_tiny_transformer/` a required mid-semester project
for graduate sections.
