from __future__ import annotations
from common.state_machine import State
from typing import Callable, NamedTuple, Optional
from engine.frontend.io_handler import IOHandler
from world.world_state import WorldState

class DialogueOption(NamedTuple):
    text: str
    next: Optional[DialogueNode] = None
    requirements: list[Callable[[WorldState], bool]] = []
    effects: list[Callable[[WorldState], None]] = []


class DialogueNode:
    text: str
    options: list[DialogueOption]

    def __init__(self, text: str, options):
        self.text = text
        self.options = options
