from enum import Enum
from abc import ABC
from common.state.state import State
from common.state.state_machine import StateMachine

class Command(State):
    keyword: str

    def execute(self, ) -> str:
        ...

    def match(self, command: str) -> bool:
        ...

