from enum import Enum

class Action(Enum):
    GRAB = 1
    DROP = 2
    GO = 3
    TALK = 4
    STEAL = 5

class Command:
    keyword: str

    def execute(self, ) -> str:
        ...


    def match(self, command: str) -> bool:
        ...

