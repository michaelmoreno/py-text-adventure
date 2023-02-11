from game.entities.entity import Entity
from common.state_machine import StateMachine, State
from engine.frontend.commands.factory import CommandFactory
from engine.frontend.io_handler import IOHandler

class Grab(State):
    def __init__(self, context: StateMachine, player: Entity):
        self.context = context
        self.player: Entity

    def execute(self):
        if self.player.location.has_item('sword'):
            self.player.inventory.add('sword')
            self.context.prompt = 'Sword added to inventory' # type: ignore
        return 'There is no such item nearby!'

class GrabFactory(CommandFactory):
    player: Entity

    def build(self, context: IOHandler):
        return Grab(context, self.player)