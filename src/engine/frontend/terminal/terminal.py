import time
from engine.frontend.frontend import Frontend
from engine.frontend.input_handler import IOHandler

class Terminal(Frontend):
    def __init__(self, input_handler: IOHandler):
        super().__init__(input_handler)

    def display(self, text: str) -> None:
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.01)

    def capture(self) -> str:
        return input('>')

    def cycle(self) -> None:
        message = self.capture()
        response = self.input_handler.handle(message)