# Examples: LLM and RAG Evaluation

Reusable snippets matching `lesson.md`.

## 1. Golden case schema (jsonl)

```json
{"case_id": "CLAIM-007", "question": "What is the deadline to file a claim?",
 "expected_answer": "30 days from the incident date.",
 "reference_chunk_ids": ["c_1042"], "risk_level": "high", "failure_category": null}
{"case_id": "OOS-003", "question": "What's the weather tomorrow?",
 "expected_answer": null, "reference_chunk_ids": [], "risk_level": "low",
 "failure_category": "should_refuse"}
```

## 2. Retrieval metric against reference chunks

```python
def retrieval_hit(retrieved_ids: list[str], reference_ids: list[str], k: int) -> bool:
    return any(rid in set(reference_ids) for rid in retrieved_ids[:k])

recall_at_k = sum(retrieval_hit(r, c.reference_chunk_ids, 5) for r, c in runs) / len(runs)
```

## 3. Faithfulness via LLM-as-judge (sketch)

```python
JUDGE_PROMPT = """Given CONTEXT and ANSWER, is every claim in ANSWER supported
by CONTEXT? Respond JSON: {"faithful": true|false, "unsupported_claims": [...]}.
CONTEXT:\n{context}\nANSWER:\n{answer}"""

async def faithfulness(answer: str, context: str) -> float:
    r = await judge.complete_structured(
        JUDGE_PROMPT.format(context=context, answer=answer),
        schema=FaithfulnessVerdict, temperature=0)
    return 1.0 if r.faithful else 0.0
```

## 4. No-answer accuracy

```python
def no_answer_correct(case, result) -> bool:
    should_refuse = case.expected_answer is None
    did_refuse = result.answer is None
    return should_refuse == did_refuse
```

## 5. Per-risk-level aggregation

```python
from collections import defaultdict
from statistics import mean

def by_risk(results) -> dict:
    buckets = defaultdict(list)
    for case, r in results:
        buckets[case.risk_level].append(r.metrics)
    return {risk: {m: mean(x[m] for x in rows) for m in rows[0]}
            for risk, rows in buckets.items()}
```

## 6. Release gate

```python
def release_gate(report: dict, baseline: dict, max_regression=0.02) -> str:
    high = report["high"]
    if high["faithfulness"] < 0.95:        return "fail"
    if high["no_answer_accuracy"] < 1.0:   return "fail"
    if report["overall"]["answer_relevance"] < 0.85: return "fail"
    # block regressions on any metric vs production baseline
    for risk in report:
        for m, v in report[risk].items():
            if baseline.get(risk, {}).get(m, 0) - v > max_regression:
                # high-risk regression -> human must sign off
                return "manual_review" if risk == "high" else "fail"
    return "pass"
```

## 7. Judge calibration against human

```python
def agreement(judge_scores: list[bool], human_scores: list[bool]) -> float:
    return sum(j == h for j, h in zip(judge_scores, human_scores)) / len(human_scores)

# agreement < ~0.8 means the judge is too noisy to trust; fix the judge prompt.
```

## 8. Failure taxonomy assignment

```python
TAXONOMY = ["retrieval_miss", "ranking_miss", "hallucination", "wrong_citation",
            "incomplete", "should_have_refused", "over_refused", "unsafe", "formatting"]

def categorise(case, result, retrieved_ids) -> str | None:
    if result.passed: return None
    ref = set(case.reference_chunk_ids)
    if ref and not (ref & set(retrieved_ids)):       return "retrieval_miss"
    if ref and not (ref & set(retrieved_ids[:5])):   return "ranking_miss"
    if case.expected_answer is None and result.answer is not None: return "should_have_refused"
    if case.expected_answer is not None and result.answer is None: return "over_refused"
    if result.unfaithful:                            return "hallucination"
    if result.wrong_citation:                        return "wrong_citation"
    return "incomplete"
```

## 9. DeepEval-style test (evals as pytest)

```python
import pytest

@pytest.mark.parametrize("case", load_golden("golden/v1.jsonl"), ids=lambda c: c.case_id)
def test_case_meets_threshold(case, run_pipeline):
    result = run_pipeline(case.question, tenant_id="t1")
    if case.risk_level == "high":
        assert result.faithfulness >= 0.95, f"{case.case_id} faithfulness too low"
    if case.expected_answer is None:
        assert result.answer is None, f"{case.case_id} should have refused"
```

## 10. Feedback -> new golden case

```python
def feedback_to_golden_case(feedback_row, answer_row) -> dict:
    return {
        "case_id": f"FB-{feedback_row.id}",
        "question": answer_row.question,
        "expected_answer": feedback_row.corrected_answer,   # expert-provided
        "reference_chunk_ids": feedback_row.correct_chunk_ids,
        "risk_level": feedback_row.risk_level or "medium",
        "failure_category": feedback_row.failure_category,
    }
# Every real failure an expert reviews becomes a regression case. The set grows
# to cover your actual failure surface, not your imagined one.
```
