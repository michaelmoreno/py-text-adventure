from abc import ABC

class Frontend(ABC):
    prompt: Prompt

    def __init__(self, prompt: Prompt):
        self.prompt = prompt
