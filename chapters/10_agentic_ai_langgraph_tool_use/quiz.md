# Quiz: Agentic AI, LangGraph, and Tool Use

## Multiple Choice

1. What makes an AI system agentic?
   - A. It can use tools, state, and workflow steps toward a goal
   - B. It only generates one answer
   - C. It cannot be logged
   - D. It never needs permissions

2. Where should tool permissions be enforced?
   - A. Only inside the model prompt
   - B. In the application/tool service boundary
   - C. Nowhere
   - D. In the UI color scheme

3. What does LangGraph help model?
   - A. Stateful graph-based workflows
   - B. CSS layouts
   - C. SQL indexes only
   - D. Docker images

4. Which is an agent evaluation target?
   - A. Tool selection correctness
   - B. Tool argument correctness
   - C. Human approval trigger correctness
   - D. All of the above

5. Why is memory risky?
   - A. It can leak private data or preserve stale context
   - B. It makes vector search impossible
   - C. It prevents logging
   - D. It replaces authentication

## Fill in the Blanks

1. A tool should define input schema, output schema, permissions, side effects, timeout, and ________ policy.
2. LangGraph workflows use nodes, edges, conditional routing, and shared ________.
3. Human approval is useful for risky or irreversible ________.
4. Tool outputs should be treated as data and may contain prompt ________.
5. Agent traces help debug decisions and state ________.

## Short Answer

1. Explain why an agent is more dangerous than a chatbot.
2. Design a safe tool wrapper for `create_review_task`.
3. Name five agent failure modes.

## Answer Key

### Multiple Choice

1. A
2. B
3. A
4. D
5. A

### Fill in the Blanks

1. retry
2. state
3. actions
4. injection
5. transitions

