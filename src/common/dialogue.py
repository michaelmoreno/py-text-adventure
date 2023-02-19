from __future__ import annotations
from typing import Callable, Optional
from dataclasses import dataclass
from world.world_state import WorldState

@dataclass
class DialogueOption:
    text: str
    requirements: list[Optional[Callable[[WorldState], bool]]]
    effects: list[Optional[Callable[[WorldState], None]]]
    next: Optional[DialogueNode]

class DialogueNode:
    text: str
    options: list[DialogueOption]

    def __init__(self, text: str, options):
        self.text = text
        self.options = options
