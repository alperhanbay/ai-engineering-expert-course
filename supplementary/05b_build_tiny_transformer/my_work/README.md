# My Work — Supplementary 05b

Commit your deliverables here.

## Deliverables checklist

- [ ] `notes.md` — redo the 2×2 attention worked example by hand; show the
      arithmetic. Confirm `python attention.py` produces the same numbers.
- [ ] `training_log.md` — loss curve from `python train.py`; note where the
      loss plateaus and your guess as to why.
- [ ] `samples.md` — three generations from the trained model at different
      decoding settings (e.g. `temperature=0.5/1.0/1.5` and `top_k=20`).
      One paragraph explaining what changed and why, in terms of the
      decoding mechanism.
- [ ] `architecture_diagram.md` — your own Mermaid (or hand-drawn) diagram
      of the transformer block, labelled with tensor shapes at each step.
- [ ] `reflection.md` — one paragraph: what surprised you about
      implementing attention vs reading about it?

## Tips

- Download Tiny Shakespeare:
  `mkdir -p data && curl -o data/input.txt https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt`
- Your loss should start near `log(vocab_size)` (random) — for ~65 unique
  characters, ~4.1 nats. Trained to ~1.5 nats is normal for a tiny model.
- If you see NaN losses: lower the learning rate.
- If you want to *feel* the KV-cache, modify `mini_transformer.generate()`
  to cache per-step K/V tensors and reuse them. The naive version
  recomputes everything every step.

## AI tool use (mandatory section, see ACADEMIC_INTEGRITY.md)

- I used AI tools for: _list here, or "none"_
- I did NOT use AI tools for: _list_
- I verified the math by computing one attention forward pass by hand.
