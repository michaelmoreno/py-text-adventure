from __future__ import annotations
from common.state_machine import State
from typing import Callable, NamedTuple

class DialogueOption(NamedTuple):
    text: str
    requirements: list[Callable[[GameState], bool]]
    result: Dialogue

class Dialogue(State):
    text: str
    options: list[DialogueOption]

    def __init__(self, text: str, options):
        self.text = text
        self.options = options

    def execute(self):
        ...

# diag = Dialogue(
#     'Hi there! How are you?',:
#     (
#         'Good', Dialogue(
#             ''
#         )
#         'Who are you?'
#         )
# )
    


class DialogueContext:
    state: Dialogue

    def enter(self, dialogue: Dialogue ):
        ...