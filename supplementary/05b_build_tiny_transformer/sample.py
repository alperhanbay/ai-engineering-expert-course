"""Sample text from the trained model. Demonstrates decoding controls in code.

Usage:
    python sample.py --checkpoint runs/latest/model.pt --prompt "Once upon"

Try several temperatures, top_k, top_p settings. Note:
  - temperature 0  -> degenerate / repetitive
  - temperature 1  -> "natural" sounding for a trained model
  - temperature 2  -> word salad
  - top_k = 1      -> argmax (greedy) -> same as temperature ~ 0
  - top_p = 0.9    -> "nucleus sampling" — common production default
"""
from __future__ import annotations
import argparse
from pathlib import Path

import torch

from mini_transformer import MiniTransformer


def load(checkpoint_path: Path) -> tuple[MiniTransformer, dict, dict, dict]:
    ckpt = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    cfg = ckpt["config"]
    model = MiniTransformer(
        vocab_size=len(ckpt["stoi"]),
        max_seq_len=cfg["seq_len"],
        d_model=cfg["d_model"],
        num_heads=cfg["num_heads"],
        num_layers=cfg["num_layers"],
    )
    model.load_state_dict(ckpt["model_state"])
    model.eval()
    return model, ckpt["stoi"], ckpt["itos"], cfg


def encode(text: str, stoi: dict[str, int]) -> torch.Tensor:
    ids = [stoi[c] for c in text if c in stoi]
    if not ids:
        # fall back to a random vocab token to avoid empty input
        ids = [next(iter(stoi.values()))]
    return torch.tensor([ids], dtype=torch.long)


def decode(ids: torch.Tensor, itos: dict[int, str]) -> str:
    return "".join(itos[int(i)] for i in ids[0])


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--checkpoint", default="runs/latest/model.pt")
    p.add_argument("--prompt", default="The ")
    p.add_argument("--max_new_tokens", type=int, default=200)
    p.add_argument("--temperature", type=float, default=1.0)
    p.add_argument("--top_k", type=int, default=None)
    p.add_argument("--top_p", type=float, default=None)
    p.add_argument("--num_samples", type=int, default=3)
    args = p.parse_args()

    model, stoi, itos, _ = load(Path(args.checkpoint))
    print(f"--- prompt ---\n{args.prompt!r}\n--- settings ---\n"
          f"temperature={args.temperature}, top_k={args.top_k}, top_p={args.top_p}\n"
          f"--- {args.num_samples} samples ---")

    seed = encode(args.prompt, stoi)
    for i in range(args.num_samples):
        out = model.generate(seed.clone(), max_new_tokens=args.max_new_tokens,
                             temperature=args.temperature,
                             top_k=args.top_k, top_p=args.top_p)
        text = decode(out, itos)
        print(f"\n[sample {i + 1}]\n{text}")


if __name__ == "__main__":
    main()
