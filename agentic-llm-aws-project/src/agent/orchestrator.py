import json
from typing import Callable, Dict, Any

from src.agent.prompts import build_prompt
from src.agent.state import AgentState
from src.tools.registry import execute_tool
from src.memory.retriever import retrieve_memory


class AgentOrchestrator:
    def __init__(self, llm_client: Callable[[str], str], max_steps: int = 5):
        self.llm_client = llm_client
        self.max_steps = max_steps

    def run(self, state: AgentState) -> Dict[str, Any]:
        state.memory = retrieve_memory(state.user_query)

        for _ in range(self.max_steps):
            prompt = build_prompt(state)
            raw_response = self.llm_client(prompt)

            try:
                action = json.loads(raw_response)
            except json.JSONDecodeError:
                state.add_step(
                    {"type": "invalid_json", "raw": raw_response},
                    {"error": "LLM returned invalid JSON"},
                )
                continue

            action_type = action.get("type")

            if action_type == "final_answer":
                return {"answer": action.get("answer", ""), "steps": len(state.intermediate_steps)}

            if action_type == "tool_call":
                observation = execute_tool(
                    action.get("tool_name", ""),
                    action.get("tool_input", {}),
                )
                state.add_step(action, observation)
                continue

            if action_type == "reflect":
                state.add_step(action, {"note": action.get("note", "")})
                continue

            state.add_step(action, {"error": "Unknown action type"})

        return {
            "answer": "I could not complete the task within the allowed number of steps.",
            "steps": len(state.intermediate_steps),
        }
