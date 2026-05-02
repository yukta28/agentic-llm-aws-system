# Evaluation Plan

## Offline evaluation

Create a dataset:

```json
[
  {
    "task": "Find the status of order 123",
    "expected_tool": "query_order",
    "expected_answer_contains": ["shipped"]
  }
]
```

Measure:

- Did the agent choose the right tool?
- Did the tool input schema validate?
- Did the final answer use the tool result?
- How many steps did it take?

## Runtime metrics

Emit these per request:

- `agent.total_latency_ms`
- `agent.llm_latency_ms`
- `agent.tool_latency_ms`
- `agent.steps`
- `agent.invalid_actions`
- `agent.tool_errors`
- `agent.final_status`

## Failure tests

Test for:

- Tool timeout
- Invalid JSON from the LLM
- Missing required tool arguments
- Prompt injection inside retrieved memory
- Infinite loops
