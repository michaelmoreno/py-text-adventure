from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from engine.frontend.io_handler import IOHandler
from abc import ABC, abstractmethod
from engine.frontend.commands.command import Command

class CommandFactory(ABC):
    keywords: list[str]

    def __init__(self, keywords: list[str]):
        self.keywords = keywords

    def match(self, message: str) -> bool:
        action, *args = message.strip().lower().split()
        return action in self.keywords
    
    @abstractmethod
    def build(self, context: IOHandler) -> Command:
        ...