import json
from src.agent.orchestrator import AgentOrchestrator
from src.agent.state import AgentState


def fake_llm(prompt: str) -> str:
    if "intermediate_steps=[]" in prompt.replace(" ", ""):
        return json.dumps({
            "type": "tool_call",
            "tool_name": "get_order_status",
            "tool_input": {"order_id": "123"}
        })
    return json.dumps({
        "type": "final_answer",
        "answer": "Order 123 has shipped."
    })


def test_agent_completes_order_task():
    agent = AgentOrchestrator(llm_client=fake_llm)
    state = AgentState(session_id="s1", user_query="What is the status of order 123?")
    result = agent.run(state)

    assert "shipped" in result["answer"].lower()
