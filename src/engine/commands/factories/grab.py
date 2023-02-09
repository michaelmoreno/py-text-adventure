from engine.commands.factories.factory import CommandFactory
from engine.frontend.input_handler import IOHandler
from entities.creatures.creature import Creature
from engine.commands.states.grab.grab import Grab

class GrabFactory(CommandFactory):
    player: Creature
    context: IOHandler

    def build(self):
        return Grab(self.context, self.player)