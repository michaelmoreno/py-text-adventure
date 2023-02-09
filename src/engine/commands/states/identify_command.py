from common.state.state_machine import State, StateMachine
from engine.commands.factories.factory import CommandFactory
from engine.frontend.io_handler import IOHandler

class IdentifyCommand(State):
    context: IOHandler
    factories: list[CommandFactory]

    def __init__(self, context: IOHandler, factories: list[CommandFactory]):
        self.context = context
        self.factories = factories

    def match_command(self, message: str) -> State:
        for factory in self.factories:
            if factory.match(message):
                return factory.build()
        self.context.response = "I'm not sure what you're asking for..."
        return self

    def execute(self):
        next_state = self.match_command(self.context.received)
        self.context.enter(next_state)
        next_state.execute()
