from __future__ import annotations
from common.state_machine import StateMachine, State
from engine.frontend.handle_command import HandleCommand
from engine.frontend.commands.factory import CommandFactory
from engine.frontend.frontend import Frontend


class IOHandler(StateMachine):
    state: State
    frontend: Frontend

    def __init__(self, frontend: Frontend, command_factories: list[CommandFactory]):
        self.frontend = frontend
        self.state = HandleCommand(self, command_factories)
        self.handle_command = self.state
    
    def update(self):
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
        self.enter(self.handle_command)

