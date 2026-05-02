from typing import Any, Dict, Literal, Optional
from pydantic import BaseModel, Field


class ToolCall(BaseModel):
    type: Literal["tool_call"]
    tool_name: str
    tool_input: Dict[str, Any] = Field(default_factory=dict)


class FinalAnswer(BaseModel):
    type: Literal["final_answer"]
    answer: str


class Reflect(BaseModel):
    type: Literal["reflect"]
    note: str


AgentAction = ToolCall | FinalAnswer | Reflect
