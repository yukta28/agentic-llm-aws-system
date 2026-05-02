import json
import re

from src.agent.orchestrator import AgentOrchestrator
from src.agent.state import AgentState


def _extract_city(prompt: str) -> str:
    """
    Tiny deterministic parser for local demo only.
    A production version should let the LLM produce structured tool input.
    """
    match = re.search(r"weather(?: in| for)? ([A-Za-z .-]+)", prompt, re.IGNORECASE)
    if match:
        city = match.group(1).split("\n")[0].strip(" ?.!")
        return city or "Seattle"
    return "Seattle"


def demo_llm_client(prompt: str) -> str:
    """
    Replace with Amazon Bedrock InvokeModel / Converse API call.
    This deterministic demo lets tests run locally.
    """
    lower = prompt.lower()

    if ("weather" in lower or "temperature" in lower) and "source='open-meteo'" not in lower and '"source": "Open-Meteo"' not in prompt:
        return json.dumps({
            "type": "tool_call",
            "tool_name": "get_current_weather",
            "tool_input": {"city": _extract_city(prompt)}
        })

    if "open-meteo" in lower:
        return json.dumps({
            "type": "final_answer",
            "answer": "I called the real weather API and returned the current conditions from Open-Meteo."
        })

    if "order 123" in lower and "shipped" not in lower:
        return json.dumps({
            "type": "tool_call",
            "tool_name": "get_order_status",
            "tool_input": {"order_id": "123"}
        })

    return json.dumps({
        "type": "final_answer",
        "answer": "Order 123 has shipped and is estimated to arrive on 2026-05-05."
    })


def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))
    session_id = body.get("session_id", "demo-session")
    query = body["query"]

    state = AgentState(session_id=session_id, user_query=query)
    agent = AgentOrchestrator(llm_client=demo_llm_client)
    result = agent.run(state)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(result)
    }
