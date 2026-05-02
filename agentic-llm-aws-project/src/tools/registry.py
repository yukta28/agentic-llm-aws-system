from typing import Any, Callable, Dict
from src.tools.sample_tools import get_order_status, calculator


TOOLS: Dict[str, Callable[..., Dict[str, Any]]] = {
    "get_order_status": get_order_status,
    "calculator": calculator,
}


def execute_tool(tool_name: str, tool_input: Dict[str, Any]) -> Dict[str, Any]:
    if tool_name not in TOOLS:
        return {"error": f"Unknown tool: {tool_name}"}

    try:
        return TOOLS[tool_name](**tool_input)
    except TypeError as exc:
        return {"error": f"Invalid tool input: {exc}"}
