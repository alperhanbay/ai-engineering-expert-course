# Examples: Capstone, Portfolio, and Interview Readiness

Templates matching `lesson.md`.

## 1. Portfolio README skeleton

```md
# <Capstone Name> — AI Knowledge Assistant for <domain>

## What it is
A production-style RAG+agent assistant for <domain>, for <users>. Answers from
<corpus> with citations, refuses when unsupported, and gates side-effect actions.

## Run it
```bash
cp .env.example .env
docker compose up --build      # api + postgres + qdrant
make demo                      # runs the 5-step demo
```

## Architecture
See architecture_pack/ (system, data, RAG, agent, deployment, threat model).

## Results (golden-v3, per risk level)
| risk | faithfulness | citation-correct | no-answer-acc | n |
|------|-------------|------------------|---------------|---|
| high | 0.96        | 0.93             | 1.00          | 40|
| med  | 0.94        | 0.90             | 1.00          | 35|
| low  | 0.92        | 0.88             | 1.00          | 25|
Measured by `eval/run_eval.py`; see evidence_index.md.

## Security
Threat model: architecture_pack/threat_model.md. Guardrail suite: 52/52 pass.

## Limitations (honest)
1. Multi-jurisdiction questions: faithfulness drops ~6%; tracked in failure_log.
2. Tables in scanned PDFs parse poorly; flagged, not yet fixed.
3. No multilingual support beyond <lang>.

## Sources
[1] ... [2] ...
```

## 2. Evidence index (claims -> artifacts)

```md
| Claim in README                     | Source artifact |
|-------------------------------------|-----------------|
| faithfulness 0.96 (high risk)       | eval/runs/run_5012.json |
| guardrail suite 52/52               | guardrail_tests/ CI run #381 |
| p95 /ask 2.4s                       | telemetry/latency_budget.md |
| cross-tenant leak: 0                | tests/test_cross_tenant.py |
```

## 3. STAR story template (with a number)

```md
## STAR: retrieval failure
S: Legal-code questions returned wrong answers; users complained.
T: Find and fix the retrieval gap without regressing paraphrase queries.
A: Diagnosed Recall@5 0.71 on exact-term queries; added hybrid (RRF) search.
   Measured per query-type; rejected reranking (no faithfulness gain, +40ms).
R: Recall@5 0.71 -> 0.89 on exact-term; paraphrase unchanged; +40ms p95.
   Faithfulness on high-risk held at 0.96.
```

## 4. System-design answer checklist (say these, in order)

```md
1. Requirements: users, accuracy bar, latency budget, data sensitivity, scale.
2. Data + retrieval: corpus, chunking, embeddings, hybrid, filtering.
3. Generation: prompt, structured output, citations, no-answer.
4. Evaluation: golden set, metrics per risk level, release gate.
5. Operations: observability (quality not just uptime), incidents, rollback.
6. Security: injection, tenant isolation, code-enforced perms, audit.
7. Tradeoffs: cost vs quality vs latency, with decision criteria.
```

## 5. Demo script (runbook)

```md
# Demo (target < 15 min from clean clone)
1. docker compose up --build   # wait for /healthz
2. POST /documents (ingest sample policy) -> job done
3. POST /ask "claim deadline?"  -> grounded answer + [d_10:p3] citation
4. POST /ask "who won the match?" -> refusal (insufficient_context)
5. make eval                    -> show per-risk-level report + gate=pass
6. POST /ask with injected doc  -> guardrail blocks; audit entry written
```

## 6. Architecture diagram (text form, keep it matching code)

```
[client] -> [API /ask] -> [auth dep] -> [RagService]
                                          |-> [Retriever] -> [Qdrant] (tenant filter)
                                          |-> [Reranker] (confidence-aware)
                                          |-> [LLM] (structured output)
                                          |-> [Guardrails] (in + out)
                                          |-> [Audit] -> [Postgres]
[traces] -> OTel collector ; [metrics] -> Prometheus -> Grafana
```

## 7. Limitations section (the senior signal)

```md
## Known limitations & next steps
- Multi-jurisdiction: -6% faithfulness. Next: jurisdiction-aware routing (ch8).
- Scanned-PDF tables: parser mangles columns. Next: table-aware parser.
- Single-language. Next: multilingual embeddings bake-off (ch6 method).
- No fine-tuning done; decided against per ch14 memo (RAG sufficed).
```

## 8. Interview Q&A drill format

```md
Q: How do you know your RAG system is accurate?
A: Golden set of 100 cases, per risk level. Faithfulness 0.96 on high-risk,
   citation-correctness 0.93, no-answer accuracy 100%. Release gate blocks
   any high-risk regression. Failures categorised; each becomes a regression case.

Q: What happens when the model is wrong in production?
A: Per-stage traces localise it (retrieval vs generation). Cohort analysis by
   prompt_version finds the bad release. Manifest rollback restores code+prompt+index
   in <5 min. The case enters the golden set.
```
