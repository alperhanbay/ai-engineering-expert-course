# Expanded Question Bank: Docker, Linux, Git, and CI/CD

## How To Use This Bank

Answer without looking at the answer key. For every wrong answer, write one sentence explaining the concept in your own words and one sentence explaining how it appears in a production AI system.


## Multiple Choice

1. Which sentence is the best working definition of `container`?
   - A. A running isolated process created from an image.
   - B. A packaged filesystem and runtime configuration used to create containers.
   - C. A file describing how to build a container image.
   - D. Docker's local multi-service orchestration format.

2. In production AI work, what is the primary role of `image`?
   - A. A running isolated process created from an image.
   - B. A file describing how to build a container image.
   - C. Docker's local multi-service orchestration format.
   - D. A packaged filesystem and runtime configuration used to create containers.

3. A teammate asks you to define `Dockerfile` in one sentence. Which is closest?
   - A. A packaged filesystem and runtime configuration used to create containers.
   - B. Docker's local multi-service orchestration format.
   - C. A file describing how to build a container image.
   - D. A running isolated process created from an image.

4. Pick the description of `Compose` you would put in a `dictionary.md` entry.
   - A. A file describing how to build a container image.
   - B. Docker's local multi-service orchestration format.
   - C. A running isolated process created from an image.
   - D. A packaged filesystem and runtime configuration used to create containers.

5. Which sentence is the best working definition of `environment variable`?
   - A. A runtime configuration value supplied outside code.
   - B. A running isolated process created from an image.
   - C. A packaged filesystem and runtime configuration used to create containers.
   - D. A file describing how to build a container image.

6. In production AI work, what is the primary role of `secret`?
   - A. A running isolated process created from an image.
   - B. A packaged filesystem and runtime configuration used to create containers.
   - C. A file describing how to build a container image.
   - D. A sensitive value such as an API key, token, or password.

7. A teammate asks you to define `CI gate` in one sentence. Which is closest?
   - A. A packaged filesystem and runtime configuration used to create containers.
   - B. A file describing how to build a container image.
   - C. An automated check that must pass before merge or release.
   - D. A running isolated process created from an image.

8. Pick the description of `release manifest` you would put in a `dictionary.md` entry.
   - A. A file describing how to build a container image.
   - B. A record linking a release to code, model, prompt, index, dataset, and eval results.
   - C. A running isolated process created from an image.
   - D. A packaged filesystem and runtime configuration used to create containers.


## Applied Multiple Choice

1. Applied case: AI stacks depend on multiple services and fail when environments are not reproducible.
   - A. Remove logging and evaluation to keep the diff small and merge faster.
   - B. Assume the largest available model will mask the underlying weakness in `container` so no system change is needed.
   - C. Set up a controlled experiment isolating `container`, capture before/after numbers, and write the result to a decision record.
   - D. Ship the change without measurement because the most recent demo looked good.

2. Applied case: Prompt, model, and index changes need release discipline like code changes.
   - A. Skip the rollback plan; staging is close enough to production.
   - B. Add the work to the capstone as a reviewable artifact that exercises `image` end-to-end, with tests and a trace.
   - C. Remove logging and evaluation to keep the diff small and merge faster.
   - D. Assume the largest available model will mask the underlying weakness in `container` so no system change is needed.

3. Applied case: Full LLM evals can be too slow for every pull request, so CI must be tiered.
   - A. Define explicit acceptance criteria, rollback steps, and a reviewer checklist tied to Docker, Linux, Git, and CI/CD.
   - B. Assume the largest available model will mask the underlying weakness in `container` so no system change is needed.
   - C. Skip the rollback plan; staging is close enough to production.
   - D. Hard-code the new behaviour for the first failing case and call it a fix.

4. Applied case: Build a local stack with API, PostgreSQL, vector DB, and optional observability services.
   - A. Skip the rollback plan; staging is close enough to production.
   - B. Hard-code the new behaviour for the first failing case and call it a fix.
   - C. Ship the change without measurement because the most recent demo looked good.
   - D. Compare at least two approaches against a labelled set covering `release manifest`, then choose on measured quality, latency, cost, and risk.

5. Applied case: Create a CI pipeline with unit tests, API contract tests, Docker build, and eval smoke test.
   - A. Ship the change without measurement because the most recent demo looked good.
   - B. Remove logging and evaluation to keep the diff small and merge faster.
   - C. Write a one-page design memo naming the assumption, the test that would falsify it, and the metric you'd watch in production.
   - D. Hard-code the new behaviour for the first failing case and call it a fix.

6. Applied case: Write a release manifest that versions code, prompt, model, embedding model, index, and eval dataset.
   - A. Assume the largest available model will mask the underlying weakness in `container` so no system change is needed.
   - B. Set up a controlled experiment isolating `container`, capture before/after numbers, and write the result to a decision record.
   - C. Ship the change without measurement because the most recent demo looked good.
   - D. Remove logging and evaluation to keep the diff small and merge faster.


## Fill In The Blanks

1. Containers make AI services reproducible across machines. A common failure looks like: The service works locally but fails on another developer's environment. The concept is ________.
2. Given the production failure "An image contains secrets or unpinned dependencies.", the concept being misused is ________.
3. To handle situations where it encodes environment setup instead of relying on manual steps, the engineering tool you reach for is ________ (watch for: A Dockerfile installs unnecessary tools and creates a huge attack surface.).
4. ________ is best summarised as: Docker's local multi-service orchestration format. Verification step: Create a one-command local stack for capstone development.
5. On a system review, you find the model name is hardcoded and cannot differ by environment — the underlying chapter concept is ________.
6. Secrets must not be committed, logged, embedded in images, or exposed to prompts. A common failure looks like: An API key appears in a Docker image layer or Git history. The concept is ________.
7. Given the production failure "A prompt change bypasses eval tests and breaks production behavior.", the concept being misused is ________.
8. To handle situations where aI releases include artifacts beyond code, the engineering tool you reach for is ________ (watch for: A rollback restores code but leaves a bad index in production.).

## Short Answer

1. Explain how `container` appears in the capstone, what artifact proves it, and what failure mode you would test.
2. If a reviewer asks 'why does `image` matter here?', what one-paragraph answer do you give? Include a metric.
3. Describe the smallest experiment that would tell you whether `Dockerfile` is correctly implemented in your system.
4. When would you intentionally *avoid* using `Compose`? Name a constraint or tradeoff.
5. What does a healthy log or trace look like for `environment variable`? List the fields you would expect.
6. Explain how `secret` appears in the capstone, what artifact proves it, and what failure mode you would test.
7. If a reviewer asks 'why does `CI gate` matter here?', what one-paragraph answer do you give? Include a metric.
8. Describe the smallest experiment that would tell you whether `release manifest` is correctly implemented in your system.

## Scenario Questions

1. Incident: AI stacks depend on multiple services and fail when environments are not reproducible. What do you inspect first, and which metric would prove the fix?
2. Design review: Prompt, model, and index changes need release discipline like code changes. Which artifact would you require before approving?
3. Postmortem prompt: Full LLM evals can be too slow for every pull request, so CI must be tiered. What regression test would prevent recurrence?
4. A pull request modifies `Compose` and a downstream quality metric drops. What rollback, evaluation, and documentation do you require before merge?

## Practical Debug Questions

1. What log or trace fields would help you debug a failure in `container` in this chapter's context?
2. What single metric would you watch in production when changing `environment variable`?
3. You suspect `release manifest` is degraded. Design the smallest experiment that would falsify or confirm it in under an hour.
4. For the failure 'AI stacks depend on multiple services and fail when environments are not reproducible.', sketch a rollback plan with a clear restore-point definition.
5. What artifact would you put in a portfolio README to prove competence with `container`, `image`, `Dockerfile`?

## Answer Key

### Multiple Choice

1. A
2. D
3. C
4. B
5. A
6. D
7. C
8. B

### Applied Multiple Choice

1. C
2. B
3. A
4. D
5. C
6. B

### Fill In The Blanks

1. container
2. image
3. Dockerfile
4. Compose
5. environment variable
6. secret
7. CI gate
8. release manifest

Short-answer, scenario, and debug questions should be graded against the rubric in `../../syllabus/evaluation_rubric.md`.

## References

[1] Docker documentation: https://docs.docker.com/
[2] Docker Compose: https://docs.docker.com/compose/
[3] Dockerfile reference: https://docs.docker.com/reference/dockerfile/
[4] Git documentation: https://git-scm.com/doc
[5] GitHub Actions documentation: https://docs.github.com/en/actions
