from __future__ import annotations
from typing import Protocol

class State(Protocol):
    context: StateMachine

    def __init__(self, context: StateMachine):
        self.context = context

    def enter(self):
        ...
    def execute(self) -> None:
        ...
    def exit(self):
        ...

class StateMachine:
    state: State

    def __init__(self, initial_state: State):
        self.state = initial_state
    
    def enter(self, state: State):
        # self.state.exit()
        self.state = state
        self.state.execute()