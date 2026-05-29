"""Minimal Byte-Pair Encoding tokenizer, from scratch.

Sennrich, Haddow, Birch (2015): https://arxiv.org/abs/1508.07909

BPE starts with a vocabulary of bytes (256 of them) and iteratively
merges the most frequent adjacent pair into a new token. The merge table
is the tokenizer.

This implementation is character-level (not byte-level) for clarity.
Production tokenizers (tiktoken, sentencepiece) are byte-level for
robustness to arbitrary input.
"""
from __future__ import annotations
from collections import Counter
from typing import Iterable


class BPETokenizer:
    def __init__(self) -> None:
        # word -> count of that word in the training corpus
        self._word_freqs: Counter[str] = Counter()
        # ordered list of merges: ("a", "b") means "merge ab into a single token"
        self.merges: list[tuple[str, str]] = []
        # final vocabulary: token string -> id
        self.vocab: dict[str, int] = {}

    # ---------- training ----------

    def train(self, corpus: Iterable[str], num_merges: int) -> None:
        """Learn `num_merges` merges from the corpus."""
        # 1. Pre-tokenize: split on whitespace; represent each word as
        #    a tuple of characters with end-of-word marker `</w>`.
        for line in corpus:
            for word in line.split():
                self._word_freqs[word] += 1

        # internal representation: word -> (char, char, ..., "</w>") tuple
        splits: dict[str, list[str]] = {
            w: list(w) + ["</w>"] for w in self._word_freqs
        }

        for _ in range(num_merges):
            pair_freqs = self._count_pairs(splits)
            if not pair_freqs:
                break
            best_pair, _ = pair_freqs.most_common(1)[0]
            splits = self._apply_merge(splits, best_pair)
            self.merges.append(best_pair)

        # final vocab = base chars + merged tokens
        seen: set[str] = set()
        for tokens in splits.values():
            seen.update(tokens)
        # ensure deterministic ordering: base chars sorted, then merges in
        # the order they were learned
        base = sorted({c for c in seen if len(c) == 1})
        merged = ["".join(p) for p in self.merges]
        for i, tok in enumerate(base + merged):
            self.vocab.setdefault(tok, i)

    def _count_pairs(self, splits: dict[str, list[str]]) -> Counter:
        counts: Counter = Counter()
        for word, tokens in splits.items():
            freq = self._word_freqs[word]
            for i in range(len(tokens) - 1):
                counts[(tokens[i], tokens[i + 1])] += freq
        return counts

    def _apply_merge(self, splits, pair) -> dict[str, list[str]]:
        a, b = pair
        merged = a + b
        new: dict[str, list[str]] = {}
        for word, tokens in splits.items():
            out: list[str] = []
            i = 0
            while i < len(tokens):
                if i < len(tokens) - 1 and tokens[i] == a and tokens[i + 1] == b:
                    out.append(merged)
                    i += 2
                else:
                    out.append(tokens[i])
                    i += 1
            new[word] = out
        return new

    # ---------- encoding / decoding ----------

    def encode(self, text: str) -> list[int]:
        ids: list[int] = []
        for word in text.split():
            tokens = list(word) + ["</w>"]
            for a, b in self.merges:
                tokens = self._merge_in_word(tokens, a, b)
            for t in tokens:
                if t not in self.vocab:
                    # unknown char — could add an <unk> token; we just skip here
                    continue
                ids.append(self.vocab[t])
        return ids

    @staticmethod
    def _merge_in_word(tokens: list[str], a: str, b: str) -> list[str]:
        out: list[str] = []
        i = 0
        while i < len(tokens):
            if i < len(tokens) - 1 and tokens[i] == a and tokens[i + 1] == b:
                out.append(a + b)
                i += 2
            else:
                out.append(tokens[i])
                i += 1
        return out

    def decode(self, ids: list[int]) -> str:
        inv = {i: t for t, i in self.vocab.items()}
        tokens = [inv[i] for i in ids if i in inv]
        # </w> marks end of word
        text = "".join(tokens).replace("</w>", " ").strip()
        return text


if __name__ == "__main__":
    # tiny smoke test — try the running example from the lesson
    corpus = ["the cat sat on the cat", "the dog sat", "the cat ran"]
    tok = BPETokenizer()
    tok.train(corpus, num_merges=10)
    print("merges:", tok.merges)
    print("vocab size:", len(tok.vocab))
    test = "the cat ran on the dog"
    ids = tok.encode(test)
    print("ids:", ids)
    print("decoded:", tok.decode(ids))
