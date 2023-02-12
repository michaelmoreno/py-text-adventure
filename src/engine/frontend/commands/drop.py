from game.entities.entity import Entity
from engine.frontend.commands.command import CommandFactory, Command
from engine.frontend.io_handler import IOHandler
from game.items.item import Item

class DropCommand(Command):
    io: IOHandler

    def __init__(self, io: IOHandler, player: Entity):
        super().__init__(io)
        self.player = player

    def find_item(self, name: str) -> Item | None:
        items = [item for item in self.player.inventory.items
            if name in item.name.lower()]

        match len(items):
            case 0:
                return None
            case 1:
                return items[0]
            case _:
                return self.io.select_option(
                    items,
                    'There are multiple items with that name. Which one do you mean?')

    def handle(self, message: str):
        action, *args = message.strip().lower().split()
        if len(args) == 0:
            return self.io.output('Drop what? drop <item>')
        target = self.find_item(*args)
        if target:
            self.player.inventory.remove(target)
            self.player.location.items.append(target)
            self.io.output(f'{target.name} removed from inventory.')
        else:
            self.io.output(f"You don't have any {args[0]}'s!")

class DropFactory(CommandFactory):
    player: Entity

    def __init__(self, keywords: list[str], player: Entity):
        super().__init__(keywords)
        self.player = player

    def build(self, io: IOHandler):
        return DropCommand(io, self.player)
