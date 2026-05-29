"""Scaled dot-product attention and multi-head attention, from scratch.

Matches the 2x2 worked example in chapters/05_*/deep_dive.md.

You will see two things implemented here that hosted APIs hide:
  1. The exact softmax(QK^T / sqrt(d)) V formula.
  2. The causal mask (each token can only attend to itself + earlier tokens).
"""
from __future__ import annotations
import math
import torch
import torch.nn as nn
import torch.nn.functional as F


def scaled_dot_product_attention(q: torch.Tensor,
                                 k: torch.Tensor,
                                 v: torch.Tensor,
                                 mask: torch.Tensor | None = None) -> torch.Tensor:
    """
    q, k, v shapes: (B, H, T, D_head)
    mask shape:    (1, 1, T, T) or broadcastable — True where allowed.

    Returns: (B, H, T, D_head)
    """
    d_head = q.size(-1)
    # scores: (B, H, T, T)
    scores = q @ k.transpose(-2, -1) / math.sqrt(d_head)
    if mask is not None:
        scores = scores.masked_fill(~mask, float("-inf"))
    weights = F.softmax(scores, dim=-1)
    return weights @ v


class MultiHeadAttention(nn.Module):
    """Multi-head self-attention with a causal mask.

    Key shapes (B = batch, T = sequence length, D = model dim, H = num heads):
      input  x      : (B, T, D)
      q, k, v       : (B, T, D) then reshaped to (B, H, T, D/H)
      output        : (B, T, D)
    """
    def __init__(self, d_model: int, num_heads: int, dropout: float = 0.0) -> None:
        super().__init__()
        assert d_model % num_heads == 0, "d_model must be divisible by num_heads"
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_head = d_model // num_heads

        # one linear per Q/K/V projection; combined for speed
        self.qkv_proj = nn.Linear(d_model, 3 * d_model, bias=False)
        self.out_proj = nn.Linear(d_model, d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        B, T, D = x.shape
        # project to q, k, v
        qkv = self.qkv_proj(x)                            # (B, T, 3D)
        q, k, v = qkv.chunk(3, dim=-1)                    # each (B, T, D)

        # reshape into heads: (B, H, T, D/H)
        q = q.view(B, T, self.num_heads, self.d_head).transpose(1, 2)
        k = k.view(B, T, self.num_heads, self.d_head).transpose(1, 2)
        v = v.view(B, T, self.num_heads, self.d_head).transpose(1, 2)

        # causal mask: lower-triangular ones. True = allowed.
        mask = torch.tril(torch.ones(T, T, dtype=torch.bool, device=x.device))
        mask = mask.view(1, 1, T, T)

        out = scaled_dot_product_attention(q, k, v, mask)  # (B, H, T, D/H)
        out = out.transpose(1, 2).contiguous().view(B, T, D)
        return self.dropout(self.out_proj(out))


if __name__ == "__main__":
    # Reproduce the 2x2 worked example from chapter 5 deep_dive.
    Q = torch.tensor([[1.0, 0.0], [0.0, 1.0]])
    K = torch.tensor([[1.0, 0.0], [1.0, 1.0]])
    V = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

    # add batch and head dims: (1, 1, 2, 2)
    q = Q.view(1, 1, 2, 2)
    k = K.view(1, 1, 2, 2)
    v = V.view(1, 1, 2, 2)

    out = scaled_dot_product_attention(q, k, v)
    print("attention output (should match the lesson's [[1.66, 2.66], [2.00, 3.00]]):")
    print(out.view(2, 2))
