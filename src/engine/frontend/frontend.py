from abc import ABC

class Frontend(ABC):
    def capture(self) -> str:
        ...