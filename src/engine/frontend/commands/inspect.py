from game.items.item import Item
from game.entities.entity import Entity
from game.entities.entity import Location
from engine.frontend.commands.command import CommandFactory
from engine.frontend.io_handler import IOHandler
from engine.frontend.commands.command import Command

class LookCommand(Command):
    context: IOHandler
    def __init__(self, context: IOHandler, player: Entity):
        self.context = context
        self.player = player

    def select_candidate(self, candidates: list[Item | Entity | Location]) -> Item | Entity | Location:
        self.context.output('There are multiple things with that name. Which are you referring to?')
        self.context.output(' '.join(
            f"[{i+1}. {thing.name} ({type(thing).__name__})]"
            for i,thing in enumerate(candidates)))
        choice = self.context.capture()
        if not choice.isdigit() or int(choice) > len(candidates):
            self.context.output('Invalid choice. Try again.')
            return self.select_candidate(candidates)
        return candidates[int(choice)-1]

    
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
                return self.select_candidate(candidates) # type: ignore
    
    def handle(self, message: str):
        action, *args = message.strip().lower().split()
        if len(args) == 0:
            return self.context.output('Inspect what? inspect <item/entity>')
        target = self.find_thing(*args)
        if target:
            self.context.output(target.description)
        else:
            self.context.output(f"I don't see a {args[0]} here...")

class InspectFactory(CommandFactory):
    player: Entity

    def __init__(self, keywords: list[str], player: Entity):
        super().__init__(keywords)
        self.player = player

    def build(self, context: IOHandler):
        return LookCommand(context, self.player)
