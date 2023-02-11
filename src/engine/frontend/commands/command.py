from enum import Enum
from abc import ABC
from common.state_machine import State

class Command(State):
    def execute(self, ) -> str:
        ...
