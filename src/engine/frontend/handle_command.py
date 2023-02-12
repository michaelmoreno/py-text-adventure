from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from engine.frontend.io_handler import IOHandler
from engine.frontend.commands.factory import CommandFactory
from common.state_machine import State
from engine.frontend.commands.command import Command

class HandleCommand(State):
    context: IOHandler
    factories: list[CommandFactory]

    def __init__(self, context: IOHandler, factories: list[CommandFactory]):
        self.context = context
        self.factories = factories

    def match_command(self, message: str) -> Command | None:
        for factory in self.factories:
            if factory.match(message):
                return factory.build(self.context)
        return None

    def execute(self):
        message = self.context.capture()
        command = self.match_command(message)
        if command:
            command.handle(message)
        else:
            self.context.output('Invalid command. Try again.')
