# Lesson: Docker, Linux, Git, and CI/CD for AI Systems

## 1. Reproducibility Is a Feature

A working AI system that nobody else can reproduce is a liability. The user-visible value of "reproducibility" is invisible until you need it — and then it is everything: a contributor who can run the stack in 15 minutes, a CI job that finds a bug your laptop hides, a rollback that restores not just code but the prompt and the index that went with it, an auditor who can rebuild the system that produced a specific answer six months ago.

Reproducibility is not a single tool. It is a discipline that crosses four layers:

- **Linux**: predictable runtime environment, signals, processes, filesystems, logs.
- **Docker**: the container image as an immutable, versioned unit of deployment.
- **Git**: the commit graph as the single source of truth for code and configuration.
- **CI/CD**: automated, gated, repeatable build → test → release.

In an AI system, all four matter more than in a typical backend service because *the unit of behaviour is not just code*. A prompt change, a model upgrade, an index rebuild, an embedding model swap — each of those can change the system's output without touching a line of application code. Reproducibility means *every one of those artifacts is versioned, signed, and rolled back as a unit*. This chapter teaches you to build that habit before you have a production incident that requires it.

## 2. The Linux Surface You Actually Need

You do not need to be a kernel developer. You do need fluency with the small set of Linux concepts that appear in every production incident and every container build.

**Processes and signals.** Your service is a process; container orchestrators kill it with `SIGTERM` and expect a graceful shutdown within a grace period (default 30 s in Kubernetes, configurable everywhere). If your handler does not drain in-flight requests on `SIGTERM`, you will drop user requests on every deploy.

```python
import asyncio
import signal


async def main():
    shutdown_event = asyncio.Event()
    loop = asyncio.get_running_loop()

    for sig in (signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(sig, shutdown_event.set)

    server = await start_server()
    await shutdown_event.wait()
    await server.shutdown(timeout=20)   # drain in-flight requests, then exit
```

If your framework already handles signals (Uvicorn does, with `--timeout-graceful-shutdown`), use it instead of reinventing.

**File descriptors and ulimits.** A worker that holds many open connections (LLM streams, DB pool, vector store) can hit the default ulimit (often 1024). Set it in your Docker base image and in the orchestrator manifest. The first time this bites you it will look like "random connection refused" under load.

**Filesystems.** Containers' overlay filesystems are slow for write-heavy paths. Mount a volume for anything you write often (logs, temp files, model caches). The `/tmp` inside a container is not the same as the host's.

**journalctl, dmesg, top, htop, lsof, ss, strace.** You will use these in every incident. The two non-obvious ones:

- `lsof -p <pid>` shows what files and sockets a process has open. Helpful when "connections are leaking somewhere".
- `strace -p <pid>` shows the system calls a stuck process is making. Helpful when "the service is hung on... something".

You do not need to memorise them; you need to know they exist so you reach for them instead of restarting and hoping.

## 3. The Dockerfile: An Image You Can Defend in Review

A Dockerfile is the most-reviewed file in any AI service. A few rules separate a "works on my machine" image from a production-ready one:

```dockerfile
# syntax=docker/dockerfile:1.7

# ---- stage 1: build dependencies ----
FROM python:3.11-slim-bookworm AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync --frozen --no-dev

# ---- stage 2: runtime ----
FROM python:3.11-slim-bookworm AS runtime

RUN groupadd --system app && useradd --system --gid app --home /app app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:${PATH}"

WORKDIR /app

# Copy the virtualenv from the builder, then app code.
COPY --from=builder --chown=app:app /app/.venv ./.venv
COPY --chown=app:app src ./src

USER app

EXPOSE 8000
HEALTHCHECK --interval=10s --timeout=3s --start-period=20s --retries=3 \
    CMD ["python", "-c", "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://localhost:8000/healthz', timeout=2).status == 200 else 1)"]

# Use exec form so signals reach the Python process directly.
CMD ["uvicorn", "src.ai_service.api.main:app", \
     "--host", "0.0.0.0", "--port", "8000", \
     "--workers", "1", "--timeout-graceful-shutdown", "20"]
```

What is *deliberate* in there:

- **Pinned base image**, not `python:latest`. `latest` is a moving target; reproducible builds need a stable tag.
- **Multi-stage build.** The build stage has compilers and dev tooling; the runtime stage doesn't. Final image is small, fewer CVEs.
- **Non-root user.** A container running as root is a finding in every security review. Create a system user, `USER app`, and stick with it.
- **`HEALTHCHECK` defined in the image.** Even if your orchestrator uses its own probe, the in-image healthcheck helps `docker compose up` know when to call the service "ready".
- **`CMD` in exec form** (the array form, not the string form). Shell form launches a `/bin/sh -c "..."`, which doesn't forward signals. With exec form, `SIGTERM` reaches your Python process directly so your graceful shutdown actually runs.
- **`--workers 1` in the container.** One container, one worker process. Scale by adding *containers*, not by stuffing workers into one. The orchestrator handles parallelism.
- **`PYTHONUNBUFFERED=1`.** Without it, Python buffers stdout and your logs disappear into the void until the buffer flushes.

The image you don't want to ship:

- 1.2 GB because it includes `git`, `vim`, `curl`, dev headers, `gcc`, and pip's wheel cache.
- Running as root.
- A `RUN apt-get update && apt-get install -y python3 vim curl git build-essential ...` line with no cleanup.
- A `CMD bash -c "uvicorn ..."` that breaks signal handling.

A useful rule: if the final image is larger than 500 MB for a Python AI service, something is wrong. Investigate.

## 4. Pinning and Reproducibility

Dependencies must be pinned. Not pinned-ish. Pinned with a lockfile.

- **`uv.lock`**, `poetry.lock`, `pip-compile`'s `requirements.txt`, or PDM's lock — pick one and commit it.
- `pyproject.toml` declares the ranges (`fastapi>=0.110,<0.120`); the lockfile records the exact resolved versions (`fastapi==0.115.6`).
- CI installs from the lockfile, never resolves fresh in CI.

The reason: an unconstrained `pip install fastapi` will install whatever was published last week. Your image becomes a different image every time it's built. Reproducibility dies. The first time a transitive dependency ships a breaking change at 2 a.m., you'll appreciate the lockfile.

For non-Python dependencies (system packages), the base image tag (`python:3.11-slim-bookworm`) gives you a snapshot in time. If you must pin even harder, use a digest: `python@sha256:abc...`. Most teams don't, and that's fine; the slim tag is reasonably stable.

## 5. docker-compose: The Local Stack

`docker-compose.yml` is how a new contributor goes from `git clone` to a working stack in one command. Treat it as part of the product.

```yaml
services:
  api:
    build: .
    ports:
      - "8000:8000"
    env_file: .env
    depends_on:
      postgres:
        condition: service_healthy
      qdrant:
        condition: service_started
    healthcheck:
      test: ["CMD", "curl", "-fsS", "http://localhost:8000/healthz"]
      interval: 5s
      timeout: 3s
      retries: 5

  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: ai
      POSTGRES_PASSWORD: ai
      POSTGRES_DB: ai
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./scripts/init.sql:/docker-entrypoint-initdb.d/init.sql
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ai"]
      interval: 5s
      timeout: 3s
      retries: 10

  qdrant:
    image: qdrant/qdrant:latest
    volumes:
      - qdrant_data:/qdrant/storage

  jaeger:
    image: jaegertracing/all-in-one:latest
    ports:
      - "16686:16686"
    profiles: ["observability"]   # only starts with --profile observability

volumes:
  pgdata:
  qdrant_data:
```

Things that pay back:

- **`depends_on: condition: service_healthy`** instead of `service_started`. Without it, the API starts before Postgres is ready and the first request is a flake.
- **`profiles`** for optional services (observability, evaluation runners). `docker compose up` brings the minimum stack; `docker compose --profile observability up` brings Jaeger/Prometheus too.
- **Volumes for stateful services**. Without them, `docker compose down` deletes your work. With them, you can shut down and resume.
- **An init.sql** mounted into Postgres for the schema. Faster than running migrations on every startup.

Document the one-command setup in your top-level README:

```bash
cp .env.example .env       # fill in any required values
docker compose up --build  # api + postgres + qdrant
make test                  # runs unit + contract + integration
```

If those three lines don't get a contributor to a working state, the local stack is incomplete.

## 6. Git: Commits as a Communication Tool

Git is your release-history database, your blame source, your rollback graph. Treat commits as messages to a future engineer (often you) who has lost all context.

**Commit hygiene that pays back:**

- One logical change per commit. "fix typo + refactor service + add feature" is three commits.
- Commit messages with a subject (under 72 chars) and a body that explains *why*. The "what" is in the diff.
- Reference the issue or ticket in the body, not the subject.
- Squash WIP commits before merging; keep the public history clean.

**Branch strategy.** For small teams, `main`-and-feature-branches works. For larger teams, GitHub Flow (short-lived feature branches → PR → merge to `main` → deploy) is robust. Avoid `git flow` (`develop` + `release/*` + `hotfix/*`) unless you genuinely need release branches.

**Hooks worth installing.** `pre-commit` (the framework, not the git hook) lets you run formatters and linters locally on every commit:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
        args: [--maxkb=500]
```

The first time you accidentally commit a 30 MB pickle, the `check-added-large-files` hook will save you the embarrassment of force-pushing.

**Never commit secrets.** Add a tool to your hooks (`detect-secrets`, `gitleaks`) and run it in CI too. If a secret ever lands in a commit, rotate it immediately — git rebases do not actually remove it from forks and caches.

## 7. The CI Pipeline: Tiered for AI

AI services have an extra cost dimension that traditional services do not: model evals. A full eval suite may take 10–30 minutes, cost real money in API calls, and produce results that are sometimes noisy. Running them on every PR is too slow and too expensive; not running them at all is reckless. The solution is *tiering*.

A workable pipeline:

```yaml
# .github/workflows/ci.yml
name: ci
on: [pull_request, push]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
      - run: uv sync --frozen
      - run: uv run ruff check .
      - run: uv run ruff format --check .

  type:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
      - run: uv sync --frozen
      - run: uv run mypy src

  unit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
      - run: uv sync --frozen
      - run: uv run pytest tests/unit -q

  contract:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16-alpine
        env: {POSTGRES_USER: ai, POSTGRES_PASSWORD: ai, POSTGRES_DB: ai}
        ports: ["5432:5432"]
        options: --health-cmd="pg_isready -U ai" --health-interval=5s
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
      - run: uv sync --frozen
      - run: uv run alembic upgrade head
      - run: uv run pytest tests/contract tests/integration -q

  docker:
    runs-on: ubuntu-latest
    needs: [lint, type, unit]
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v3
      - uses: docker/build-push-action@v5
        with:
          context: .
          push: false
          tags: ai-service:ci
          cache-from: type=gha
          cache-to: type=gha,mode=max

  eval_smoke:
    runs-on: ubuntu-latest
    needs: [unit, contract]
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
      - run: uv sync --frozen
      - run: uv run python scripts/eval_smoke.py    # one golden case, fake LLM
```

Notes:

- **Five jobs in parallel** for fast feedback. Lint and type don't depend on anything; unit doesn't depend on type; contract doesn't depend on docker.
- **`needs: [...]`** gates the expensive jobs on the cheap ones. Docker build runs only if lint/type/unit pass.
- **`eval_smoke`** is a single golden case with a fake LLM (`temperature=0`, deterministic) to verify the *plumbing* still wires up end-to-end. Total cost: zero dollars; total time: seconds.
- **Full eval runs separately**, on a schedule or on demand, not on every PR. Tag PRs that need it (`labels: needs-eval`) and run the suite only when the label is present.

Cache aggressively: `uv` (or `pip`) cache, Docker layer cache, mypy cache. The first PR of the day takes 8 minutes; subsequent ones take 90 seconds.

## 8. Secrets in CI

Never put a secret in a workflow file. Use the platform's secret store (GitHub Actions Secrets, GitLab Variables, etc.) and inject via environment.

```yaml
- name: eval against real provider
  env:
    OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY_TEST }}
  run: uv run pytest tests/eval/test_full.py
```

Rules:

- **Tier the secrets.** A "test" key with low rate limits and a small budget cap is what CI gets; production keys never appear in CI.
- **Mask secrets in logs.** GitHub Actions masks `secrets.X` automatically *only if you reference it through the `secrets` context*. If you `echo $SOMETHING` after assignment, it may be revealed; don't echo secrets.
- **Rotate on a schedule.** A leaked secret is far worse if it's been valid for two years.

If a secret leaks, *rotate first, investigate second*. The window between detection and rotation is what attackers exploit.

## 9. The Release Manifest

A code rollback in an AI system is incomplete. Reverting the application code does nothing about the prompt that shipped with it, the model id the request used, the index version the retriever consulted, or the eval results that gated the release. *Every* one of those changes can cause an incident, and the rollback must restore *all* of them.

Hence the release manifest — a small file that records, per release, the full set of versioned artifacts:

```yaml
# release_manifest.yaml
release_id: "2026-05-26-7ae4e08"
created_at: "2026-05-26T15:42:00Z"
git_sha: "7ae4e08"
docker_image: "ghcr.io/acme/ai-service@sha256:abc...123"
prompt_version: "rag_v4"
model_id: "gpt-4o-mini-2024-07-18"
embedding_model: "text-embedding-3-small"
index_version: "v17"
eval_dataset_version: "golden-v3"
eval_run_id: "run_4711"
eval_release_gate: "pass"
approved_by: "alperhanbay"
notes: |
  - rag_v4 changes the no-answer phrasing
  - index v17 re-chunked with section-aware splitter
```

The CI gate to enforce: a release is rejected unless `release_manifest.yaml` exists, has every field non-empty, and `eval_release_gate` is `pass` (or a `manual_review` flag is present with the reviewer named).

Rollback becomes: "fetch manifest of the last known-good release, deploy that image, set those artifact versions". Without the manifest, rollback is partial and the same bug recurs.

## 10. Versioning Strategy

A small but stable convention:

- **Calendar versions for releases**: `2026-05-26-7ae4e08` (date + short sha). Easy to sort, no semver wars.
- **Semver for libraries** you publish (rare in an AI service).
- **Prompt versions** are short strings (`rag_v4`, `summarise_v2`). Major change → new version. The old version stays accessible by name for rollback.
- **Index versions** are integers or dates (`v17`, `2026-05-13`). Incremented on any change that requires re-embedding.
- **Model ids** use the provider's exact deployment name, not a friendly alias. `gpt-4o-mini-2024-07-18`, not `gpt-4o-mini`. The alias may be updated by the vendor; the dated name is stable.

The non-obvious rule: *never overwrite a versioned artifact*. A prompt `rag_v4` ships once and never changes. Improvements ship as `rag_v5`. Likewise indexes: a re-build is `v18`, not "`v17` with new chunks". This is the only way rollback stays meaningful.

## 11. Linting, Type Checking, Security Scanning

Three CI jobs you should not skip:

1. **Lint and format** (`ruff`). Sub-second on a 50 KLoc codebase. Catches dead imports, unused variables, formatting drift.
2. **Type check** (`mypy` or `pyright`). Slower but catches the boundary mistakes the most. Run on the public service interface even if you can't get the whole codebase clean.
3. **Security scan** of the Docker image. `trivy` or `grype` are open-source and fast. A nightly scan catches CVEs in base images.

```yaml
- name: trivy scan
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: ai-service:ci
    severity: HIGH,CRITICAL
    exit-code: 1
```

`HIGH,CRITICAL` is the right starting bar — `MEDIUM` will swamp you with noise. Tighten over time.

## 12. Common Mistakes and Anti-Patterns

1. **`docker build .` without `.dockerignore`.** Sends your entire `.venv`, `__pycache__`, and `node_modules` to the daemon. Build is slow and the image bloats.
2. **`FROM python:latest`.** Builds become non-reproducible the moment the tag rolls.
3. **`RUN pip install -r requirements.txt` without a lockfile.** Same.
4. **Container as root.** A finding in every security review.
5. **`CMD ["bash", "-c", "uvicorn ..."]`.** Signals don't reach Python.
6. **Secrets in `ENV` instructions.** They're baked into image layers, visible to anyone with `docker pull` access.
7. **No `.env.example`.** New contributors guess which env vars are required.
8. **CI runs everything on every PR.** Eval suite costs $40 per PR; team works around CI by skipping it.
9. **`git commit -am` for everything.** Loses the discipline of staged changes; tests pass on uncommitted local edits and surprise CI.
10. **A `release` happens by hand, not via CI.** Releases drift from what was tested.

## 13. Production Failure Modes

- **Image build works locally, fails in CI** because a dev machine has a tool the CI runner doesn't. Defensive measure: build the image in CI and run *everything* against that image.
- **Container OOM-killed under load.** Cause: memory limits set lower than the worker actually uses (model client maintains in-memory cache). Defensive measure: load test with memory metrics; set limits to observed p99 + 30%.
- **Graceful shutdown doesn't.** Cause: long-running LLM call holds the worker past the grace period; orchestrator sends `SIGKILL`. Defensive measure: enforce per-request timeouts (chapter 03) so no request outlives the grace period.
- **A new dependency pulls in a transitive that segfaults under musl.** Cause: `python:3.11-alpine` (musl libc) vs `python:3.11-slim` (glibc). Defensive measure: use slim, not alpine, unless you have a compelling size reason.
- **The release manifest is filled in after deploy.** Cause: no CI gate. Defensive measure: gate fails if the manifest is missing or incomplete.
- **A revoked PR sneaks back in via a stale branch.** Cause: hotfix merged directly to `main` while a long-lived feature branch lagged. Defensive measure: short-lived branches; rebase before merging; CI on `main`.
- **CI passes; production breaks** because production has different env vars. Cause: drift between `.env.example` and actual production config. Defensive measure: a `validate_config` script that runs at container startup and fails fast.

## 14. Security at the Build and Deploy Layer

Six controls worth getting right before chapter 15 covers the application-layer security:

1. **Image signing.** Sign images with Cosign or Notary. Production deploy verifies the signature.
2. **Pinned base by digest.** `python@sha256:...` is stricter than `python:3.11-slim-bookworm`. Use digests for production images.
3. **Read-only root filesystem.** `--read-only` in `docker run`, or `securityContext.readOnlyRootFilesystem: true` in Kubernetes. Forces you to mount writable volumes explicitly, prevents most write-based attacks.
4. **Drop Linux capabilities.** `--cap-drop=ALL` and only `--cap-add` what you need (usually nothing).
5. **No host network or privileged mode.** Both are CI-failable.
6. **Secrets via the orchestrator**, not env-file-baked. Kubernetes secrets, Docker swarm secrets, Vault — any of them is better than a `.env` file shipped with the image.

## 15. The Capstone Checklist

By the end of chapter 04, the following should exist in `chapters/04_docker_linux_git_cicd/my_work/`:

- A `Dockerfile` with multi-stage build, pinned base, non-root user, healthcheck, exec-form CMD. Final image size documented.
- A `docker-compose.yml` for `api + postgres + vector_db` (plus optional observability via a `profiles` block).
- A `.env.example` with every required variable.
- A `.dockerignore` excluding `.venv`, `__pycache__`, `node_modules`, `tests/`, etc.
- A `pre-commit` config covering format, lint, trailing whitespace, large file check, secret detection.
- A CI workflow (GitHub Actions or equivalent) with jobs: lint, type, unit, contract, docker build, eval smoke. Parallel where possible; cached aggressively.
- A `release_manifest.yaml` template plus a CI gate that fails when the manifest is incomplete.
- A `RELEASING.md` documenting the release procedure (manifest, tag, deploy) and the rollback procedure (read manifest, deploy previous image, restore artifact versions).
- A short README in `my_work/` showing `docker compose up` in three commands and the expected output.

If a teammate can clone, `docker compose up`, hit `/healthz`, run the test suite, and read the release procedure — without asking you anything — the chapter is done.

## 16. Key Takeaway

Reproducibility is the boring layer that makes everything else possible. A small investment in Dockerfile discipline, lockfiles, CI tiering, and release manifests pays back every single time someone needs to roll back, reproduce, or onboard. AI changes the *content* of what you ship; it doesn't change the discipline of *how* you ship.

## Numbered References

[1] Docker documentation: https://docs.docker.com/
[2] Docker Compose: https://docs.docker.com/compose/
[3] Dockerfile reference: https://docs.docker.com/reference/dockerfile/
[4] Git documentation: https://git-scm.com/doc
[5] GitHub Actions documentation: https://docs.github.com/en/actions
