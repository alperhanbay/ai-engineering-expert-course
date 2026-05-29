# Homework: Docker, Linux, Git, and CI/CD

Graded against `../../syllabus/evaluation_rubric.md`. Outputs under `my_work/`.

## Required

1. **Multi-stage Dockerfile.** Build an image for your chapter 03 FastAPI
   app. Multi-stage, pinned base, non-root user, healthcheck, exec-form CMD.
   Record `docker image ls` in `my_work/image_size.md`. Target final size
   under 500 MB.

2. **`.dockerignore`.** Exclude `.venv`, `__pycache__`, `tests/fixtures/*`,
   `*.ipynb`, etc. Verify build context size is under 5 MB with
   `du -sh .` after dockerignore.

3. **docker-compose stack.** `api + postgres + qdrant` (or your chosen
   vector DB) with healthchecks, `depends_on: service_healthy`, named
   volumes, and a `--profile observability` block for Jaeger/Prometheus.
   `docker compose up` reaches a healthy `/healthz` on a fresh clone.

4. **`.env.example`.** Every required env var listed, with placeholders
   and a one-line comment per var. No real values committed.

5. **pre-commit hooks.** Install `ruff`, `ruff-format`, trailing-whitespace,
   end-of-file-fixer, check-yaml, check-added-large-files (max 500 KB),
   and a secret detector. Run on the repo, commit any fixes.

6. **CI pipeline.** GitHub Actions workflow with jobs: lint, type, unit,
   contract (with postgres service), docker build, eval smoke. Parallel
   where possible, gated by `needs`. Cache `uv` and Docker layers. Target
   PR pipeline duration: under 10 minutes.

7. **Release manifest.** Add a `release_manifest.yaml` template plus a CI
   step that fails the build if the manifest is missing any required field
   or if `eval_release_gate != pass` and no `manual_review` field is set.

8. **Rollback drill.** Document a tabletop rollback in
   `my_work/rollback_drill.md`: simulate "release N has a broken prompt;
   restore release N-1". Step-by-step, time each step, target under 5
   minutes.

## Stretch

9. **Image signing.** Sign your CI-built image with Cosign and verify the
   signature in a deploy step. Document in `my_work/image_signing.md`.

10. **Read-only root filesystem.** Add `read_only: true` to your
    docker-compose `api` service and identify what additional writable
    volumes you need. Justify each one.

11. **Linting that fails the build.** Add `mypy --strict` for one module
    and prove it fails CI when a type error is introduced.

12. **Trivy scan.** Add a `trivy` step to CI that fails on HIGH/CRITICAL
    CVEs in the built image. Document one CVE you fixed (likely by
    bumping a base image).

## Acceptance

- `docker compose up --build` on a fresh clone reaches a healthy
  `/healthz` in under 60 seconds (after the first cold build).
- CI passes on a clean PR; an intentional violation (lint, type, contract,
  manifest) causes the right job to fail.
- The rollback drill is reproducible from `my_work/rollback_drill.md` by
  a teammate without further explanation.
