from game.entities.entity import Entity
from common.state_machine import State
from engine.frontend.io_handler import IOHandler

class Talk(State):
    context: IOHandler
    player: Entity

    def __init__(self, context: IOHandler, player: Entity):
        self.context = context
        self.player = player

    def execute(self):
        npc = self.player.location.find_entity('dax')
        if npc:
            dialogue = npc.dialogue_node
            self.context.enter(dialogue)
        else:
            self.context.output('No entity found')
        