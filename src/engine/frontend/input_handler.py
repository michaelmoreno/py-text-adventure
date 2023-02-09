from enum import Enum
from common.state.state_machine import StateMachine, State
from engine.commands.states.identify_command import IdentifyCommand

class PromptMode(Enum):
    COMMAND = 0
    DIALOGUE = 1
    BATTLE = 2


class InputHandler(StateMachine):
    state: State
    prompt: str

    def __init__(self, initial_state: State):
        # self.state = IdentifyCommand(self, [])
        self.prompt = '>'
    
    def handle(self, message: str) -> str:
        self.state.execute()
        return self.prompt

    def enter(self, state: State):
        self.state = state

# should the frontend call input handler, or input handler call frontend?