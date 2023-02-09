from engine.commands.factories.factory import CommandFactory
from engine.frontend.input_handler import InputHandler
from entities.creatures.creature import Creature
from engine.commands.states.grab.grab import Grab

class GrabFactory(CommandFactory):
    player: Creature
    context: InputHandler

    def build(self):
        return Grab(self.context, self.player)