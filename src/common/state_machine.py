from __future__ import annotations
from typing import Protocol
from abc import ABC, abstractmethod

class State(ABC):
    context: StateMachine
    
    def enter(self):
        ...
    @abstractmethod
    def execute(self) -> None:
        ...
        
    def exit(self):
        ...

class StateMachine:
    state: State

    def __init__(self, initial_state: State):
        self.state = initial_state
    
    def enter(self, state: State):
        self.state.exit()
        self.state = state
        self.state.execute()