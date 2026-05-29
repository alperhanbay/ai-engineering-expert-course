"""Train the mini transformer on a tiny text corpus.

Default: trains on whatever text file you point it at, character-level for
simplicity. Replace with the BPE tokenizer for a more realistic experiment.

CPU-friendly: a few thousand steps in minutes on a laptop.
"""
from __future__ import annotations
import argparse
import math
from pathlib import Path

import torch
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset

from mini_transformer import MiniTransformer


class CharDataset(Dataset):
    """Character-level dataset. One sample = a fixed-length window of token ids."""

    def __init__(self, text: str, seq_len: int):
        self.seq_len = seq_len
        chars = sorted(set(text))
        self.stoi = {c: i for i, c in enumerate(chars)}
        self.itos = {i: c for c, i in self.stoi.items()}
        self.ids = torch.tensor([self.stoi[c] for c in text], dtype=torch.long)

    @property
    def vocab_size(self) -> int:
        return len(self.stoi)

    def __len__(self) -> int:
        return self.ids.size(0) - self.seq_len - 1

    def __getitem__(self, idx: int):
        x = self.ids[idx: idx + self.seq_len]
        y = self.ids[idx + 1: idx + self.seq_len + 1]
        return x, y


def get_lr(step: int, warmup: int, max_steps: int, lr_max: float, lr_min: float) -> float:
    """Standard warmup -> cosine decay schedule."""
    if step < warmup:
        return lr_max * (step + 1) / warmup
    progress = (step - warmup) / max(1, max_steps - warmup)
    return lr_min + 0.5 * (lr_max - lr_min) * (1 + math.cos(math.pi * progress))


def train(args) -> None:
    text = Path(args.data).read_text(encoding="utf-8")
    print(f"corpus: {len(text):,} characters")

    ds = CharDataset(text, seq_len=args.seq_len)
    print(f"vocab: {ds.vocab_size}, samples: {len(ds):,}")

    loader = DataLoader(ds, batch_size=args.batch_size, shuffle=True,
                        num_workers=0, drop_last=True)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = MiniTransformer(
        vocab_size=ds.vocab_size,
        max_seq_len=args.seq_len,
        d_model=args.d_model,
        num_heads=args.num_heads,
        num_layers=args.num_layers,
    ).to(device)
    print(f"parameters: {model.num_params():,}")

    optimiser = optim.AdamW(model.parameters(), lr=args.lr, betas=(0.9, 0.95),
                            weight_decay=0.1)

    model.train()
    step = 0
    losses: list[float] = []

    while step < args.max_steps:
        for x, y in loader:
            x, y = x.to(device), y.to(device)
            lr = get_lr(step, args.warmup, args.max_steps, args.lr, args.lr * 0.1)
            for g in optimiser.param_groups:
                g["lr"] = lr

            _, loss = model(x, y)
            optimiser.zero_grad(set_to_none=True)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimiser.step()

            losses.append(loss.item())
            if step % args.log_every == 0:
                avg = sum(losses[-args.log_every:]) / min(args.log_every, len(losses))
                print(f"step {step:>6} | loss {avg:.4f} | lr {lr:.2e}")

            step += 1
            if step >= args.max_steps:
                break

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    torch.save({"model_state": model.state_dict(),
                "stoi": ds.stoi, "itos": ds.itos,
                "config": vars(args)}, out / "model.pt")
    print(f"saved {out / 'model.pt'}")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--data", default="data/input.txt",
                   help="path to a text file (try Tiny Shakespeare)")
    p.add_argument("--out", default="runs/latest")
    p.add_argument("--seq_len", type=int, default=64)
    p.add_argument("--batch_size", type=int, default=32)
    p.add_argument("--d_model", type=int, default=64)
    p.add_argument("--num_heads", type=int, default=4)
    p.add_argument("--num_layers", type=int, default=4)
    p.add_argument("--max_steps", type=int, default=2000)
    p.add_argument("--warmup", type=int, default=100)
    p.add_argument("--lr", type=float, default=3e-3)
    p.add_argument("--log_every", type=int, default=100)
    args = p.parse_args()
    train(args)


if __name__ == "__main__":
    main()
