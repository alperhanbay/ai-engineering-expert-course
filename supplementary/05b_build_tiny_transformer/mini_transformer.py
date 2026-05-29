"""A tiny decoder-only transformer (GPT-style).

The whole model fits in this file so you can read it end to end.

Tensor shape conventions:
    B = batch size
    T = sequence length (number of tokens)
    D = model dimension (embedding size)
    H = number of attention heads
    V = vocabulary size
"""
from __future__ import annotations
import math
import torch
import torch.nn as nn
import torch.nn.functional as F

from attention import MultiHeadAttention


class TransformerBlock(nn.Module):
    """One block: attention -> residual+LN -> MLP -> residual+LN.

    This is the "pre-LN" variant (LayerNorm before the sublayer), which is
    what most modern LLMs use because it trains more stably than post-LN.
    """
    def __init__(self, d_model: int, num_heads: int, mlp_ratio: int = 4,
                 dropout: float = 0.0) -> None:
        super().__init__()
        self.ln1 = nn.LayerNorm(d_model)
        self.attn = MultiHeadAttention(d_model, num_heads, dropout)
        self.ln2 = nn.LayerNorm(d_model)
        # Standard MLP: D -> 4D -> D with GELU non-linearity
        self.mlp = nn.Sequential(
            nn.Linear(d_model, mlp_ratio * d_model),
            nn.GELU(),
            nn.Linear(mlp_ratio * d_model, d_model),
            nn.Dropout(dropout),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # pre-LN residual: x = x + sublayer(LN(x))
        x = x + self.attn(self.ln1(x))
        x = x + self.mlp(self.ln2(x))
        return x


class MiniTransformer(nn.Module):
    """A small decoder-only LM. ~100k-1M parameters at default config."""
    def __init__(self,
                 vocab_size: int,
                 max_seq_len: int = 128,
                 d_model: int = 64,
                 num_heads: int = 4,
                 num_layers: int = 4,
                 dropout: float = 0.1) -> None:
        super().__init__()
        self.max_seq_len = max_seq_len
        self.d_model = d_model

        # Embeddings: token (V -> D) and positional (T -> D)
        self.token_embed = nn.Embedding(vocab_size, d_model)
        self.pos_embed = nn.Embedding(max_seq_len, d_model)
        self.embed_dropout = nn.Dropout(dropout)

        self.blocks = nn.ModuleList([
            TransformerBlock(d_model, num_heads, dropout=dropout)
            for _ in range(num_layers)
        ])
        self.final_ln = nn.LayerNorm(d_model)

        # LM head: D -> V. Weight-tied with the token embedding (a common
        # trick: it reduces parameters and often slightly improves quality).
        self.lm_head = nn.Linear(d_model, vocab_size, bias=False)
        self.lm_head.weight = self.token_embed.weight

        # Standard initialization (small, Gaussian)
        self.apply(self._init_weights)

    @staticmethod
    def _init_weights(module: nn.Module) -> None:
        if isinstance(module, nn.Linear):
            nn.init.normal_(module.weight, mean=0.0, std=0.02)
            if module.bias is not None:
                nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Embedding):
            nn.init.normal_(module.weight, mean=0.0, std=0.02)

    def forward(self,
                idx: torch.Tensor,
                targets: torch.Tensor | None = None
                ) -> tuple[torch.Tensor, torch.Tensor | None]:
        """
        idx:     (B, T) token ids
        targets: (B, T) token ids to predict (shifted by 1), or None

        Returns logits (B, T, V) and the cross-entropy loss (or None).
        """
        B, T = idx.shape
        assert T <= self.max_seq_len, f"sequence length {T} > max {self.max_seq_len}"

        positions = torch.arange(T, device=idx.device).unsqueeze(0)  # (1, T)
        x = self.token_embed(idx) + self.pos_embed(positions)        # (B, T, D)
        x = self.embed_dropout(x)

        for block in self.blocks:
            x = block(x)
        x = self.final_ln(x)
        logits = self.lm_head(x)                                     # (B, T, V)

        loss = None
        if targets is not None:
            # cross-entropy over the vocab, averaged over all positions
            loss = F.cross_entropy(
                logits.view(-1, logits.size(-1)),
                targets.view(-1),
                ignore_index=-1,
            )
        return logits, loss

    @torch.no_grad()
    def generate(self,
                 idx: torch.Tensor,
                 max_new_tokens: int,
                 temperature: float = 1.0,
                 top_k: int | None = None,
                 top_p: float | None = None) -> torch.Tensor:
        """Autoregressive generation. Naive (no KV-cache, fine for tiny size).

        Implements three of the decoding strategies from chapter 5.4:
          - temperature: divides logits before softmax
          - top_k:      keeps only the k highest-probability tokens
          - top_p:      keeps the smallest set whose mass exceeds p (nucleus)
        """
        for _ in range(max_new_tokens):
            # crop to context window
            ctx = idx[:, -self.max_seq_len:]
            logits, _ = self.forward(ctx)
            # only the last position's logits matter for next-token prediction
            logits = logits[:, -1, :] / max(temperature, 1e-6)

            if top_k is not None:
                v, _ = torch.topk(logits, top_k)
                logits[logits < v[:, [-1]]] = float("-inf")

            if top_p is not None:
                sorted_logits, sorted_idx = torch.sort(logits, descending=True)
                probs = F.softmax(sorted_logits, dim=-1)
                cumprob = torch.cumsum(probs, dim=-1)
                # mask out tail beyond p
                tail = cumprob - probs > top_p
                sorted_logits[tail] = float("-inf")
                logits = torch.full_like(logits, float("-inf")).scatter_(
                    1, sorted_idx, sorted_logits)

            probs = F.softmax(logits, dim=-1)
            next_id = torch.multinomial(probs, num_samples=1)
            idx = torch.cat([idx, next_id], dim=1)
        return idx

    def num_params(self) -> int:
        return sum(p.numel() for p in self.parameters())


if __name__ == "__main__":
    # Sanity check: build a model, run a forward pass with random input.
    m = MiniTransformer(vocab_size=100, max_seq_len=16, d_model=32,
                        num_heads=4, num_layers=2)
    print(f"parameters: {m.num_params():,}")
    x = torch.randint(0, 100, (2, 16))
    y = torch.randint(0, 100, (2, 16))
    logits, loss = m(x, y)
    print(f"logits: {tuple(logits.shape)}  loss: {loss.item():.3f}")
    # Generate 20 tokens
    out = m.generate(x[:, :1], max_new_tokens=20, temperature=1.0, top_k=10)
    print(f"generated shape: {tuple(out.shape)}")
