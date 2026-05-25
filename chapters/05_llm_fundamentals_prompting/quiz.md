# Quiz: LLM Fundamentals and Prompting

## Multiple Choice

1. Why do tokens matter in production?
   - A. They affect cost, latency, and context limits
   - B. They replace embeddings
   - C. They remove hallucination
   - D. They are only relevant during training

2. What is grounding?
   - A. Making the model run on a server
   - B. Requiring answers to be supported by provided sources
   - C. Increasing temperature
   - D. Removing citations

3. Which setting is usually safer for deterministic extraction?
   - A. Very high temperature
   - B. Lower temperature
   - C. Random prompts
   - D. No schema

4. Why should retrieved context be treated as untrusted data?
   - A. It may contain prompt injection
   - B. It is always short
   - C. It cannot affect the model
   - D. It replaces authorization

5. What should be versioned in a production prompt workflow?
   - A. Prompt text
   - B. Model used
   - C. Evaluation results
   - D. All of the above

## Fill in the Blanks

1. The context window is measured in ________.
2. Few-shot prompting gives the model ________ of desired behavior.
3. Structured output is useful when downstream systems need reliable ________.
4. Prompt injection tries to override trusted ________.
5. Prompting alone does not fully solve ________.

## Short Answer

1. Explain the difference between system prompt and retrieved context.
2. Why can too much context reduce answer quality?
3. Give a prompt-injection test case for a RAG system.

## Answer Key

### Multiple Choice

1. A
2. B
3. B
4. A
5. D

### Fill in the Blanks

1. tokens
2. examples
3. parsing
4. instructions
5. hallucination

