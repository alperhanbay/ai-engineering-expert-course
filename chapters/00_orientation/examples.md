# Examples: Orientation and Expert Roadmap

Templates matching `lesson.md`. Copy these into `my_work/` and fill them.

## 1. Capstone proposal template

```md
# Capstone Proposal: <name>

## Domain
<regulated/high-accuracy domain, e.g. insurance policy Q&A>

## Users
<specific user + their need, e.g. "claims adjusters checking filing deadlines">

## Corpus
<source documents + confirmation you can legally use/redistribute them>

## Success metric
<what a good answer looks like + how you'd score it, e.g. "correct deadline with
a verifiable citation; refuses when the policy doesn't cover the question">

## Risks (specific, not generic)
1. <e.g. hallucinated deadline -> missed claim -> legal liability>
2. <e.g. cross-tenant leak of one client's policy to another>
3. ...

## Non-goals
<what you will deliberately NOT build, e.g. "no multi-language; no live policy edits">
```

## 2. Roadmap template (artifact per chapter)

```md
# Capstone Roadmap

| Ch | Artifact for MY capstone                         | Evidence checkpoint |
|----|--------------------------------------------------|---------------------|
| 01 | typed service skeleton + fake providers          | tests pass, no network |
| 02 | schema for policies/chunks/answers/audit         | 6 named queries run |
| 03 | /ask, /documents, /feedback API + OpenAPI        | contract tests pass |
| 04 | docker-compose stack + CI + release manifest     | one-command up |
| 05 | prompt registry + injection tests                | injection set runs |
| 06 | retrieval benchmark + cross-tenant test          | recall@5 measured |
| 07 | end-to-end RAG + citations + no-answer           | unanswerable refuses |
| 08 | experiment harness + reranking decision          | baseline vs +rerank |
| 09 | 100-case golden set + release gate               | per-risk report |
| 10 | agent graph + approval gates                     | injection refused |
| 11 | vendor-neutral arch + migration plan             | provider swapped in dev |
| 12 | observability + runbooks + rollback drill        | MTTR < 5 min |
| 13 | latency budget + tenant-safe cache               | cross-tenant cache test |
| 14 | adaptation decision memo                         | lever justified |
| 15 | threat model + guardrail suite + PII policy      | OWASP mapped |
| 16 | integrated capstone + portfolio + interview kit  | 15-min demo |
```

## 3. Decision record template (reused all course)

```md
# Decision: <title>
Date: <date>   Owner: <name>
Context: <why this decision is needed>
Options: <A / B / C>
Chosen: <option> 
Tradeoffs: <what we give up>
Evidence: <measurement or reasoning supporting the choice>
Rollback/revision: <how to undo or revisit>
```

## 4. Failure log template (reused all course)

```md
| Date | Case/ID | Expected | Actual | Root cause | Fix | Regression test |
|------|---------|----------|--------|------------|-----|-----------------|
|      |         |          |        |            |     |                 |
```

## 5. Evidence checklist template (per concept)

```md
- [ ] Explained in my own words
- [ ] Working implementation or design artifact in my_work/
- [ ] Evaluation or test evidence
- [ ] Failure analysis (at least one failure mode tested)
- [ ] Source links from references_numbered.md
```

## 6. Peer-check record

```md
# Peer check on capstone proposal
Reviewer: <name>  Read time: <minutes>
Q: Who are the users?      A: <what they said>
Q: What is success?        A: <what they said>
Q: What is the top risk?   A: <what they said>
Verdict: <clear / needs revision>
Revision made: <what changed>
```

## 7. A good vs weak proposal (contrast)

```md
WEAK:  "A chatbot that answers questions using AI for businesses."
       (no users, no corpus, no success metric, no risk)

GOOD:  "An assistant for insurance claims adjusters that answers policy-deadline
       questions from the company's policy PDFs, cites the clause and page,
       and refuses when the policy is silent. Success = correct deadline +
       verifiable citation on the 100-case golden set; refuses 100% of
       unanswerable questions. Top risk: a hallucinated deadline causes a
       missed claim. Non-goals: no policy editing, English only."
```
