# Projects: FastAPI, REST, and Integration

## Project 1: AI API Contract

Build a FastAPI service with:

- `GET /health`
- `POST /documents`
- `POST /documents/{document_id}/index`
- `GET /jobs/{job_id}`
- `POST /ask`
- `POST /feedback`
- `POST /eval/run`

Acceptance criteria:

- OpenAPI docs generate correctly;
- request/response schemas are explicit;
- error responses follow one format;
- tests cover success and failure cases.

## Project 2: Streaming Prototype

Create a streaming `/ask/stream` endpoint.

Document:

- what is streamed;
- how errors are handled;
- how citations are delivered;
- how partial unsafe output is prevented.

## Project 3: Background Ingestion Job

Design a job system for document indexing.

Minimum states:

- queued;
- parsing;
- chunking;
- embedding;
- indexing;
- completed;
- failed.

Deliverables:

- API contract;
- state transition diagram;
- failure handling plan.

