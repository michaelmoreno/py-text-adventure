from __future__ import annotations
from common.state_machine import StateMachine, State
from engine.frontend.commands.states.identify_command import IdentifyCommand
from engine.frontend.commands.factories.factory import CommandFactory
from engine.frontend.frontend import Frontend
class IOHandler(StateMachine):
    state: State
    frontend: Frontend

    def __init__(self, frontend: Frontend, command_factories: list[CommandFactory]):
        self.frontend = frontend
        self.state = IdentifyCommand(self, command_factories)
    

    def capture(self) -> str:
        return self.frontend.capture()

    def match_command(self, message: str) -> State:
        for factory in self.factories:
            if factory.match(message):
                return factory.build(self.context)
        return self

    def update(self):
        message = self.capture()
        # need to make decision about setting state back to identifycommand
        self.state.execute()

    def enter(self, state: State):
        self.state = state
        self.state.execute()

    def output(self, message: str):
        self.frontend.display(message)
