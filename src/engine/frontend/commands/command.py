from enum import Enum
from abc import ABC
from common.state_machine import State

class Command:
    def match(self, message: str) -> bool:
        ...
    def handle(self, message: str) -> None:
        ...
