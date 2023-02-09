from typing import Protocol
from common.state.state_machine import StateMachine

class State(Protocol):
    context: StateMachine

    def __init__(self, context: StateMachine):
        self.context = context

    def execute(self) -> None:
        ...

    # def exit()