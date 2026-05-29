# Homework: LLM Fundamentals and Prompting

Graded against `../../syllabus/evaluation_rubric.md`. Outputs under `my_work/`.

## Required

1. **Token budgeting utility.** Write `my_work/token_budget.py` that, given a
   system prompt, history, retrieved chunks, and a question, reports the token
   count per component and asserts the total + reserved answer tokens fits a
   given context limit. Test it with an oversized input and show the assertion
   fires.

2. **Prompt registry.** Create `prompts/` with at least two prompts
   (`rag_answer`, `extract_fields`), each versioned with a `.meta.yaml`
   (intent, model, temperature, status, changelog). Add a `registry.json`
   mapping name → current prod version.

3. **Structured extraction.** Build an extraction task: free text in, a
   Pydantic-validated JSON object out. Use structured-output enforcement if
   your provider supports it; otherwise implement the parse-repair fallback.
   Define and test the behaviour on a deliberately malformed model output.

4. **No-answer behaviour.** Write a RAG-answer prompt that emits an exact
   `{"answer": null, "reason": "insufficient_context"}` when the context
   doesn't support an answer. Test with 5 unsupported questions; all must
   refuse.

5. **Injection test set.** Build `my_work/injection_tests/` with at least 10
   cases across the three styles (direct, indirect-via-context, tool-output).
   Each case has the input and the expected safe behaviour. Wire them as a
   pytest suite. Document which ones your current prompt passes and which it
   doesn't.

6. **Decoding experiment.** Run the same extraction task at temperature 0,
   0.3, and 1.0 (fixed seed where supported), 10 times each. Record output
   variance in `my_work/decoding_experiment.md`. Conclude which setting your
   task should use and why.

## Stretch

7. **Zero-shot vs few-shot A/B.** On a 20-case labelled set, compare a
   zero-shot prompt against a few-shot version (3 examples). Report exact-match
   and field-F1 deltas plus the token-cost delta. Recommend one with evidence.

8. **Lost-in-the-middle probe.** Place a known answer at the start, middle, and
   end of a long (6k-token) context and measure retrieval-into-answer accuracy
   by position. Confirm or refute the effect on your model.

9. **Cost model.** Given your prompt token counts and a provider price sheet,
   write a script that estimates $/1k requests for each prompt version. Use it
   to flag a version that silently got more expensive.

## Acceptance

- Token budget utility correctly rejects an over-limit input.
- All 5 unsupported questions trigger the exact no-answer JSON.
- The injection suite runs as tests; you can state your pass rate honestly.
- The decoding experiment concludes with a defended temperature choice.
