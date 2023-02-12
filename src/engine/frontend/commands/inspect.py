from game.items.item import Item
from game.entities.entity import Entity
from game.entities.entity import Location
from engine.frontend.commands.command import CommandFactory
from engine.frontend.io_handler import IOHandler
from engine.frontend.commands.command import Command

class LookCommand(Command):
    io: IOHandler

    def __init__(self, io: IOHandler, player: Entity):
        super().__init__(io)
        self.player = player
    
    def find_thing(self, name: str) -> Item | Entity | Location | None:
        nearby = self.player.location
        things = nearby.items + nearby.entities + nearby.entrances
        candidates = [x for x in things if name in x.name.lower()]

        match len(candidates):
            case 0:
                return None
            case 1:
                return candidates[0]
            case _:
                return self.io.select_option(
                    candidates, 
                    'There are multiple things with that name. Which one do you mean?',
                    '[ {index}: {name} ({type}) ]')
    
    def handle(self, message: str):
        action, *args = message.strip().lower().split()
        if len(args) == 0:
            return self.io.output('Inspect what? inspect <item/entity>')
        target = self.find_thing(*args)
        if target:
            self.io.output(target.description)
        else:
            self.io.output(f"I don't see a {args[0]} here...")

class InspectFactory(CommandFactory):
    player: Entity

    def __init__(self, keywords: list[str], player: Entity):
        super().__init__(keywords)
        self.player = player

    def build(self, io: IOHandler):
        return LookCommand(io, self.player)
