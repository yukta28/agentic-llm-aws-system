from typing import Dict, Any


def get_order_status(order_id: str) -> Dict[str, Any]:
    # Demo deterministic tool.
    fake_orders = {
        "123": {"status": "shipped", "eta": "2026-05-05"},
        "456": {"status": "processing", "eta": "unknown"},
    }
    return fake_orders.get(order_id, {"status": "not_found"})


def calculator(expression: str) -> Dict[str, Any]:
    # For a real project, do NOT eval arbitrary input.
    # This is intentionally restricted to simple digits/operators.
    allowed = set("0123456789+-*/(). ")
    if not set(expression).issubset(allowed):
        return {"error": "unsupported_expression"}
    try:
        return {"result": eval(expression, {"__builtins__": {}}, {})}
    except Exception as exc:
        return {"error": str(exc)}
