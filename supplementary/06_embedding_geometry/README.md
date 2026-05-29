# Supplementary 06: Embedding Geometry by Hand

An optional companion to chapter 6. The point: stop treating embeddings as
opaque vendor output. Embed, measure, visualise.

## What you'll see

- A pairwise cosine-similarity matrix that *should* show three clusters
  (claim deadlines, refund policy, chitchat).
- The nearest neighbours of a paraphrased query — note how the model finds
  cluster-1 sentences even though they share few words with the query.
- A 2-D t-SNE projection so you can *see* the clusters.

## Run

```bash
pip install sentence-transformers numpy scikit-learn matplotlib
python embed_and_plot.py
```

The model downloads on first run (~80 MB). It's a small 384-dim model and is
free; this lab does not call any paid API.

## What to commit

- `notes.md` answering:
  1. Which cross-cluster similarities surprised you, and why?
  2. The query "How long do I have to report a crash?" matched a sentence
     that didn't share the word "crash" — explain in one sentence what
     the embedding model "saw" that lexical search would miss.
  3. Pick a sentence from chitchat and rewrite it to deliberately *increase*
     its similarity to cluster 1 by ~0.2 without using cluster-1 keywords.
     Did it work? Why or why not?

## Stretch

- Repeat with a domain-tuned embedding model (e.g. one of the `legal-bert`
  family). Does the cluster separation improve on your domain?
- Add 30 more sentences from your capstone corpus; re-run; observe how the
  cluster structure changes (this is the *real* test).

## Why this matters for chapter 6

The cosine-vs-dot-product, normalisation, and Recall@k discussions in the
main chapter assume you have a "feel" for the geometry. After this lab,
when you read about HNSW or hybrid search, you will know what space the
algorithms are operating in.
