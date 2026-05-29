# Dictionary: Docker, Linux, Git, and CI/CD

Use this dictionary at the end of the chapter. Add your own examples in `my_work/dictionary_notes.md`.

| Term | Working Definition | Why It Matters | Common Failure Mode | Mastery Check |
| --- | --- | --- | --- | --- |
| `container` | A running isolated process created from an image. | Containers make AI services reproducible across machines. | The service works locally but fails on another developer's environment. | Run API, SQL, vector DB, and workers through Compose. |
| `image` | A packaged filesystem and runtime configuration used to create containers. | Images make deployments repeatable and reviewable. | An image contains secrets or unpinned dependencies. | Build a minimal image with pinned dependencies and no secrets. |
| `Dockerfile` | A file describing how to build a container image. | It encodes environment setup instead of relying on manual steps. | A Dockerfile installs unnecessary tools and creates a huge attack surface. | Review base image, dependency layers, user, healthcheck, and cache behavior. |
| `Compose` | Docker's local multi-service orchestration format. | It helps run API, database, vector store, and observability services together. | Integration tests require manual service startup in the right order. | Create a one-command local stack for capstone development. |
| `environment variable` | A runtime configuration value supplied outside code. | It separates environment-specific config from application logic. | The model name is hardcoded and cannot differ by environment. | Use documented env vars for providers, DB URLs, log level, and feature flags. |
| `secret` | A sensitive value such as an API key, token, or password. | Secrets must not be committed, logged, embedded in images, or exposed to prompts. | An API key appears in a Docker image layer or Git history. | Use `.env.example` without real values and document secret storage assumptions. |
| `CI gate` | An automated check that must pass before merge or release. | CI protects code quality and catches regressions early. | A prompt change bypasses eval tests and breaks production behavior. | Add tests, linting, type checks, Docker build, and eval smoke tests. |
| `release manifest` | A record linking a release to code, model, prompt, index, dataset, and eval results. | AI releases include artifacts beyond code. | A rollback restores code but leaves a bad index in production. | Version every AI artifact and link it to release evidence. |

<!-- HAND-AUTHORED: do not regenerate -->
## Extended Glossary

Additional terms used in this chapter, each with a concise definition and an authoritative source.

- **Image vs container** — an image is an immutable built template; a container is a running instance of it. Source: [Docker overview](https://docs.docker.com/get-started/overview/)
- **Image layer** — a cached filesystem layer; ordering Dockerfile steps well maximizes cache reuse. Source: [Dockerfile best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- **Multi-stage build** — separate build and runtime stages to keep the final image small. Source: [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)
- **HEALTHCHECK** — an in-image readiness probe. Source: [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- **SIGTERM / graceful shutdown** — the signal orchestrators send to drain a service before stopping it. Source: [Docker stop](https://docs.docker.com/reference/cli/docker/container/stop/)
- **docker compose** — defining and running a multi-container local stack. Source: [Compose](https://docs.docker.com/compose/)
- **CI/CD** — automated build/test/release pipelines. Source: [GitHub Actions](https://docs.github.com/en/actions)
- **Lockfile** — pinned exact dependency versions for reproducible builds. Source: [pip-tools](https://pip-tools.readthedocs.io/) / [uv](https://docs.astral.sh/uv/)
- **Semantic versioning** — MAJOR.MINOR.PATCH version contract. Source: [semver.org](https://semver.org/)
- **OCI image spec** — the open standard for container images. Source: [OCI image-spec](https://github.com/opencontainers/image-spec)
- **pre-commit** — a framework running formatters/linters/secret-scanners on commit. Source: [pre-commit](https://pre-commit.com/)
- **Container/image vulnerability scanning** — detecting CVEs in images (e.g. Trivy). Source: [Trivy](https://aquasecurity.github.io/trivy/)

## Dictionary Assignment

For each term:

1. Write a one-sentence definition in your own words.
2. Write a concrete example from your capstone (or planned capstone).
3. Write one failure mode you would test against.
4. Write one metric, test, or review check that would catch the failure.
5. Link one source from `references_numbered.md`.

## References

[1] Docker documentation: https://docs.docker.com/
[2] Docker Compose: https://docs.docker.com/compose/
[3] Dockerfile reference: https://docs.docker.com/reference/dockerfile/
[4] Git documentation: https://git-scm.com/doc
[5] GitHub Actions documentation: https://docs.github.com/en/actions
