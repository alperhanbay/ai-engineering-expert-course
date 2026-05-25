# Projects: Advanced RAG, Retrieval, and Reranking

## Project 1: Retrieval Experiment Suite

Compare:

- fixed-size chunking;
- recursive chunking;
- semantic or section-aware chunking;
- vector-only retrieval;
- hybrid retrieval;
- reranked retrieval.

Deliverables:

- experiment config file;
- results table;
- failure analysis;
- recommendation.

## Project 2: Reranking Pipeline

Implement:

```text
retrieve top 50
  -> rerank
  -> select top 5
  -> generate
```

Measure:

- quality gain;
- latency increase;
- cost increase;
- failure reduction.

## Project 3: Query Router

Build a router for:

- knowledge question;
- policy/legal citation question;
- case/customer-specific question;
- analytics question;
- unsafe/private request.

Write tests for each route.

