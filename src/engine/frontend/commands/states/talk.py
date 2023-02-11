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

    def enter_dialogue(self, dialogue):
        self.context.output(dialogue.text)
        options = ''
        for i, option in enumerate(dialogue.options):
            options += f'[ {i + 1}: {option.text} ]'
        self.context.output(options)
        

    def execute(self):
        npc = self.player.location.find_entity('Dax')
        if npc:
            dialogue = npc.dialogue_node
            self.enter_dialogue(dialogue)
        else:
            self.context.output('No entity found')
        

class TalkFactory(CommandFactory):
    player: Entity

    def __init__(self, keyword: str, world_state: object):
        super().__init__(keyword)
        self.player = world_state.player # type: ignore

    def build(self, context: IOHandler) -> Talk:
        return Talk(context, self.player)