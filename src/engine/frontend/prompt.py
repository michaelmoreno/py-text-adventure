from enum import Enum
from engine.commands.handler import CommandHandler

class PromptMode(Enum):
    COMMAND = 0
    DIALOGUE = 1
    BATTLE = 2


class Prompt:
    mode: PromptMode
    command_handler: CommandHandler

    def __init__(self, mode: PromptMode = PromptMode.COMMAND):
        self.mode = mode
    
    def handle(self, message: str) -> str:
        match self.mode:
            case PromptMode.COMMAND:
                return self.command_handler.handle(message)
            case PromptMode.DIALOGUE:
                # return 
                ...

    def set_mode(self, mode: PromptMode):
        self.mode = mode