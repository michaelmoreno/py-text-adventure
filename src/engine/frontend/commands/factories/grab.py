from engine.frontend.commands.factories.factory import CommandFactory
from engine.frontend.io_handler import IOHandler
from engine.frontend.commands.states.grab import Grab
from entities.creatures.creature import Creature

class GrabFactory(CommandFactory):
    player: Creature

    def build(self, context: IOHandler):
        return Grab(context, self.player)