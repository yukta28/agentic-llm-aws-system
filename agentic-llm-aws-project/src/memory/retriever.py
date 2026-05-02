from typing import List


def retrieve_memory(query: str) -> List[str]:
    """
    Placeholder for RAG retrieval.

    In production:
    - Embed query
    - Search vector index / Bedrock Knowledge Base
    - Return top-k relevant chunks
    """
    if "order" in query.lower():
        return ["Order tools can retrieve order status by order_id."]
    return []
