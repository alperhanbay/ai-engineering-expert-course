# Projects: Embeddings and Vector Search

## Project 1: Vector Search Benchmark

Build a small dataset of at least 100 chunks.

Run:

- vector-only retrieval;
- keyword-only retrieval;
- hybrid retrieval if your tool supports it.

Measure:

- Recall@5;
- MRR;
- p50/p95 latency;
- failure cases.

## Project 2: Metadata Filter Lab

Create records with:

- tenant IDs;
- document types;
- dates;
- permissions;
- domains.

Test retrieval with and without filters. Document any security risk.

## Project 3: Embedding Migration Plan

Write a plan for changing embedding models in production.

Include:

- dual-write or backfill strategy;
- index versioning;
- evaluation before cutover;
- rollback;
- cost estimate;
- monitoring.

