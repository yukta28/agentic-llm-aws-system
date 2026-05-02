from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class IntermediateStep:
    action: Dict[str, Any]
    observation: Dict[str, Any]


@dataclass
class AgentState:
    session_id: str
    user_query: str
    history: List[Dict[str, str]] = field(default_factory=list)
    memory: List[str] = field(default_factory=list)
    intermediate_steps: List[IntermediateStep] = field(default_factory=list)

    def add_step(self, action: Dict[str, Any], observation: Dict[str, Any]) -> None:
        self.intermediate_steps.append(
            IntermediateStep(action=action, observation=observation)
        )
