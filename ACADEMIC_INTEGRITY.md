# Academic Integrity and AI-Tool Policy

This course is delivered in 2026, when generative AI is a normal part of how
engineers write code. The policy is permissive but explicit. Read it once.

## Principles

1. **You are responsible for everything you submit.** "The AI wrote it" is
   not an excuse. If you can't explain a line in your project, it shouldn't
   be in your project.
2. **Disclose your tool use.** Honesty about what an AI helped with is
   *not* penalised; concealment is.
3. **Sources are mandatory.** Every external claim in your work cites a
   source — vendor doc, paper, repo. No exceptions for AI output.
4. **Capstone-scale fabrication fails the course.** A capstone that doesn't
   run, or whose results can't be reproduced from the committed artifacts, is
   academic misconduct regardless of where the text came from.

## What is allowed

- Using an AI assistant (Claude, ChatGPT, Copilot, Cursor, etc.) for:
  - drafting prose you then read, edit, and verify;
  - generating boilerplate (schemas, route handlers, config templates);
  - explaining unfamiliar APIs to you;
  - reviewing your code for bugs and clarity.
- Using public code (Stack Overflow, GitHub repos) — cite the source.
- Pair-programming with classmates on the structure of a solution.
- Using your favourite IDE's autocomplete.

## What is not allowed

- **Submitting AI-generated content you have not read and understood.**
  An oral spot-check during grading will catch this.
- **Concealing AI use** when it materially shaped a deliverable. The
  acknowledgement section in your README is mandatory (template below).
- **Copying another student's deliverable** — pair-programming the structure
  is fine; submitting the same code is not.
- **Fabricating evaluation results.** Numbers must trace to a committed eval
  run or trace. This is the single most serious violation in this course.
- **Fabricating citations.** A URL must be real and contain the claimed content.
- **Using the test set during training/development.** Held-out is held-out.
  Hash-check it (see ch14).

## The acknowledgement section

Every chapter's `my_work/` and the capstone repo must contain a section like:

```markdown
## AI tool use

- I used <Claude / ChatGPT / Copilot / ...> for: <e.g. drafting the README,
  generating SQL skeletons, explaining FastAPI dependency injection>.
- I did NOT use AI tools for: <e.g. the eval results, the threat model,
  the design tradeoff in decision_record.md>.
- The following parts were AI-drafted and edited by me: <list>.
- I verified every external claim against an authoritative source.
```

A missing or empty acknowledgement is a 10% grade penalty per assignment.
A false acknowledgement is academic misconduct.

## Special case: the RAG corpus

Your capstone uses someone else's documents (open standards, project docs,
or synthetic data). The corpus is *evidence*, not your writing. Rules:

- Use only documents you can legally include or redistribute.
- Cite the corpus source in `portfolio_README.md`.
- Generated answers must cite the chunk (document + page/section).
- You may NOT claim the corpus content as your own analysis.

## Special case: evaluation results

The course's release-gate discipline depends on evaluations being honest.

- Every numeric claim in your portfolio README → a committed eval run id or
  trace. The `evidence_index.md` from ch16 is the audit trail.
- Re-running the eval on a clean clone must reproduce the reported numbers
  within noise. Numbers that can't be reproduced are treated as fabricated.

## Special case: paper notes

Notes on the seminal papers (`syllabus/papers_to_read.md`) count for
participation. Rules:

- AI-summarised paper notes don't count. You read the paper.
- Quote sparingly with attribution.
- Your "one critical question" per paper must be yours.

## What happens when violations are caught

1. **First minor violation** (e.g. missing acknowledgement): 10% penalty,
   resubmit with acknowledgement.
2. **Fabricated citation or eval result**: zero on the assignment + report to
   the academic-integrity office.
3. **Capstone misconduct**: course fail.

The instructor will spot-check during oral grading by asking you to:

- Explain a function in your code.
- Justify a design choice.
- Show how a reported number was measured.

If you wrote it (or understand what an AI drafted), this takes 60 seconds.
If you didn't, no policy text saves you.

## A final note on intent

The policy isn't "AI is bad." It's "you're an engineer, not a passthrough."
The market will pay you for the parts AI can't do reliably: judgement,
verification, integration, debugging under uncertainty. Practice those.
