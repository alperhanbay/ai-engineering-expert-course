# Deep Dive: Docker, Linux, Git, and CI/CD

## Thesis

Reproducibility, reviewability, and rollback are part of AI engineering. This file expands the chapter beyond the basic lesson and connects it to current practice, project work, and verifiable sources.

## Core Concepts

### `container`

A running isolated process created from an image. Containers make AI services reproducible across machines.

Verification: Run API, SQL, vector DB, and workers through Compose.

### `image`

A packaged filesystem and runtime configuration used to create containers. Images make deployments repeatable and reviewable.

Verification: Build a minimal image with pinned dependencies and no secrets.

### `Dockerfile`

A file describing how to build a container image. It encodes environment setup instead of relying on manual steps.

Verification: Review base image, dependency layers, user, healthcheck, and cache behavior.

### `Compose`

Docker's local multi-service orchestration format. It helps run API, database, vector store, and observability services together.

Verification: Create a one-command local stack for capstone development.

### `environment variable`

A runtime configuration value supplied outside code. It separates environment-specific config from application logic.

Verification: Use documented env vars for providers, DB URLs, log level, and feature flags.

### `secret`

A sensitive value such as an API key, token, or password. Secrets must not be committed, logged, embedded in images, or exposed to prompts.

Verification: Use `.env.example` without real values and document secret storage assumptions.

### `CI gate`

An automated check that must pass before merge or release. CI protects code quality and catches regressions early.

Verification: Add tests, linting, type checks, Docker build, and eval smoke tests.

### `release manifest`

A record linking a release to code, model, prompt, index, dataset, and eval results. AI releases include artifacts beyond code.

Verification: Version every AI artifact and link it to release evidence.


## Implementation Blueprint

Build this chapter as part of the capstone, not as isolated reading. The implementation should produce one or more concrete artifacts: code, schema, benchmark, trace, rubric, threat model, release manifest, or architecture document.

Recommended workflow:

1. Define the exact problem this chapter solves in the capstone.
2. Identify the data or request path affected by `container`, `image`, `Dockerfile`, `Compose`, `environment variable`, `secret`, `CI gate`, `release manifest`.
3. Create a minimal artifact that can be reviewed.
4. Add failure cases before adding complexity.
5. Add measurements, logs, traces, or human review.
6. Document the decision with numbered references.

## Current Engineering Problems To Study

- AI stacks depend on multiple services and fail when environments are not reproducible.
- Prompt, model, and index changes need release discipline like code changes.
- Full LLM evals can be too slow for every pull request, so CI must be tiered.

## Production Failure Modes

Each failure below names the concept, the way it shows up in production, and the check that would have caught it earlier. Treat this section as the source for regression tests and runbook entries.

- `container` — failure: The service works locally but fails on another developer's environment. Mitigation check: Run API, SQL, vector DB, and workers through Compose.
- `image` — failure: An image contains secrets or unpinned dependencies. Mitigation check: Build a minimal image with pinned dependencies and no secrets.
- `Dockerfile` — failure: A Dockerfile installs unnecessary tools and creates a huge attack surface. Mitigation check: Review base image, dependency layers, user, healthcheck, and cache behavior.
- `Compose` — failure: Integration tests require manual service startup in the right order. Mitigation check: Create a one-command local stack for capstone development.
- `environment variable` — failure: The model name is hardcoded and cannot differ by environment. Mitigation check: Use documented env vars for providers, DB URLs, log level, and feature flags.
- `secret` — failure: An API key appears in a Docker image layer or Git history. Mitigation check: Use `.env.example` without real values and document secret storage assumptions.
- `CI gate` — failure: A prompt change bypasses eval tests and breaks production behavior. Mitigation check: Add tests, linting, type checks, Docker build, and eval smoke tests.
- `release manifest` — failure: A rollback restores code but leaves a bad index in production. Mitigation check: Version every AI artifact and link it to release evidence.

## Project Directions

- Build a local stack with API, PostgreSQL, vector DB, and optional observability services.
- Create a CI pipeline with unit tests, API contract tests, Docker build, and eval smoke test.
- Write a release manifest that versions code, prompt, model, embedding model, index, and eval dataset.

## Verification Artifacts

- A short concept summary with citations.
- A capstone artifact that uses at least three chapter concepts.
- A test, metric, evaluation, or review checklist.
- A failure analysis table.
- A decision record comparing at least two alternatives.
- A reference section using `[1]`, `[2]` style citations.

## How This Chapter Connects To The Capstone

In the capstone, this chapter should leave a visible artifact. Examples include a module, schema, benchmark, design memo, evaluation result, threat model, release manifest, or demo step. Do not mark the chapter complete until the artifact is connected to the capstone.

## References

[1] Docker documentation: https://docs.docker.com/
[2] Docker Compose: https://docs.docker.com/compose/
[3] Dockerfile reference: https://docs.docker.com/reference/dockerfile/
[4] Git documentation: https://git-scm.com/doc
[5] GitHub Actions documentation: https://docs.github.com/en/actions
