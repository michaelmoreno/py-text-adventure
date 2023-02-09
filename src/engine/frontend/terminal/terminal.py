import time
from engine.frontend.frontend import Frontend
from engine.frontend.io_handler import IOHandler

class TerminalFrontend(Frontend):
    def __init__(self):
        ...
        
    def display(self, text: str) -> None:
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.01)

    def capture(self) -> str:
        return input('>')

    def cycle(self) -> None:
        message = self.capture()