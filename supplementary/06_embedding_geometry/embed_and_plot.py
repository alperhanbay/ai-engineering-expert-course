"""Compute embeddings yourself and look at the geometry — Karpathy-style.

The goal: stop treating embeddings as an opaque vendor product. Embed a
small list of sentences, compute pairwise distances, and visualise the
space. By the end you should have a numerical "feel" for what cosine
similarity is doing.

Run:
    pip install sentence-transformers numpy scikit-learn matplotlib
    python embed_and_plot.py
"""
from __future__ import annotations
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


SENTENCES = [
    # cluster 1: claim deadlines (the "policy" cluster)
    "Claims must be filed within 30 days of the incident.",
    "The deadline to report a crash is one month from the date of damage.",
    "If you wait more than 30 days, your claim will not be processed.",
    # cluster 2: refund policy
    "Refunds are available up to 14 days after purchase.",
    "You may request a refund within two weeks of the order.",
    "After 14 days, no refund is available.",
    # cluster 3: unrelated chitchat
    "The weather is nice today.",
    "I enjoy hiking on weekends.",
    "Coffee tastes better in the morning.",
]


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def main() -> None:
    print("loading embedding model (downloads on first run)...")
    model = SentenceTransformer("all-MiniLM-L6-v2")  # small, 384-dim, free

    print(f"embedding {len(SENTENCES)} sentences...")
    embs = model.encode(SENTENCES, normalize_embeddings=True)
    print(f"embeddings shape: {embs.shape} (sentences x dim)")
    print()

    # ---- 1. cosine similarity matrix ----
    print("=== pairwise cosine similarity ===")
    n = len(SENTENCES)
    sim = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            sim[i, j] = cosine(embs[i], embs[j])
    # print compact
    header = "       " + "  ".join(f"s{j:>2}" for j in range(n))
    print(header)
    for i in range(n):
        row = "  ".join(f"{sim[i, j]:5.2f}" for j in range(n))
        print(f"s{i:>2}    {row}")
    print()
    print("Read: within-cluster similarities should be > 0.6;")
    print("      cross-cluster similarities should be lower.")
    print()

    # ---- 2. nearest neighbours of one query ----
    query = "How long do I have to report a crash?"
    q = model.encode([query], normalize_embeddings=True)[0]
    sims = [cosine(q, e) for e in embs]
    ranked = sorted(zip(SENTENCES, sims), key=lambda x: -x[1])
    print(f"=== nearest neighbours of: {query!r} ===")
    for s, score in ranked[:5]:
        print(f"  {score:.3f}  {s}")
    print()

    # ---- 3. 2D projection (t-SNE) so you can see the clusters ----
    proj = TSNE(n_components=2, perplexity=3, init="pca", random_state=7).fit_transform(embs)
    plt.figure(figsize=(8, 6))
    for i, (x, y) in enumerate(proj):
        plt.scatter(x, y)
        plt.annotate(f"s{i}", (x, y), fontsize=9)
    plt.title("t-SNE projection of sentence embeddings")
    plt.savefig("embeddings_tsne.png", dpi=120, bbox_inches="tight")
    print("saved embeddings_tsne.png — open it and look at the clusters")


if __name__ == "__main__":
    main()
