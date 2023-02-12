from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from engine.frontend.io_handler import IOHandler
from engine.frontend.commands.factory import CommandFactory
from common.state_machine import State
from engine.frontend.commands.command import Command

class IdentifyCommand(State):
    context: IOHandler
    factories: list[CommandFactory]
    commands: list[Command]

    def __init__(self, context: IOHandler, factories: list[CommandFactory]):
        self.context = context
        self.factories = factories

    def execute(self):
        message = self.context.capture()
        for command in self.commands:
            if command.match(message):
                return command.execute(message)
        self.context.output('Invalid command. Try again.')
