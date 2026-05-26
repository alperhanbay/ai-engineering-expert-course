# Quality Checks

The course has a deliberately strict validator. It is not a linter — it
encodes the editorial rules the course has been bitten by in prior iterations
(generic dictionary definitions, template fill-in questions, identical
project-lab boilerplate across every chapter).

If you contribute content, run the validator before opening a PR. If the
validator fails, fix the underlying issue; do not weaken the rule unless you
have a clear reason.

## How to run

From the repo root:

```bash
python3 tools/validate_course_quality.py
```

Exit status `0` = passing. Non-zero = one issue per line, with the file path
and the rule that triggered.

## What it checks

### Per-chapter file presence

Every chapter directory under `chapters/` must contain all of:

```
README.md
lesson.md
deep_dive.md
examples.md
homework.md
quiz.md
question_bank.md
projects.md
project_lab.md
dictionary.md
resources.md
references_numbered.md
```

A missing file produces:
`chapters/<dir>/<file>: required chapter file missing`.

### Forbidden generic phrases

The course has been burned by these patterns. They are blocked anywhere they
appear:

- `To master ...document its definition, implementation role, failure mode, metric, and ________ reference`
- `A core term in <Chapter>`
- `Beginner Level` / `Intermediate Level` / `Advanced Level`
- `Beginner Requirements` / `Intermediate Requirements` / `Advanced Requirements`

If a phrase like the last one is meaningful to your contribution, add it under
a different heading or argue in the PR for removing it from the list — don't
silently work around it.

### `question_bank.md`

Required sections:

- `## Multiple Choice` (≥ 6 items)
- `## Applied Multiple Choice` (≥ 4 items)
- `## Fill In The Blanks` (≥ 6 items, no duplicates)
- `## Short Answer` (≥ 4 items)
- `## Scenario Questions` (≥ 4 items)
- `## Practical Debug Questions` (≥ 4 items)
- `## Answer Key` with subsections for Multiple Choice, Applied Multiple Choice, Fill In The Blanks
- `## References`

Anti-template rule: if ≥ 50% (and at least 3) of items in Multiple Choice,
Fill In The Blanks, or Scenario Questions start with the same 5-6 word prefix,
the file fails with a "share the same template" message. The generator uses
rotating templates to prevent this; if you hand-edit, vary the stems.

### `dictionary.md`

- At least 5 term rows (`| \`term\` | … |` format).
- No duplicate definition columns across rows.
- No placeholder phrases like `specific concept in <chapter>` or `needs an explicit, non-generic definition`.

### `deep_dive.md`

- At least 1500 characters.
- Must contain sections `## Thesis`, `## Core Concepts`, `## Production Failure Modes`, `## References`.
- `## Production Failure Modes` must be at least 200 characters of content.

### `project_lab.md`

- At least 2500 characters.
- Must contain `## References`.
- Must mention `Acceptance Criteria`, `Metric`, and `Failure` somewhere.

### `lesson.md`

- Must end with `## Numbered References` or `## References`.

### `references_numbered.md`

- At least 4 entries in `[N]` format.

### Cross-file checks

- The `## Practical Debug Questions` block must not be byte-identical across
  more than 3 chapters. This caught the old generator emitting the same 5
  questions in every chapter.
- The opening paragraph of `project_lab.md` must not be byte-identical across
  more than 3 chapters. This caught the old uniform "portfolio-grade
  assignments" intro.

## How to extend the validator

The file is `tools/validate_course_quality.py`. Add a new check as:

1. A pure function `check_X(path: Path) -> list[str]` that returns one
   message per violation.
2. A call from `main()`.

Tests are inline — run the validator against current content; if it should
fail and doesn't, the check is wrong. If you add a check that the current
content already violates, fix the content in the same PR.

## How regenerated files relate to the validator

`tools/generate_expansion.py` regenerates these files from per-chapter data
in the same script:

- `deep_dive.md`
- `question_bank.md`
- `project_lab.md`
- `dictionary.md`
- `references_numbered.md`
- chapter `README.md`
- `## Numbered References` section appended to `lesson.md` if missing

If you edit one of these directly, the next `python3 tools/generate_expansion.py`
will overwrite your change. To make a durable change, edit the corresponding
data in `tools/generate_expansion.py` (chapter dicts, `TERM_DETAILS`, or
`LAB_OVERLAYS`).

`lesson.md`, `examples.md`, `homework.md`, `quiz.md`, `projects.md`,
`resources.md`, and `chapters/*/my_work/` are not regenerated — edit them
freely.
