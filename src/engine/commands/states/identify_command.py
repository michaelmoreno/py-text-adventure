from common.state.state_machine import State, StateMachine
from engine.commands.factories.factory import CommandFactory

class IdentifyCommand(State):
    def __init__(self, context: StateMachine, factories: list[CommandFactory], message: str):
        self.context = context
        self.factories = factories
        self.message = message

    def match_command(self, message: str):
        for factory in self.factories:
            if factory.match(message):
                return factory.build()
        return self

    def execute(self):
        next_state = self.match_command(self.message)
        self.context.enter(next_state)
        next_state.execute()
