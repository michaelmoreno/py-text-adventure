from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from engine.frontend.io_handler import IOHandler
from engine.frontend.commands.factory import CommandFactory
from common.state_machine import State

class IdentifyCommand(State):
    context: IOHandler
    factories: list[CommandFactory]

    def __init__(self, context: IOHandler, factories: list[CommandFactory]):
        self.context = context
        self.factories = factories

    def match_command(self, message: str) -> State:
        for factory in self.factories:
            if factory.match(message):
                return factory.build(self.context)
        return self

    def execute(self):
        message = self.context.capture()
        next_state = self.match_command(message)
        self.context.enter(next_state)
        next_state.execute()