from __future__ import annotations
from typing import TypeVar, Any
from common.state_machine import StateMachine, State
from engine.frontend.handle_command import HandleCommand
from engine.frontend.commands.command import CommandFactory
from engine.frontend.frontend import Frontend

T = TypeVar('T')

class IOHandler(StateMachine):
    state: State
    frontend: Frontend

    def __init__(self, frontend: Frontend, command_factories: list[CommandFactory]):
        self.frontend = frontend
        self.state = HandleCommand(self, command_factories)
        self.handle_command = self.state
    
    def update(self):
        self.state.execute()

    def enter(self, state: State):
        self.state = state
        self.state.context = self
        self.state.enter()
    
    def capture(self) -> str:
        return self.frontend.capture()

    def output(self, message: str):
        self.frontend.display(message)
    
    def reset(self):
        self.enter(self.handle_command)

    def interpolate(self, message: str, option, i) -> str:
        lookup = {
            '{index}': i,
            '{name}': getattr(option, 'name', option),
            '{description}': getattr(option, 'description', ''),
            '{type}': type(option).__name__,
            '{text}': getattr(option, 'text', option)}

        for key, value in lookup.items():
            if key in message:
                message = message.replace(key, str(value))
        return message

    def display_options(self, options: list[Any], prompt: str, template: str, delimiter: str) -> None:
        self.output(prompt)
        self.output(delimiter.join(
                self.interpolate(template, option, i+1)
                for i, option in enumerate(options)))

    def valid_number(self, choice: str, options: list[Any]) -> bool:
        return choice.isdigit() and int(choice) <= len(options)

    def get_valid_choice(self, options: list[T]) -> T:
        choice = self.capture()
        if not self.valid_number(choice, options):
            self.output('Invalid choice. Try again.')
            return self.get_valid_choice(options)
        return options[int(choice)-1]

    def select_option(self, 
        options: list[T], 
        prompt: str = "Select an option:",
        template: str = '[ {index}: {name} ]',
        delimiter: str = '') -> T:

        self.display_options(options, prompt, template, delimiter)
        return self.get_valid_choice(options)
