# Examples: Fine-Tuning and Model Adaptation

Reusable snippets matching `lesson.md`.

## 1. Failure classification (drives the decision)

```python
LEVER = {
    "retrieval_miss": "fix retrieval (ch6/8) - NOT fine-tuning",
    "ranking_miss":   "add reranking (ch8) - NOT fine-tuning",
    "hallucination":  "usually retrieval/prompt - rarely fine-tuning",
    "formatting":     "prompt+structured output first; fine-tune if persistent",
    "tone_style":     "fine-tuning / preference tuning candidate",
    "missing_fact":   "RAG - NEVER fine-tune to memorise changing facts",
}
def recommended_lever(category: str) -> str:
    return LEVER.get(category, "investigate before choosing a lever")
```

## 2. Hash-checked held-out set (prove no leakage)

```python
import hashlib, json

def split_hashes(train, holdout):
    h = lambda rows: {hashlib.sha256(json.dumps(r, sort_keys=True).encode()).hexdigest()
                      for r in rows}
    train_h, hold_h = h(train), h(holdout)
    assert not (train_h & hold_h), "LEAK: held-out examples appear in training set"
    return train_h, hold_h
```

## 3. QLoRA training (sketch, TRL/PEFT)

```python
from peft import LoraConfig
from trl import SFTTrainer

lora = LoraConfig(r=16, lora_alpha=32, lora_dropout=0.05,
                  target_modules=["q_proj", "v_proj"], task_type="CAUSAL_LM")

trainer = SFTTrainer(
    model="meta-llama/Llama-3-8B",      # loaded 4-bit for QLoRA
    train_dataset=train_ds,
    peft_config=lora,
    args=TrainingArgs(per_device_train_batch_size=4, num_train_epochs=2,
                      learning_rate=2e-4, seed=7, output_dir="adapters/fmt_v1"),
)
trainer.train()   # produces a small adapter, base model unchanged
```

## 4. Before/after eval (per risk level, with regression + safety)

```python
async def adaptation_report(golden, base_model, adapted_model):
    base = await run_eval(base_model, golden)
    adapted = await run_eval(adapted_model, golden)
    out = {}
    for risk in ("low", "medium", "high"):
        out[risk] = {
            "target_delta": adapted[risk]["formatting_ok"] - base[risk]["formatting_ok"],
            "faithfulness_delta": adapted[risk]["faithfulness"] - base[risk]["faithfulness"],
            "safety_delta": adapted[risk]["injection_refusal"] - base[risk]["injection_refusal"],
        }
    return out
# SHIP only if target improves AND faithfulness/safety deltas are >= ~0.
```

## 5. Adapter as a versioned, rollback-able artifact

```yaml
# release_manifest.yaml fragment
model_id: "llama-3-8b"
adapter: "adapters/fmt_v1@sha256:abc..."   # versioned; rollback = previous adapter
adapter_eval_run: "run_5012"
```

## 6. Small classifier vs LLM router comparison

```python
async def compare_router(cases):
    clf = SmallIntentClassifier.load("models/router_v1")
    clf_acc = sum(clf.predict(c.query) == c.route for c in cases) / len(cases)
    llm_acc = sum(await llm_classify(c.query) == c.route for c in cases) / len(cases)
    return {
        "classifier": {"acc": clf_acc, "p95_ms": 4, "cost_per_1k": 0.0},
        "llm":        {"acc": llm_acc, "p95_ms": 320, "cost_per_1k": 0.40},
    }
# A stable narrow task often favours the classifier on latency+cost at equal accuracy.
```

## 7. Synthetic data review

```python
def review_synthetic(samples, human_gold):
    dedup = {hash(s["input"]): s for s in samples}.values()
    spotcheck = random.sample(list(dedup), 50)
    correct = sum(label_matches(s, human_gold) for s in spotcheck)
    return {"n": len(samples), "after_dedup": len(dedup),
            "spotcheck_pass_rate": correct / len(spotcheck)}
# pass_rate < ~0.9 -> synthetic labels too noisy to train on
```

## 8. Distillation: evaluate against ground truth, not the teacher

```python
def distillation_report(student, teacher, gold):
    vs_teacher = agreement(student.predict_all(gold), teacher.predict_all(gold))
    vs_truth   = accuracy(student.predict_all(gold), [g.label for g in gold])
    return {"agree_with_teacher": vs_teacher, "accuracy_vs_truth": vs_truth}
# High teacher-agreement but low truth-accuracy = student copied teacher's errors.
```

## 9. Decision memo template

```md
# Adaptation Decision: inconsistent extraction formatting
Failure evidence: 14% of high-risk extraction cases produce invalid field types.
Cheaper levers: structured-output enforcement cut it 14% -> 6%, not enough.
Proposal: QLoRA on llama-3-8b, 300 curated examples, 60 held-out.
Success criteria: high-risk formatting failures < 1%; faithfulness within 1%;
                  injection-refusal must not drop.
Decision: APPROVE pending before/after eval. Owner: <name>. Date: <date>.
```
