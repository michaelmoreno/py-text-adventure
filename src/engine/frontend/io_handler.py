from enum import Enum
from common.state.state_machine import StateMachine, State
from engine.commands.states.identify_command import IdentifyCommand
from engine.commands.factories.factory import CommandFactory

class PromptMode(Enum):
    COMMAND = 0
    DIALOGUE = 1
    BATTLE = 2


class IOHandler(StateMachine):
    state: State
    received: str
    response: str

    def __init__(self, command_factories: list[CommandFactory]):
        self.state = IdentifyCommand(self, command_factories)
        self.received = ''
        self.response = ''
    
    def handle(self, message: str) -> str:
        self.received = message
        self.state.execute()
        return self.response

    def enter(self, state: State):
        self.state = state

# should the frontend call input handler, or input handler call frontend?