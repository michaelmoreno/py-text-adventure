from commands.command import Command

class CommandHandler:
    commands: list[Command]

    def handle(self, message: str):
        for command in self.commands:
            if command.match(message):
                return command.execute()
        return 'Invalid command'