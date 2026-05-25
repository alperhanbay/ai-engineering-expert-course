# Projects: Docker, Linux, Git, and CI/CD

## Project 1: Local AI Stack

Create a Docker Compose stack with:

- FastAPI app;
- PostgreSQL;
- Qdrant or another vector database;
- optional Redis worker;
- optional MLflow.

Acceptance criteria:

- `docker compose up` starts the stack;
- health endpoint works;
- database is reachable;
- vector DB is reachable;
- environment variables are documented.

## Project 2: CI Pipeline Design

Design a CI pipeline that runs:

- formatting;
- linting;
- type checks;
- unit tests;
- API contract tests;
- small eval smoke test;
- Docker image build.

Write it as a GitHub Actions workflow or as pseudocode.

## Project 3: Release Manifest

Create a release manifest format that records:

- git SHA;
- Docker image tag;
- prompt version;
- model version;
- embedding model;
- index version;
- eval dataset version;
- eval score summary.

