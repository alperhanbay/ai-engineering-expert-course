# Lesson: Capstone, Portfolio, and Expert Interview Readiness

## 1. The Capstone Is the Proof

Everything in this course was building toward one thing: a single, integrated, production-style AI system that proves you can do the work — not in fragments, but end to end. The capstone is where the fifteen prior chapters stop being separate exercises and become one system with an API, a database, ingestion, retrieval, generation with citations, an agent workflow, an evaluation suite, observability, security controls, and a deployment story.

The defining standard for the capstone: **it must be defensible.** A reviewer — a hiring manager, an interviewer, an open-source visitor — should be able to read it, run it, and probe it, and find that every claim is backed by evidence. Not "it works" (a demo) but "here's the eval report, here's the trace, here's the threat model, here's the limitation I haven't solved yet." The difference between a portfolio that gets you hired and one that doesn't is rarely the cleverness of the idea; it's the honesty and completeness of the evidence.

This chapter is about assembling that proof and the narrative that goes with it. It adds little new technique — it's the integration, the documentation, and the interview preparation that turn your work into something others can evaluate.

## 2. What "Defensible" Means Concretely

A defensible capstone has these properties, each tied to a prior chapter:

- **Runnable by a stranger** in minutes from a README (chapter 4's reproducibility).
- **Grounded answers with verifiable citations** (chapter 7).
- **A no-answer path that actually refuses** (chapter 7).
- **An evaluation report with numbers, per risk level** (chapter 9) — not "it's accurate," but "faithfulness 0.96 on high-risk, here are the failures."
- **Observability that shows quality, not just uptime** (chapter 12).
- **A threat model and a guardrail suite that passes** (chapter 15).
- **A release manifest and a rollback story** (chapters 4, 12).
- **Named, honest limitations** — at least three things you know are imperfect.

The last point is the one that separates senior from junior work. A portfolio that shows only success paths signals inexperience; everyone who has shipped AI knows it's full of sharp edges. A portfolio that says "here's what works, here's what doesn't yet, here's how I'd fix it" signals someone who has actually operated a system. **Honest limitations are a feature of the portfolio, not a weakness.**

## 3. The Architecture Pack

A reviewer needs to understand your system without reading all the code. The architecture pack is a small set of one-page diagrams:

- **API / system diagram**: the components and how a request flows through them.
- **Data model diagram**: the SQL schema (chapter 2) and how documents → chunks → embeddings → answers → feedback relate.
- **RAG / retrieval flow**: ingestion and query paths (chapter 7).
- **Agent workflow**: the state graph with tools and approval gates (chapter 10).
- **Deployment diagram**: containers, services, CI/CD, where it runs (chapter 4).
- **Threat model diagram**: trust boundaries and controls (chapter 15).

Each diagram is one page and *matches the implementation*. A common failure: decorative diagrams that don't reflect the actual code, which a sharp interviewer will catch by asking "where is this in the repo?" The diagrams are a map, and the map must match the territory.

## 4. The Portfolio README

The README is the front door. Most reviewers decide whether to go deeper based on it alone. A strong portfolio README has:

- **What it is** — one paragraph: the domain, the problem, who it's for.
- **How to run it** — the chapter-4 three-command setup, tested on a clean clone.
- **Architecture** — the pack from section 3, or links to it.
- **Results** — the eval report with real numbers, per risk level, and a link to how they were measured.
- **Security** — the threat model summary and guardrail pass rate.
- **Limitations** — the honest list, with planned next steps.
- **Sources** — numbered references for external claims (the course's `[1]`-style discipline).

What kills a portfolio README: buzzwords without evidence ("production-ready, enterprise-grade, state-of-the-art") and no runnable instructions. What makes one credible: numbers, a working `docker compose up`, and named limitations. Write it for a skeptical reader who will try to break your claims.

## 5. The Demo Script

A live demo is high-risk: things break, and a demo that only shows the happy path hides exactly what reviewers want to see. A repeatable demo script de-risks it and shows depth:

1. **Ingestion**: add a document, show it indexed.
2. **Supported answer**: ask a question, get a grounded answer with a verifiable citation.
3. **Unsupported answer**: ask something the corpus can't answer, show the refusal.
4. **An eval run**: show the eval report and what the gate decides.
5. **A security case**: show an injection attempt being blocked (chapter 15).

Showing the refusal and the blocked injection is what separates a serious demo from a toy. Anyone can demo a question that works; demonstrating that the system *knows what it doesn't know* and *resists attack* is the senior signal. Script it so it's reproducible (chapter 12's demo runbook) and runs in under 15 minutes from a clean clone.

## 6. System Design Interviews

The expert interview tests whether you can *reason about* AI systems, not just build one. System design questions ("design a RAG system for legal documents," "how would you evaluate an agent") are where the course's per-chapter discipline pays off. A strong answer:

1. **Clarifies requirements first** — who are the users, what's the accuracy bar, latency budget, data sensitivity, scale. (Don't jump to architecture.)
2. **Reasons about the data and retrieval** before the model — most quality lives there (chapters 6–8).
3. **Names the evaluation strategy** — how you'd know it works, the golden set, the gate (chapter 9).
4. **Reaches failure modes and operations** — what breaks, how you'd detect it, how you'd roll back (chapter 12).
5. **Addresses security** — injection, tenant isolation, the controls (chapter 15).
6. **States tradeoffs explicitly** — cost vs quality vs latency, with the decision criteria (chapter 13).

The most common failure in these interviews: candidates describe a happy-path architecture and never reach evaluation, failure modes, or security. The chapters of this course are, not coincidentally, the checklist of what a complete system-design answer covers. An interviewer probing "how do you know it's good?" or "what happens when the model is wrong?" is checking for exactly the disciplines you've built.

## 7. Behavioral Interviews: STAR Stories from Real Work

Behavioral questions ("tell me about a time you...") are answered with STAR: Situation, Task, Action, Result. The capstone gives you real material if you mined it as you went. Prepare stories for:

- **A failure** you found and fixed (with the measured before/after).
- **A tradeoff** you made (cost vs quality, e.g. the chapter-13 decision record).
- **An incident** you handled (or simulated — the chapter-12 rollback drill).
- **A scope cut** — what you chose *not* to build and why (judgment signal).
- **Collaboration / review** — how you made your work reviewable.

The weak version lists tools used. The strong version names a measurable result and a decision: "retrieval was missing exact policy codes (Recall@5 0.71); I added hybrid search, which raised it to 0.89 at +40ms p95; I rejected reranking because it didn't improve faithfulness." That's a STAR story with a number and a tradeoff — exactly what the course's measurement discipline produces.

## 8. Mining the Capstone for Interview Material

The reason the course pushed artifacts (decision records, failure logs, eval reports, threat models) at every chapter is that they *are* your interview material. Before interviewing, harvest:

- **Failure log** (chapters 9, 12) → failure and incident STAR stories.
- **Decision records** (chapters 6, 8, 13) → tradeoff stories and system-design reasoning.
- **Eval report** (chapter 9) → the "how do you know it works?" answer.
- **Threat model** (chapter 15) → the security answer.
- **Architecture pack** (section 3) → the whiteboard you've already drawn.

A candidate who built the capstone with this discipline walks into interviews with concrete, numbered, defensible stories. A candidate who skipped the artifacts has to invent them under pressure. The interview prep isn't a separate phase — it's harvesting what you already produced.

## 9. Open-Source Quality

If the capstone is public (and it should be — chapter's earlier GitHub work), it's held to open-source standards:

- **Runnable docs** that actually work on a clean clone.
- **Honest limitations** and a roadmap, not marketing.
- **Source references** for external claims.
- **A LICENSE** and basic contribution guidance.
- **Tests and CI** that a visitor can see passing (the badge).
- **No secrets in history** (chapter 4) — and rotate anything that leaked.

The bar: a stranger should be able to clone it, run it, understand it, trust the numbers, and see clearly what's done and what isn't. That bar is also exactly what a hiring reviewer applies, so meeting it serves both audiences at once.

## 10. Common Mistakes and Anti-Patterns

1. **Happy-path-only portfolio.** Hides eval, refusal, and security — the senior signals.
2. **Buzzwords without evidence.** "Production-ready" with no eval report or runnable setup.
3. **Decorative diagrams** that don't match the code.
4. **No named limitations.** Signals inexperience.
5. **A demo that only shows one working question.**
6. **System-design answers that never reach eval, failure modes, or security.**
7. **STAR stories that list tools, not results and decisions.**
8. **Interview material invented under pressure** because artifacts weren't kept.
9. **A README that can't get a stranger to a running system.**
10. **Secrets in git history** of a public repo.

## 11. Production Failure Modes (of the Portfolio Itself)

- **The demo breaks live** because it wasn't scripted/tested on a clean clone. Defensive: the demo runbook, rehearsed.
- **An interviewer asks "where is this in the code?" and the diagram doesn't match.** Defensive: diagrams generated from or checked against the implementation.
- **"How do you know it's accurate?" gets a hand-wave.** Defensive: the eval report with per-risk-level numbers, ready to show.
- **A reviewer finds a secret in the git history.** Defensive: secret scanning (chapter 4); rotate immediately if found.
- **The numbers in the README don't reproduce.** Defensive: every claim traces to a committed eval run or trace.

## 12. Security and Privacy

1. **A public capstone must not leak data or secrets** — scrub the corpus (use redistributable/synthetic data), scan history, rotate leaked tokens (chapter 4).
2. **Demo data is real data** if you used production samples — use synthetic or public corpora for anything public.
3. **The threat model is part of the portfolio**, not hidden — showing it is a strength.
4. **Don't expose a live, unauthenticated capstone** to the internet without the chapter-15 controls; a public demo endpoint is an attack surface.

## 13. The Capstone Checklist

By the end of chapter 16, the following should exist (the capstone is the integration of all prior `my_work/`):

- A runnable capstone repo: `docker compose up` to a working `/ask` in minutes (chapter 4), with the API, SQL, ingestion, RAG, agent, eval, observability, and security controls integrated.
- An `architecture_pack/` with the six one-page diagrams, matching the code.
- A `portfolio_README.md`: what/run/architecture/results/security/limitations/sources.
- An `interview_kit.md`: 5 STAR stories (failure, tradeoff, incident, scope cut, collaboration) with measured results, 3 system-design walkthroughs, 10 Q&A drills.
- A `demo.md`: the repeatable 5-step demo (ingest, supported, unsupported, eval, security), runnable in under 15 minutes.
- At least three honestly-named limitations with planned next steps.
- Every numeric claim traceable to a committed eval run or trace.

If a stranger can clone the repo, run the demo in 15 minutes, read the eval numbers and trust them, see the injection get blocked, and find your honest limitations — without asking you — the capstone, and the course, is done.

## 14. Key Takeaway

The capstone is the proof that you can build production-grade AI end to end, and its value is in being *defensible*: runnable, measured, secured, and honest about its limits. Mine it for interview material as you build — the decision records, failure logs, eval reports, and threat model are your STAR stories and system-design answers. In interviews, reason past the happy path to evaluation, failure modes, and security, because that's where expertise shows. The senior signal, in the portfolio and in the room, is the same: evidence over claims, and honesty about what isn't solved yet.

## Numbered References

[1] OpenAI Cookbook: https://github.com/openai/openai-cookbook
[2] LangGraph GitHub: https://github.com/langchain-ai/langgraph
[3] LlamaIndex GitHub: https://github.com/run-llama/llama_index
[4] RAG Techniques GitHub: https://github.com/NirDiamant/RAG_Techniques
[5] DeepEval GitHub: https://github.com/confident-ai/deepeval
[6] RAGAS GitHub: https://github.com/explodinggradients/ragas
