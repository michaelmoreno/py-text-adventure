from __future__ import annotations
from common.state_machine import StateMachine, State
from engine.frontend.commands.states.identify_command import IdentifyCommand
from engine.frontend.commands.factory import CommandFactory
from engine.frontend.frontend import Frontend


class IOHandler(StateMachine):
    state: State
    frontend: Frontend

    def __init__(self, frontend: Frontend, command_factories: list[CommandFactory]):
        self.frontend = frontend
        self.state = IdentifyCommand(self, command_factories)
        self.identify_command = self.state
    
    def handle(self):
        self.state.execute()

    def enter(self, state: State):
        self.state = state
        self.state.context = self
        self.state.enter()
    
    def capture(self) -> str:
        return self.frontend.capture()

    def output(self, message: str):
        self.frontend.display(message)
    
    def reset(self):
        self.enter(self.identify_command)

