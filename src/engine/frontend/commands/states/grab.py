from game.entities.entity import Entity
from common.state_machine import StateMachine, State
from engine.frontend.commands.factory import CommandFactory
from engine.frontend.io_handler import IOHandler

class Grab(State):
    context: IOHandler
    def __init__(self, player: Entity):
        self.player: Entity

    def execute(self):
        if self.player.location.has_item('sword'):
            self.player.inventory.add('sword')
            self.context.prompt = 'Sword added to inventory' # type: ignore
        return 'There is no such item nearby!'

class GrabFactory(CommandFactory):
    player: Entity

    def __init__(self, keyword: str, player: Entity):
        super().__init__(keyword)
        self.player = player

    def build(self, context: IOHandler):
        return Grab(self.player)