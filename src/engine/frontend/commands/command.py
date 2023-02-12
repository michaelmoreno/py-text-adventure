from __future__ import annotations
from typing import TYPE_CHECKING, Protocol, Any, TypeVar
if TYPE_CHECKING:
    from engine.frontend.io_handler import IOHandler
from abc import ABC, abstractmethod

T = TypeVar('T')

class Command(ABC):
    io: IOHandler

    def __init__(self, io: IOHandler):
        self.io = io

    @abstractmethod
    def handle(self, message: str) -> None:
        ...

    def _display_prompt(self) -> None:
        self.io.output(f"Select an option:")

    def _display_options(self, options: list[Any]) -> None:
        s = ''
        for i, option in enumerate(options):
            s += f'[ {i+1}. {option} ]'
        self.io.output(s)

    def _get_valid_choice(self, options: list[T]) -> T:
        choice = self.io.capture()
        if not choice.isdigit() or int(choice) > len(options):
            self.io.output('Invalid choice. Try again.')
            return self._get_valid_choice(options)
        return options[int(choice)-1]

    def select_option(self, options: list[T]) -> T:
        self._display_prompt()
        self._display_options(options)
        return self._get_valid_choice(options)


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
