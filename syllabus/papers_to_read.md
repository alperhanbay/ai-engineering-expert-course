# Required Reading: Seminal Papers

A curated, university-style reading list. These are the primary sources behind
the field's current practice. The course discusses each at engineering depth;
this list asks you to read the *original* — the math, the experiments, the
honest limitations sections.

Order matters: read foundations before alignment, alignment before RAG/agents.
Plan one paper per week alongside the matching chapter.

## How to read a paper (briefly)

1. Abstract + Introduction + Conclusion — 10 min.
2. Figures (especially the headline result figure) — 10 min.
3. Method section, slowly, with a pen — 30-60 min.
4. Experiments + ablations — 20 min.
5. Limitations + Related Work — 15 min.

Keep a one-page note per paper in `my_work/papers/` covering: claim,
contribution, evidence, what they didn't show, your one critical question.

## The list

### Foundations of transformers and LLMs

| Year | Paper | Authors | Link | Tie-in |
| --- | --- | --- | --- | --- |
| 2017 | Attention Is All You Need | Vaswani et al. | https://arxiv.org/abs/1706.03762 | ch05 — the transformer architecture |
| 2018 | BERT: Pre-training of Deep Bidirectional Transformers | Devlin et al. | https://arxiv.org/abs/1810.04805 | ch05/ch06 — bidirectional pretraining; embeddings ancestor |
| 2020 | Language Models are Few-Shot Learners (GPT-3) | Brown et al. | https://arxiv.org/abs/2005.14165 | ch05 — scale + in-context learning |
| 2020 | Scaling Laws for Neural Language Models | Kaplan et al. | https://arxiv.org/abs/2001.08361 | ch05/ch14 — capacity/compute/data tradeoffs |
| 2022 | Training Compute-Optimal LLMs (Chinchilla) | Hoffmann et al. | https://arxiv.org/abs/2203.15556 | ch14 — data-vs-parameters lesson |
| 2022 | Emergent Abilities of Large Language Models | Wei et al. | https://arxiv.org/abs/2206.07682 | ch05 — phase transitions; debated |

### Alignment, instruction following, preference learning

| Year | Paper | Authors | Link | Tie-in |
| --- | --- | --- | --- | --- |
| 2017 | Deep RL from Human Preferences | Christiano et al. | https://arxiv.org/abs/1706.03741 | ch14 — RLHF roots |
| 2022 | Training Language Models to Follow Instructions (InstructGPT) | Ouyang et al. | https://arxiv.org/abs/2203.02155 | ch14 — RLHF on LLMs |
| 2023 | Direct Preference Optimization (DPO) | Rafailov et al. | https://arxiv.org/abs/2305.18290 | ch14 — preference tuning without RL |
| 2021 | LoRA: Low-Rank Adaptation | Hu et al. | https://arxiv.org/abs/2106.09685 | ch14 — PEFT default |
| 2023 | QLoRA: Efficient Finetuning of Quantized LLMs | Dettmers et al. | https://arxiv.org/abs/2305.14314 | ch14 — fits one GPU |

### Retrieval and RAG

| Year | Paper | Authors | Link | Tie-in |
| --- | --- | --- | --- | --- |
| 2020 | Dense Passage Retrieval (DPR) | Karpukhin et al. | https://arxiv.org/abs/2004.04906 | ch06 — dense retrieval foundation |
| 2020 | Retrieval-Augmented Generation (RAG) | Lewis et al. | https://arxiv.org/abs/2005.11401 | ch07 — original RAG paper |
| 2020 | ColBERT: Late Interaction | Khattab & Zaharia | https://arxiv.org/abs/2004.12832 | ch08 — late interaction |
| 2022 | HyDE: Precise Zero-Shot Dense Retrieval | Gao et al. | https://arxiv.org/abs/2212.10496 | ch08 — query rewriting |
| 2023 | RAG for Knowledge-Intensive NLP (Survey) | Gao et al. | https://arxiv.org/abs/2312.10997 | ch07/ch08 — landscape |
| 2023 | Lost in the Middle | Liu et al. | https://arxiv.org/abs/2307.03172 | ch05/ch08 — long-context attention degradation |

### Agents, tools, reasoning

| Year | Paper | Authors | Link | Tie-in |
| --- | --- | --- | --- | --- |
| 2022 | ReAct: Synergizing Reasoning and Acting | Yao et al. | https://arxiv.org/abs/2210.03629 | ch10 — the agent pattern |
| 2022 | Chain-of-Thought Prompting | Wei et al. | https://arxiv.org/abs/2201.11903 | ch05 — reasoning elicitation |
| 2023 | Toolformer | Schick et al. | https://arxiv.org/abs/2302.04761 | ch10 — tool use |

### Evaluation

| Year | Paper | Authors | Link | Tie-in |
| --- | --- | --- | --- | --- |
| 2023 | Judging LLM-as-a-Judge (MT-Bench) | Zheng et al. | https://arxiv.org/abs/2306.05685 | ch09 — judge calibration + bias |
| 2023 | RAGAS: Automated RAG Evaluation | Es et al. | https://arxiv.org/abs/2309.15217 | ch09 — RAG metrics |
| 2023 | ARES | Saad-Falcon et al. | https://arxiv.org/abs/2311.09476 | ch09 — automated RAG eval |

### Serving and efficiency

| Year | Paper | Authors | Link | Tie-in |
| --- | --- | --- | --- | --- |
| 2022 | FlashAttention | Dao et al. | https://arxiv.org/abs/2205.14135 | ch13 — fast attention |
| 2023 | Efficient Memory Management for LLM Serving (vLLM/PagedAttention) | Kwon et al. | https://arxiv.org/abs/2309.06180 | ch13 — serving |
| 2023 | Speculative Decoding (accelerating) | Leviathan et al. | https://arxiv.org/abs/2211.17192 | ch13 — fast inference |

### Safety and security

| Year | Paper | Authors | Link | Tie-in |
| --- | --- | --- | --- | --- |
| 2023 | Indirect Prompt Injection | Greshake et al. | https://arxiv.org/abs/2302.12173 | ch15 — the defining attack |
| 2023 | Universal and Transferable Adversarial Attacks on LLMs | Zou et al. | https://arxiv.org/abs/2307.15043 | ch15 — jailbreak research |

### Mixture-of-Experts and modern architectures

| Year | Paper | Authors | Link | Tie-in |
| --- | --- | --- | --- | --- |
| 2017 | Outrageously Large Neural Networks (sparsely-gated MoE) | Shazeer et al. | https://arxiv.org/abs/1701.06538 | ch05 — MoE foundations |
| 2022 | Switch Transformers | Fedus et al. | https://arxiv.org/abs/2101.03961 | ch05 — scalable MoE |

## Suggested mapping to chapters

| Chapter | Read alongside |
| --- | --- |
| 05 LLM fundamentals | Vaswani 2017, Brown 2020, Kaplan 2020, Wei 2022, Liu 2023 |
| 06 embeddings | Devlin 2018, Karpukhin 2020 |
| 07 RAG | Lewis 2020, Gao 2023 (survey) |
| 08 advanced RAG | Khattab 2020 (ColBERT), Gao 2022 (HyDE) |
| 09 evaluation | Zheng 2023, Es 2023 (RAGAS), Saad-Falcon 2023 (ARES) |
| 10 agents | Yao 2022 (ReAct), Wei 2022 (CoT), Schick 2023 (Toolformer) |
| 13 optimization | Dao 2022 (FlashAttention), Kwon 2023 (vLLM), Leviathan 2023 (speculative) |
| 14 fine-tuning | Hoffmann 2022 (Chinchilla), Ouyang 2022 (InstructGPT), Hu 2021 (LoRA), Dettmers 2023 (QLoRA), Rafailov 2023 (DPO) |
| 15 security | Greshake 2023, Zou 2023 |

## Deliverable

For each paper you read, commit `my_work/papers/<short_name>.md` with the
one-page note (claim, contribution, evidence, gaps, your question).

## A note on staleness

This list will need refreshing every 6–12 months. The 2026 frontier is moving
fast (long-context attention research, agent benchmarks, post-training).
If you're reading this more than a year after the course was published,
treat the post-2023 entries as candidates for replacement.
