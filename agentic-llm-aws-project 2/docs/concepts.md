# Concepts

## Agent as a policy function

You can model the agent as:

```text
π(state) -> action
```

Where:

- `state` contains the user request, conversation, memory, and tool results.
- `action` is one of:
  - `tool_call`
  - `final_answer`
  - `reflect`
  - `error`

## Why JSON actions?

LLMs are flexible, but production systems need structure.

Bad:

```text
Maybe call the weather API?
```

Good:

```json
{
  "type": "tool_call",
  "tool_name": "get_weather",
  "tool_input": {
    "city": "Seattle"
  }
}
```

Structured outputs make validation and retries possible.

## Tool design rules

Tools should be:

- Narrow
- Validated
- Observable
- Idempotent when possible
- Protected by authorization checks

## Memory is retrieval, not storage

Long-term memory should not mean dumping everything into the prompt.

A better pattern:

```text
user query -> embedding/search -> top relevant chunks -> prompt context
```

## Evaluation

Evaluate the full system, not only the model.

Track:

- Task success
- Tool selection accuracy
- Invalid action rate
- Average number of loop steps
- Latency
- Cost per request
