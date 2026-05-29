# Lesson: Orientation and Expert Roadmap

## 1. What This Course Actually Trains

This course exists to make you strong in a field, not to get you past one job interview. The target is the ability to **design, build, evaluate, operate, secure, and explain** production AI systems — LLM, RAG, and agentic — that face real data, real users, real latency budgets, real safety requirements, and real production feedback. That is a wider skill than "can call an LLM API." It is the difference between someone who can make a demo and someone a team trusts to own a system in production.

The orientation chapter's job is to set the frame for everything that follows: what "expert" means here, how to study so the learning sticks, what artifact each chapter must leave behind, and — most importantly — how to choose the capstone that turns sixteen chapters of separate skills into one defensible system. The single most consequential decision you make in this course is made here, in chapter 00, before you write any code: *what are you going to build, for whom, and how will you know it's good?*

## 2. The Expert Profile

"Production-grade LLM, RAG, and Agentic AI Engineer" decomposes into capabilities the course builds in order:

- **Backend foundations** (chapters 1–4): maintainable Python services, SQL as the control plane, HTTP contracts, reproducible deployment. The unglamorous layer that everything sits on.
- **LLM and retrieval** (chapters 5–8): prompting as engineering, embeddings and vector search, RAG pipelines, advanced retrieval and reranking. Where most quality lives.
- **Measurement and autonomy** (chapters 9–10): evaluation as a control system, agents as workflow engineering. Where systems become trustworthy and capable.
- **Operations and platforms** (chapters 11–13): enterprise platforms without lock-in, production monitoring, optimization. Where systems survive contact with reality.
- **Adaptation and safety** (chapters 14–15): when to fine-tune (rarely), layered security. Where engineering judgment and risk management show.
- **Integration** (chapter 16): the capstone and the narrative. Where it all becomes proof.

The expert is not the person who knows the most tool names. It's the person who can look at a problem, choose the cheapest lever that solves it, measure whether it worked, operate it in production, and explain the tradeoffs — and who knows when *not* to reach for the impressive technique. The whole course is biased toward that judgment.

## 3. Why Most Learners Plateau (and How Not To)

Three failure patterns stall people learning AI engineering. Name them so you can avoid them:

1. **Tool collection.** Installing LangChain, LlamaIndex, Qdrant, vLLM, and five others without building an integrated system. You end up able to recite features and unable to ship. The cure: one capstone, one tool per category, integration over breadth.
2. **Demo thinking.** Stopping at "it answered my question once." Demos hide evaluation, latency, security, cost, and failure modes — i.e. everything that's hard. The cure: every chapter produces a *measured* artifact, not a screenshot.
3. **No evidence.** Learning that lives only in your head. You can't prove it to an interviewer, a reviewer, or yourself. The cure: the `my_work/` discipline — every chapter leaves a file someone else could review.

The through-line: **integration and evidence beat breadth and enthusiasm.** A learner who builds one complete, measured, secured, documented system understands more than one who skimmed twenty tutorials, and has something to show for it.

## 4. The Capstone Decision

The capstone is a production-style AI knowledge assistant for a *regulated or high-accuracy domain* — legal, medical, financial, insurance, internal compliance/policy. The domain constraint is deliberate: high-accuracy domains force you to confront the hard parts (faithfulness, citations, no-answer behaviour, audit, security) that a casual chatbot lets you skip.

Choosing well, in chapter 00, shapes the whole course. A good capstone choice has:

- **A real corpus you can use**: public standards, open documentation, or synthetic documents you can redistribute. (Don't pick a domain whose documents you can't legally use.)
- **Clear users with a real need**: "a claims adjuster checking policy deadlines," not "people, generally."
- **A measurable success criterion**: what does a good answer look like, and how would you score it?
- **Genuine risk**: a wrong answer should *matter*, so the safety and evaluation work has teeth.
- **Manageable scope**: narrow enough to finish, rich enough to be interesting.

Write the proposal now (this chapter's project lab). It's an hour or two of work that makes the next sixteen chapters coherent. Every later chapter's project lab references "the capstone" — without a chosen capstone, those become abstract exercises instead of building one real thing.

## 5. How to Study Each Chapter

Each chapter is a standalone mini-course with a fixed structure (the chapter README lists the reading order). The effective study loop:

1. **Read `lesson.md` and `deep_dive.md`** — the conceptual and expert-track material. Take notes on what's new to you.
2. **Skim `examples.md`, `dictionary.md`, `references_numbered.md`** — patterns, terms, sources to return to.
3. **Do one project from `project_lab.md` end-to-end** — not three halfway. The Acceptance Criteria are the bar.
4. **Self-test with `question_bank.md` and `quiz.md`** — wrong answers go in a failure log.
5. **Commit the artifact to `my_work/`** — the proof the chapter is done.

The non-negotiable: **if you can't point to a file in `my_work/`, the chapter isn't done.** Reading is necessary but not sufficient. The artifact — code, schema, eval report, decision record, threat model — is what makes the learning real and reviewable.

## 6. The Artifact-Per-Chapter Map

Every chapter leaves a concrete artifact that feeds the capstone. This is the spine of the course (the repo's `COURSE_MAP.md` has the full table):

- Ch 1: typed service skeleton with provider adapters.
- Ch 2: SQL schema (documents → answers → audit) + named queries.
- Ch 3: the HTTP API contract (OpenAPI, error contract, streaming).
- Ch 4: one-command stack + CI + release manifest.
- Ch 5: prompt registry + injection test set.
- Ch 6: retrieval benchmark + cross-tenant test.
- Ch 7: end-to-end RAG with citations + no-answer.
- Ch 8: retrieval experiment harness + router.
- Ch 9: golden set + eval runner + release gate.
- Ch 10: agent graph + tool policy + approval gates.
- Ch 11: vendor-neutral architecture + migration plan.
- Ch 12: observability + runbooks + rollback drill.
- Ch 13: latency budget + tenant-safe cache + serving matrix.
- Ch 14: adaptation decision memo (often: don't fine-tune).
- Ch 15: threat model + guardrail suite + PII policy.
- Ch 16: integrated capstone + portfolio + interview kit.

By chapter 16, these aren't sixteen separate things — they're one system, and you assembled it incrementally instead of cramming at the end.

## 7. The Three Reusable Templates

Three artifacts recur across chapters; standardise them in chapter 00 and reuse them everywhere:

- **The decision record**: a short doc capturing a choice — context, options, the decision, the tradeoff, the evidence, the rollback plan. Used for model choice, vector DB, chunking, reranking, serving, adaptation. These become your interview tradeoff stories (chapter 16).
- **The failure log**: a table of failed cases — what was expected, what happened, the root cause, the fix, the regression test added. The fastest path to robustness, and the source of your incident STAR stories.
- **The evidence checklist**: per concept — explained in your own words? working artifact? eval/test evidence? failure analysis? sources linked? The self-assessment that keeps you honest about whether a chapter is actually done.

Set up these templates now (this chapter's project lab) so every later chapter has somewhere to put its thinking.

## 8. How Evidence Compounds

The reason the artifact discipline matters beyond tidiness: evidence compounds into a portfolio and an interview narrative. The decision records become tradeoff answers. The failure log becomes incident stories. The eval report becomes the "how do you know it works?" answer. The threat model becomes the security answer. The architecture pack becomes the whiteboard you've already drawn.

A learner who keeps the artifacts arrives at chapter 16 with the portfolio and interview kit *almost already written* — they harvest, they don't invent. A learner who skipped them has to manufacture all of it under deadline pressure and it shows. The cheap, boring habit of committing an artifact per chapter is what makes the expensive, high-stakes moment (the interview, the public repo) easy.

## 9. Pace and the Two Tracks

Pick a sustainable pace and protect it (the syllabus has detailed schedules):

- **Standard expert track**: 16–20 weeks, 8–12 h/week. One chapter per ~1.5 weeks, most of the time on the project lab.
- **Intensive track**: 10–12 weeks, 15–20 h/week. One chapter per week.
- **Interview sprint** after completion: ~10 days of mock interviews and system-design drills, drawing on the artifacts you kept.

The chapters get harder in the middle (5–10, the LLM/RAG/agent core) and the project labs there deserve extra time. The foundations (1–4) go faster if you have backend experience but shouldn't be skipped — the whole system sits on them. The two failure modes to actively resist remain tool-collection and demo-thinking; the pace matters less than the discipline of one measured artifact per chapter.

## 10. Common Mistakes and Anti-Patterns

1. **Skipping the capstone proposal.** The rest of the course loses its spine.
2. **Picking a domain whose corpus you can't legally use.** Stalls at ingestion.
3. **Tool collection** instead of integration.
4. **Demo thinking** — stopping before evaluation, security, ops.
5. **No `my_work/` artifacts.** Learning that can't be proven.
6. **Reading all chapters, doing no project labs.** Forgotten by mid-course.
7. **Not keeping decision records and failure logs.** Interview material invented under pressure later.
8. **A capstone with no real risk.** Safety/eval work becomes theatre.
9. **Over-scoping the capstone.** Never finished.
10. **Changing tools mid-course** without a measured reason.

## 11. Setting Up for Success

Before chapter 1, set up:

- A git repo for your `my_work/` artifacts (or use this course repo's chapter folders).
- The three templates (decision record, failure log, evidence checklist).
- A written capstone proposal: domain, users, corpus, success metric, top risks, non-goals.
- A roadmap mapping each chapter to the artifact it will produce for your capstone.
- A realistic pace commitment you can sustain.

This is an afternoon of setup that pays back for the whole course. The learner who does it starts chapter 1 building toward something; the learner who skips it starts chapter 1 doing a disconnected exercise.

## 12. The Capstone Checklist (for This Chapter)

By the end of chapter 00, the following should exist in `chapters/00_orientation/my_work/`:

- `capstone_proposal.md`: domain, users, corpus (and its legal usability), success metric, top 3–5 risks, non-goals. Under ~600 words but complete.
- `roadmap.md`: each chapter mapped to the concrete artifact it will leave for the capstone, with an evidence checkpoint.
- `decision_log.md`: the template, with the first entry already written (e.g. "why this domain?").
- A `failure_log.md` and `evidence_checklist.md` template ready for later chapters.

If a peer can read your proposal cold and tell you who the users are, what success looks like, and what the top risk is — without asking you — chapter 00 is done and the course has a spine.

## 13. Key Takeaway

This course trains the judgment to build, measure, operate, secure, and explain production AI — not the ability to recite tools. The decisive move is here in chapter 00: choose a capstone in a high-accuracy domain, with a real corpus, real users, a measurable success criterion, and genuine risk. Then study by doing one measured project per chapter and committing the artifact, so evidence compounds into a portfolio and an interview narrative. Integration and evidence beat breadth and enthusiasm — start the capstone now and build it incrementally.

## Numbered References

[1] OpenAI platform documentation: https://platform.openai.com/docs
[2] LangGraph overview: https://docs.langchain.com/oss/python/langgraph/overview
[3] LlamaIndex RAG overview: https://developers.llamaindex.ai/python/framework/understanding/rag/
[4] OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
