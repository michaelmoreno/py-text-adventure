from game.entities.entity import Entity
from common.state_machine import StateMachine, State
from engine.frontend.commands.factory import CommandFactory
from engine.frontend.io_handler import IOHandler
from engine.frontend.commands.command import Command

class LookCommand(Command):
    context: IOHandler
    def __init__(self, context: IOHandler, player: Entity):
        self.context = context
        self.player = player
    
    def describe_entities(self):
        entities = [entity for entity in self.player.location.entities if entity != self.player]
        
        if any(entities):
            self.context.output('You see:')
            for entity in entities:
                self.context.output(entity.name)
        else:
            self.context.output("You don't see any entities...")
    
    def describe_items(self):
        items = self.player.location.items
        if len(items) == 0:
            self.context.output("You don't see any items...")
        else:
            self.context.output('You see:')
            for item in items:
                self.context.output(item.name)
        
    def describe_entrances(self):
        entrances = self.player.location.entrances
        if len(entrances) == 0:
            self.context.output("You don't see any entrances...")
        else:
            self.context.output('You see:')
            for entrance in entrances:
                self.context.output(entrance.name)

    def handle(self, message: str):
        action, *args = message.strip().lower().split()
        if len(args) == 0:
            return self.context.output('Look for what? look <entities/items/entrances/all>')
        if len(args) > 1:
            return self.context.output('Too many arguments. look <entities/items/entrances/all>')
        
        match args[0]:
            case 'entities':
                self.describe_entities()
            case 'items':
                self.describe_items()
            case 'entrances':
                self.describe_entrances()
            case 'all':
                self.describe_entities()
                self.describe_items()
                self.describe_entrances()
            case _:
                self.context.output("I don't understand what you want to look for.")
        

class LookFactory(CommandFactory):
    player: Entity

    def __init__(self, keywords: list[str], player: Entity):
        super().__init__(keywords)
        self.player = player

    def build(self, context: IOHandler):
        return LookCommand(context, self.player)
