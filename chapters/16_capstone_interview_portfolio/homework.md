# Homework: Capstone, Portfolio, and Interview Readiness

Graded against `../../syllabus/evaluation_rubric.md`. This chapter integrates all
prior `my_work/`. Outputs under `my_work/`.

## Required

1. **Integrated capstone.** Assemble the prior chapters into one runnable repo:
   API + SQL + ingestion + RAG + agent + eval + observability + security. A
   stranger runs `docker compose up` and reaches a working `/ask` in minutes.

2. **Architecture pack.** Produce six one-page diagrams in
   `my_work/architecture_pack/`: system, data model, RAG flow, agent workflow,
   deployment, threat model. Each must match the code.

3. **Portfolio README.** Write `my_work/portfolio_README.md`: what it is, how to
   run, architecture, results (eval numbers per risk level), security (threat
   model + guardrail pass rate), limitations (≥3, honest), sources.

4. **Demo script.** Write `my_work/demo.md`: the 5-step repeatable demo
   (ingest, supported answer + citation, unsupported → refusal, eval run,
   blocked injection). Time it; target under 15 minutes from clean clone.

5. **Interview kit.** Write `my_work/interview_kit.md`: 5 STAR stories (failure,
   tradeoff, incident, scope cut, collaboration) each with a measured result; 3
   system-design walkthroughs that reach eval + failure modes + security; 10
   Q&A drills.

6. **Evidence traceability.** Ensure every numeric claim in the README traces to
   a committed eval run or trace. Add a `my_work/evidence_index.md` linking
   claims to their source artifacts.

## Stretch

7. **Record the demo.** Capture a screen recording or transcript of the demo
   running end-to-end on a clean clone.

8. **Mock interview.** Have a peer run a system-design and a behavioral round
   using your interview kit; record what questions you couldn't answer well and
   close those gaps.

9. **Public-repo hardening.** If public: LICENSE, contribution guidance, CI
   badge, secret scan of history, synthetic/redistributable corpus only.

## Acceptance

- A stranger runs the demo in under 15 minutes from a clean clone.
- The demo shows a refusal and a blocked injection, not just a working answer.
- Every README number traces to a committed artifact.
- At least three honest limitations are named with next steps.
