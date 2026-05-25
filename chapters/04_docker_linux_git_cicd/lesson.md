# Lesson: Docker, Linux, Git, and CI/CD

## 1. Why Deployment Foundations Matter

An AI service that only works on your laptop is not production-ready. Docker, Linux, Git, and CI/CD make your system reproducible, testable, reviewable, and deployable.

LLM/RAG systems often depend on:

- API service;
- SQL database;
- vector database;
- object storage;
- background workers;
- evaluation runner;
- model serving endpoint;
- monitoring tools.

Docker Compose is useful for local integration testing because it can run many services together.

## 2. Linux Basics

You should be comfortable with:

- filesystem navigation;
- environment variables;
- processes;
- ports;
- logs;
- permissions;
- shell scripts;
- package installation;
- networking basics.

AI deployment debugging often begins with:

```bash
ps
netstat or ss
curl
tail
env
df
du
top or htop
```

## 3. Git Workflow

A strong workflow:

```text
main
  -> feature branch
  -> commit small changes
  -> tests
  -> pull request
  -> review
  -> merge
  -> tagged release
```

For AI systems, version not only code but also:

- prompts;
- evaluation datasets;
- index versions;
- model configuration;
- migration files;
- experiment reports.

## 4. Docker Concepts

| Concept | Meaning |
| --- | --- |
| image | packaged filesystem and metadata |
| container | running instance of an image |
| Dockerfile | build instructions |
| volume | persistent or mounted storage |
| network | container communication layer |
| Compose | multi-container local stack |

## 5. Dockerfile Design

Good Dockerfiles:

- use a specific base image;
- install only necessary dependencies;
- copy dependency files before source code for caching;
- do not store secrets;
- run as non-root when possible;
- include health checks where appropriate.

## 6. Docker Compose for AI Systems

Common local stack:

```text
api
postgres
qdrant
redis
worker
mlflow
prometheus
grafana
```

Not every project needs all of these, but you should understand the roles.

## 7. Environment and Secrets

Use `.env.example` to document required variables, but never commit real secrets.

Examples:

```text
DATABASE_URL=
VECTOR_DB_URL=
OPENAI_API_KEY=
MODEL_PROVIDER=
LOG_LEVEL=
```

Production secrets should come from a secret manager or deployment platform, not from the image.

## 8. CI/CD

CI should catch:

- formatting errors;
- type errors;
- unit test failures;
- API contract changes;
- migration issues;
- basic security issues;
- evaluation regressions for small smoke sets.

Full LLM evaluations can be expensive, so split:

- fast checks on every pull request;
- deeper evals on scheduled jobs or release candidates.

## 9. Release and Rollback

AI releases may include:

- code;
- prompt;
- model config;
- vector index;
- embedding model;
- reranker;
- eval dataset.

Rollback must know which artifact changed.

Example:

```text
release_2026_05_25:
  code: git sha
  prompt: rag_v5
  index: legal_idx_2026_05
  model: provider_model_x
  eval_dataset: golden_v3
```

## 10. Key Takeaway

Deployment foundations are part of AI expertise. A strong AI engineer can run the whole stack locally, test it in CI, deploy it reproducibly, and roll it back when quality or reliability drops.
## Numbered References

[1] Docker documentation: https://docs.docker.com/
[2] Docker Compose: https://docs.docker.com/compose/
[3] Dockerfile reference: https://docs.docker.com/reference/dockerfile/
[4] Git documentation: https://git-scm.com/doc
[5] GitHub Actions documentation: https://docs.github.com/en/actions
