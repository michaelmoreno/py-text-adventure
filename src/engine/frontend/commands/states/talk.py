from game.entities.entity import Entity
from common.state_machine import State
from engine.frontend.io_handler import IOHandler
from engine.frontend.commands.factory import CommandFactory

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
        

class TalkFactory(CommandFactory):
    player: Entity

    def __init__(self, world_state: object):
        self.player = world_state.player # type: ignore

    def build(self, context: IOHandler) -> Talk:
        return Talk(context, self.player)