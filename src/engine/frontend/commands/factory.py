from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from engine.frontend.io_handler import IOHandler
from abc import ABC, abstractmethod
from engine.frontend.commands.command import Command

class CommandFactory(ABC):
    keyword: str

    def __init__(self, keyword: str):
        self.keyword = keyword

    def match(self, message: str) -> bool:
        return message == self.keyword
    
    @abstractmethod
    def build(self, context: IOHandler) -> Command:
        ...