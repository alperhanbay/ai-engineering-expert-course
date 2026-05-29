# Open Problems in LLM and RAG Engineering

A university course should be honest about where the field is still groping.
This document collects the active open problems the course *touches* but does
not pretend to solve. Read it before the capstone. Pick a couple your work
acknowledges in your portfolio README's "limitations" section.

## 1. Why LLMs work — interpretability

We can train trillion-parameter models; we cannot meaningfully explain *why*
any specific output happened. Mechanistic interpretability is making progress
(sparse autoencoders, feature circuits, induction heads) but is years from
production use.

**What we don't know:** how to causally attribute an output to a feature in
the model in a way auditors would accept; whether interpretability methods
scale to frontier models.

**Why it matters to you:** your portfolio cannot claim "we know why the model
answered X." Your defensibility (chapter 16) comes from *the system around
the model* (retrieval, citations, eval), not from explaining the model.

**Pointers**: Anthropic's interpretability research (https://transformer-circuits.pub/);
OpenAI's research blog; recent ICML/NeurIPS interpretability tracks.

## 2. Alignment beyond preference fine-tuning

RLHF (chapter 14) and its successors (DPO) align models to human preferences
*on the distributions used during training*. Out-of-distribution behaviour,
deceptive alignment, and scalable oversight (how do humans supervise tasks
they can't do themselves?) remain unsolved.

**What we don't know:** whether current alignment techniques generalise to
more capable systems; how to detect when they fail; how to align without
humans-in-the-loop on every example.

**Why it matters to you:** your guardrails (chapter 15) are the load-bearing
controls — never the model's alignment alone.

## 3. Evaluation validity

Chapter 9 teaches LLM-as-judge + calibration. The deeper problem: even with
calibration, your judge inherits the judge's biases. The field doesn't have a
ground-truth-free way to evaluate generative output reliably.

**What we don't know:** whether "faithfulness" measured by a judge model
corresponds to what users care about; how much eval-set overfitting actually
happens in published numbers; whether MT-Bench-style benchmarks predict
production behaviour.

**Why it matters to you:** publish honest results. A gap of 0.05 on
faithfulness probably isn't real signal. Always include the calibration
study.

**Pointers**: Zheng et al. (MT-Bench, 2306.05685); Saad-Falcon et al. (ARES,
2311.09476); ongoing eval-benchmark contamination work.

## 4. Hallucination

We can reduce hallucination (RAG, citations, structured output, refusal); we
cannot eliminate it. The relationship between training data, decoding, and
output truthfulness is not fully understood.

**What we don't know:** whether scaling alone fixes hallucination; whether
retrieval can ever be enough; the right metric for "truthfulness" in
open-ended generation.

**Why it matters to you:** the no-answer path (chapter 7) is a feature, not a
limitation. Build it in.

## 5. Prompt injection — fundamentally unsolved

OWASP LLM01 is at the top of the list because, as of late 2025, no purely
prompt-level defence prevents injection (chapter 15). Containment via code,
permissions, and human approval is the engineering answer; a "secure prompt"
is not.

**What we don't know:** whether architecture changes (separate trusted and
untrusted channels) will resolve this; how much current detection
classifiers are gameable.

**Why it matters to you:** test your guardrails against indirect injection
through retrieved content and tool outputs. Don't claim your system is
injection-proof — claim your blast radius is bounded.

**Pointers**: Greshake et al. (2302.12173); Zou et al. (universal jailbreaks,
2307.15043); OWASP LLM Top 10.

## 6. Long-context attention

Chapter 5 mentions "lost in the middle" (Liu et al., 2307.03172). Why
long-context performance degrades — and at what point context size starts
hurting more than helping — is an active research area.

**What we don't know:** whether techniques like positional interpolation,
hierarchical attention, or retrieval-into-context work robustly; how to
measure context utilisation cheaply.

**Why it matters to you:** "just stuff more context in" is not a reliable
quality strategy. Measure (chapter 8) and budget (chapter 13).

## 7. Embeddings — domain shift and the "feel" of vector space

Embeddings work surprisingly well, often poorly on domain-specific terms,
and we have no compact theory of when they generalise. The MTEB
leaderboard captures one slice; your domain may not match.

**What we don't know:** whether domain-tuned embeddings beat general ones in
production after the small/large-corpus crossover; how to predict embedding
performance without measuring.

**Why it matters to you:** chapter 6's labelled retrieval set is essential.
Measure your domain.

## 8. Cost transparency and model lifecycle

Hosted models change behind their aliases. Per-token pricing changes. Quotas
change. The course's chapter 11 + chapter 13 give you the engineering shape,
but the actual numbers in your decision matrices will rot.

**What we don't know (collectively):** how to negotiate model-lifecycle terms
that protect production deployments; whether open models will catch up to
the cost-effectiveness gap in time for your project.

**Why it matters to you:** record the model id behind the alias (chapter 2)
and the date the matrix was filled. Refresh annually.

## 9. Multi-agent coordination

Chapter 10 builds single-agent workflows. Multi-agent systems (CrewAI,
AutoGen, swarms) are a rapidly evolving space with little consensus on
evaluation, safety, or design patterns.

**What we don't know:** whether multi-agent designs are reliably better
than single-agent + good orchestration; how to evaluate emergent
multi-agent behaviour.

**Why it matters to you:** the course teaches the unit; multi-agent is the
extension. Don't add it without a measured reason.

## 10. The "agentic" benchmark crisis

There is no consensus benchmark for production agent quality. Existing
benchmarks (SWE-bench, GAIA, AgentBench) measure specific tasks; production
agent quality is task-specific and your golden set is your real benchmark.

**What we don't know:** how to publish agent results that transfer across
domains.

**Why it matters to you:** measure on *your* domain. Public benchmarks are
signals, not proof.

## 11. Compliance moving faster than the field

Regulators (EU AI Act, US state laws, sector regs) are codifying
requirements while the field is still inventing. Some requirements
(explanation, audit, data residency) translate cleanly to the controls in
chapter 15; others (model risk categorisation, conformity assessments) are
still being interpreted.

**What we don't know:** where the line will land in 2026-2028.

**Why it matters to you:** your audit log (chapter 2) and threat model
(chapter 15) are the artifacts that will translate across regimes. Build
both well.

## How to use this document

1. After ch00, skim it once to set expectations.
2. After ch09 and ch15, return and mark which problems your capstone
   actively touches.
3. In your portfolio README's "Limitations" section, name at least three
   open problems your work is exposed to and how you mitigated (rather
   than solved) them.

That honesty is the senior signal the course optimises for.
