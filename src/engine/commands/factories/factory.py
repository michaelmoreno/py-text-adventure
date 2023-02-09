from abc import ABC, abstractmethod
from engine.commands.command import Command

class CommandFactory(ABC):
    keyword: str

    def match(self, message: str) -> bool:
        return message == self.keyword
    
    @abstractmethod
    def build(self) -> Command:
        ...