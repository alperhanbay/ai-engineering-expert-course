# Projects: SQL and Data Management

## Project 1: AI System Data Model

Design SQL tables for:

- tenants;
- users;
- documents;
- chunks;
- embedding metadata;
- RAG requests;
- retrieved contexts;
- generated answers;
- feedback;
- eval cases;
- eval runs;
- audit logs.

Deliverables:

- `schema.sql`;
- entity relationship diagram;
- 10 sample queries;
- index design notes.

## Project 2: Evaluation Dataset Registry

Create a schema for versioned evaluation datasets.

Include:

- dataset version;
- case source;
- expected answer;
- reference contexts;
- difficulty;
- risk level;
- reviewer;
- active/inactive flag.

## Project 3: Incident Analysis Queries

Write SQL queries for:

- slowest 20 requests;
- lowest-rated model version;
- retrieval requests with no contexts;
- answers without citations;
- cross-tenant access attempts;
- eval cases that failed after a prompt change.

