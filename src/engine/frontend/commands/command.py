from enum import Enum
from abc import ABC
from common.state_machine import State

class Command(State):
    keyword: str

    def execute(self, ) -> str:
        ...

    def match(self, command: str) -> bool:
        ...

