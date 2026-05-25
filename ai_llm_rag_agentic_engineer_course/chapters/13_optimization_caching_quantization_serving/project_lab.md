# Project Lab: Optimization, Caching, Quantization, and Serving

Optimization is the disciplined reduction of cost and latency while preserving quality and safety. This lab turns the chapter's projects into concrete, reviewable
deliverables. Pick one project and finish it end-to-end before starting another.
The "Acceptance Criteria" sections are the gate — not the existence of files.

## Project 1: Instrument a RAG request and create a latency budget with p50/p95 measurements.

### Scenario

The capstone's `/ask` endpoint has acceptable quality but p95 latency is 4.2s and cost per 1k requests is uncomfortably high. Before throwing money or quantization at it, you need a measured budget showing where each millisecond and each dollar goes, and a decision matrix for the serving options.

### Inputs

- instrumented RAG request path (from chapter 12) producing per-stage latency
- 200 representative requests sampled from logs (PII-scrubbed) for a realistic load
- the chapter 09 golden eval set for quality-regression checks
- access to at least one hosted API and one self-host option (vLLM or TGI) for comparison

### Outputs / Artifacts

- `latency_budget.md` — stage-by-stage p50/p95 breakdown with a target and a measured 'now'
- `cache_design.md` — what is cached (prompt prefix, embedding, retrieved chunks, final answer), key format including tenant id, TTL, invalidation, security risks considered
- `serving_matrix.md` — hosted API vs vLLM vs TGI vs Triton on quality, p95, throughput, $/1k, ops burden
- `quantization_eval.md` — before/after eval on the golden set when a quantized open model is included

### Test Cases

- warm vs cold prompt-cache request — both correct, second must be faster
- cross-tenant cache test: tenant A request must never return tenant B's cached answer
- streaming response: an early-token error path must still produce a recoverable error event
- quantized vs full-precision: faithfulness on high-risk cases must not drop more than an agreed threshold

### Metrics

- p50 and p95 end-to-end latency, decomposed by stage
- cache hit rate; latency delta for hits vs misses
- $ per 1k requests for each serving option
- quality delta (faithfulness, citation-correctness) before vs after each change

### Failure Cases To Cover

- Cache key omits tenant id and leaks responses across tenants
- Streaming bypasses guardrails because the safety check runs on the full text
- Quantization improves throughput but silently regresses on long-context cases
- The decision matrix is filled with vendor claims, not measurements from this corpus

### Acceptance Criteria

- the latency budget names a single target and shows the measured delta per stage
- the cache design names a control for the cross-tenant risk and a test that proves it
- the serving matrix is filled with numbers from this repo, with the script to reproduce them
- no optimization is recommended without a before/after quality measurement on the golden set

### Deliverables Layout

```
my_work/
  project_1_scope.md            # one paragraph + concept list
  project_1_implementation/      # code or design doc
  project_1_report.md            # results, numbers, plots
  project_1_decision_record.md   # alternatives + chosen approach + why
  project_1_tests/               # the test cases above, runnable or scripted
```

### Expected README Section

In your portfolio README, this project should appear under "Projects" with:
a one-sentence summary, the headline metric you measured, the main tradeoff
you made, and a link to the decision record. Avoid screenshots-only entries.

## Project 2: Design a cache strategy with keys, TTLs, invalidation, and security risks.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `latency budget`, `streaming`, `batching`, `prompt caching`, `KV-cache`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `latency budget`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_2_implementation/`
- `my_work/project_2_report.md` summarising results with numbers
- `my_work/project_2_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `latency budget`
- an edge case driven by the failure mode of `streaming`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `latency budget` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Streaming improves perceived latency but complicates validation and citations.
- Caching can leak data if keys ignore tenant or permission context.
- Quantization and serving changes require before/after quality evaluation.
- silent degradation of `Triton` after a config change goes unnoticed

### Acceptance Criteria

- a reviewer can run or read the artifact and understand what was built without asking you
- every numeric claim is backed by a test, eval result, or measured run logged in the report
- at least one known limitation is named honestly (not a humblebrag)
- the artifact is wired into the capstone, not orphaned in `my_work/`

### Deliverables Layout

```
my_work/
  project_2_scope.md            # one paragraph + concept list
  project_2_implementation/      # code or design doc
  project_2_report.md            # results, numbers, plots
  project_2_decision_record.md   # alternatives + chosen approach + why
  project_2_tests/               # the test cases above, runnable or scripted
```

### Expected README Section

In your portfolio README, this project should appear under "Projects" with:
a one-sentence summary, the headline metric you measured, the main tradeoff
you made, and a link to the decision record. Avoid screenshots-only entries.

## Project 3: Compare hosted API, vLLM, TGI, and Triton using a decision matrix.

### Scenario

Build this as a reviewable artifact in your capstone, not a private notebook — treat the diff as something a teammate will read in a pull request. It should exercise at least three of: `latency budget`, `streaming`, `batching`, `prompt caching`, `KV-cache`, and produce evidence a reviewer can verify without running you down on Slack.

### Inputs

- a small, real or synthetic dataset that exercises `latency budget`
- a clearly written problem statement (one paragraph) committed alongside the code
- any external configuration (model names, endpoints, thresholds) in `.env.example`

### Outputs / Artifacts

- runnable code or design doc in `my_work/project_3_implementation/`
- `my_work/project_3_report.md` summarising results with numbers
- `my_work/project_3_decision_record.md` for the main tradeoff

### Test Cases

- a typical happy-path case that touches `latency budget`
- an edge case driven by the failure mode of `streaming`
- an adversarial or out-of-distribution input the system should refuse or flag
- a regression case taken from one of the chapter's stated problems

### Metrics

- a quality metric appropriate to `latency budget` (define units and how it's measured)
- a latency or cost metric (p50 and p95 where it makes sense)
- a coverage or completeness metric for the test set

### Failure Cases To Cover

- Streaming improves perceived latency but complicates validation and citations.
- Caching can leak data if keys ignore tenant or permission context.
- Quantization and serving changes require before/after quality evaluation.
- silent degradation of `Triton` after a config change goes unnoticed

### Acceptance Criteria

- a reviewer can run or read the artifact and understand what was built without asking you
- every numeric claim is backed by a test, eval result, or measured run logged in the report
- at least one known limitation is named honestly (not a humblebrag)
- the artifact is wired into the capstone, not orphaned in `my_work/`

### Deliverables Layout

```
my_work/
  project_3_scope.md            # one paragraph + concept list
  project_3_implementation/      # code or design doc
  project_3_report.md            # results, numbers, plots
  project_3_decision_record.md   # alternatives + chosen approach + why
  project_3_tests/               # the test cases above, runnable or scripted
```

### Expected README Section

In your portfolio README, this project should appear under "Projects" with:
a one-sentence summary, the headline metric you measured, the main tradeoff
you made, and a link to the decision record. Avoid screenshots-only entries.

## Review Rubric

| Dimension | Evidence that passes |
| --- | --- |
| Specificity | scenario, inputs, and outputs match what the artifact actually does |
| Measurement | metrics are numeric, named, and reproducible from the repo |
| Failure handling | at least three failure cases are exercised in tests |
| Tradeoff honesty | decision record names alternatives and a measured reason |
| Source backing | numbered references support every external claim |

## References

[1] OpenAI prompt caching: https://platform.openai.com/docs/guides/prompt-caching
[2] vLLM online serving: https://docs.vllm.ai/en/latest/serving/online_serving/
[3] vLLM OpenAI-compatible server: https://docs.vllm.ai/en/latest/serving/openai_compatible_server/
[4] Hugging Face TGI: https://huggingface.co/docs/text-generation-inference/main/en/index
[5] NVIDIA Triton: https://docs.nvidia.com/deeplearning/triton-inference-server/index.html
[6] Transformers quantization: https://huggingface.co/docs/transformers/quantization
[7] ONNX Runtime quantization: https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html
