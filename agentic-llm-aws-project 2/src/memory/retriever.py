from typing import List


def retrieve_memory(query: str) -> List[str]:
    """
    Placeholder for RAG retrieval.

    In production:
    - Embed query
    - Search vector index / Bedrock Knowledge Base
    - Return top-k relevant chunks
    """
    q = query.lower()
    memory = []

    if "order" in q:
        memory.append("Order tools can retrieve order status by order_id.")

    if "weather" in q or "temperature" in q or "forecast" in q:
        memory.append(
            "Current weather requires a real-time API call. Use get_current_weather(city, country_code?)."
        )

    return memory
