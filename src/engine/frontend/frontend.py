from abc import ABC
from engine.frontend.input_handler import IOHandler

class Frontend(ABC):
    input_handler: IOHandler

    def __init__(self, input_handler: IOHandler):
        self.input_handler = input_handler
