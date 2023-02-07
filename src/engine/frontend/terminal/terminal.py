from engine.frontend.frontend import Frontend

class Terminal(Frontend):
    def __init__(self, prompt: Prompt):
        super().__init__(prompt)
        self.prompt = prompt

    def display(self, text: str) -> None:
        print(text)

    def capture(self) -> str:
        return input()

    def cycle(self) -> None:
        message = self.capture()
        response = self.prompt.handle(message)