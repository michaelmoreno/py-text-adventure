from __future__ import annotations
from common.state_machine import State
from typing import Callable, NamedTuple
from engine.frontend.io_handler import IOHandler

class DialogueOption(NamedTuple):
    text: str
    requirements: list[Callable[[object], bool]]
    result: DialogueNode

class DialogueNode(State):
    context: IOHandler
    text: str
    options: list[DialogueOption]

    def __init__(self, context: IOHandler, text: str, options):
        self.context = context
        self.text = text
        self.options = options

    def execute(self):
        self.context.output(self.text)
        self.context.output(''.join([option.text for option in self.options]))
        self.context.capture()
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