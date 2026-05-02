SYSTEM_PROMPT = """
You are an agentic AI assistant.

Return only valid JSON.

Available action types:
1. tool_call
2. final_answer
3. reflect

Rules:
- Use tools only when needed.
- Do not invent tool results.
- If you have enough information, return final_answer.
- Keep responses concise.
"""

def build_prompt(state) -> str:
    return f"""
{SYSTEM_PROMPT}

User query:
{state.user_query}

Retrieved memory:
{state.memory}

Intermediate steps:
{state.intermediate_steps}

Return the next action as JSON.
"""
