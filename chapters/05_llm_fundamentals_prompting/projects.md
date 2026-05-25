# Projects: LLM Fundamentals and Prompting

## Project 1: Prompt Version Registry

Create a prompt registry with:

- prompt ID;
- version;
- task;
- system prompt;
- expected schema;
- model;
- eval score;
- known failures.

Test at least three prompt versions on the same 20 questions.

## Project 2: Structured Output Extractor

Build a prompt and schema for extracting:

- entities;
- dates;
- obligations;
- risks;
- citations.

Acceptance criteria:

- valid JSON;
- no unsupported fields;
- no invented citations;
- graceful no-answer behavior.

## Project 3: Prompt Injection Test Suite

Create 15 adversarial examples:

- malicious retrieved document;
- user asks for system prompt;
- user asks to ignore policy;
- source says to reveal private data;
- source contains fake citation instructions.

For each case, define expected safe behavior.

