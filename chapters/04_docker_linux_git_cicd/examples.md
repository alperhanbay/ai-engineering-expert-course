# Examples: Docker, Linux, Git, and CI/CD

Reusable snippets matching `lesson.md`.

## 1. Multi-stage Dockerfile

```dockerfile
# syntax=docker/dockerfile:1.7
FROM python:3.11-slim-bookworm AS builder
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync --frozen --no-dev

FROM python:3.11-slim-bookworm AS runtime
RUN groupadd --system app && useradd --system --gid app --home /app app
ENV PYTHONUNBUFFERED=1 PATH="/app/.venv/bin:${PATH}"
WORKDIR /app
COPY --from=builder --chown=app:app /app/.venv ./.venv
COPY --chown=app:app src ./src
USER app
EXPOSE 8000
HEALTHCHECK --interval=10s --timeout=3s --start-period=20s --retries=3 \
    CMD ["python","-c","import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://localhost:8000/healthz',timeout=2).status==200 else 1)"]
CMD ["uvicorn","src.ai_service.api.main:app","--host","0.0.0.0","--port","8000","--timeout-graceful-shutdown","20"]
```

## 2. `.dockerignore`

```
.venv/
__pycache__/
*.pyc
.git/
.github/
tests/
*.ipynb
.env
.pytest_cache/
.mypy_cache/
.ruff_cache/
node_modules/
*.md
```

## 3. docker-compose with healthchecks

```yaml
services:
  api:
    build: .
    ports: ["8000:8000"]
    env_file: .env
    depends_on:
      postgres: {condition: service_healthy}
      qdrant: {condition: service_started}
  postgres:
    image: postgres:16-alpine
    environment: {POSTGRES_USER: ai, POSTGRES_PASSWORD: ai, POSTGRES_DB: ai}
    volumes: ["pgdata:/var/lib/postgresql/data"]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ai"]
      interval: 5s
      retries: 10
  qdrant:
    image: qdrant/qdrant:latest
    volumes: ["qdrant_data:/qdrant/storage"]
  jaeger:
    image: jaegertracing/all-in-one:latest
    ports: ["16686:16686"]
    profiles: ["observability"]
volumes: {pgdata: {}, qdrant_data: {}}
```

## 4. Graceful shutdown on SIGTERM

```python
import asyncio, signal

async def main():
    stop = asyncio.Event()
    loop = asyncio.get_running_loop()
    for s in (signal.SIGTERM, signal.SIGINT):
        loop.add_signal_handler(s, stop.set)
    server = await start_server()
    await stop.wait()
    await server.shutdown(timeout=20)   # drain in-flight requests
```

## 5. pre-commit config

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.0
    hooks: [{id: ruff, args: [--fix]}, {id: ruff-format}]
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - {id: trailing-whitespace}
      - {id: end-of-file-fixer}
      - {id: check-yaml}
      - {id: check-added-large-files, args: [--maxkb=500]}
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks: [{id: gitleaks}]
```

## 6. Tiered CI (GitHub Actions, abridged)

```yaml
name: ci
on: [pull_request, push]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
      - run: uv sync --frozen
      - run: uv run ruff check . && uv run ruff format --check .
  unit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
      - run: uv sync --frozen
      - run: uv run pytest tests/unit -q
  docker:
    needs: [lint, unit]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v3
      - uses: docker/build-push-action@v5
        with: {context: ., push: false, tags: "ai-service:ci", cache-from: "type=gha", cache-to: "type=gha,mode=max"}
  eval_smoke:
    needs: [unit]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
      - run: uv sync --frozen
      - run: uv run python scripts/eval_smoke.py
```

## 7. Release manifest

```yaml
release_id: "2026-05-26-7ae4e08"
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
```

## 8. Manifest gate (CI step)

```python
# scripts/check_manifest.py
import sys, yaml

REQUIRED = ["release_id","git_sha","docker_image","prompt_version","model_id",
            "embedding_model","index_version","eval_dataset_version",
            "eval_run_id","eval_release_gate","approved_by"]

m = yaml.safe_load(open("release_manifest.yaml"))
missing = [k for k in REQUIRED if not m.get(k)]
if missing:
    sys.exit(f"manifest missing/empty fields: {missing}")
if m["eval_release_gate"] != "pass" and "manual_review" not in m:
    sys.exit("eval gate not 'pass' and no manual_review override present")
print("manifest ok")
```

## 9. Trivy scan step

```yaml
- name: trivy
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: ai-service:ci
    severity: HIGH,CRITICAL
    exit-code: 1
```

## 10. Useful incident commands

```bash
lsof -p <pid>            # open files + sockets for a process
ss -tanp | grep <pid>    # network connections
strace -p <pid>          # syscalls a stuck process is making
journalctl -u ai-service -f --since "10 min ago"
docker stats             # live CPU/mem per container
docker logs --tail 100 -f <container>
```

## 11. Makefile that ties it together

```makefile
.PHONY: up test lint type
up:      ; docker compose up --build
test:    ; uv run pytest tests/unit tests/contract -q
lint:    ; uv run ruff check . && uv run ruff format --check .
type:    ; uv run mypy src
release: ; python scripts/check_manifest.py && ./scripts/deploy.sh
```
