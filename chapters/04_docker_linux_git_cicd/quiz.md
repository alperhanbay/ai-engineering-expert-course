# Quiz: Docker, Linux, Git, and CI/CD

## Multiple Choice

1. What is a Docker image?
   - A. A running process
   - B. A packaged filesystem and metadata used to create containers
   - C. A SQL table
   - D. A vector embedding

2. Why should real secrets not be committed to `.env.example`?
   - A. It slows down Python
   - B. It exposes credentials and creates security risk
   - C. Docker cannot read environment variables
   - D. Git does not support text files

3. What should a CI pipeline usually run on every pull request?
   - A. Formatting checks and tests
   - B. Manual production deploy only
   - C. Full fine-tuning of a large model
   - D. No checks

4. In AI systems, what may need versioning besides code?
   - A. Prompts
   - B. Index versions
   - C. Evaluation datasets
   - D. All of the above

5. Why is Docker Compose useful during development?
   - A. It runs multiple dependent services locally
   - B. It replaces all security controls
   - C. It trains foundation models automatically
   - D. It removes the need for tests

## Fill in the Blanks

1. A container is a running instance of an ________.
2. A rollback plan must know which artifact ________.
3. `.env.example` should document variables but not contain real ________.
4. CI means continuous ________.
5. Docker Compose is useful for local multi-service ________ testing.

## Short Answer

1. Name five services that might appear in a local RAG Docker Compose stack.
2. Why should prompts be versioned?
3. What is the difference between a fast CI eval and a full release eval?

## Answer Key

### Multiple Choice

1. B
2. B
3. A
4. D
5. A

### Fill in the Blanks

1. image
2. changed
3. secrets
4. integration
5. integration

