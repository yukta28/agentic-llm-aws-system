import json
from src.agent.orchestrator import AgentOrchestrator
from src.agent.state import AgentState


def demo_llm_client(prompt: str) -> str:
    """
    Replace with Amazon Bedrock InvokeModel / Converse API call.
    This deterministic demo lets tests run locally.
    """
    if "order 123" in prompt.lower() and "shipped" not in prompt.lower():
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
