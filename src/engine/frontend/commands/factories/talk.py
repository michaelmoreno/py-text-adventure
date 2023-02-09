from engine.frontend.commands.factories.factory import CommandFactory
from game.entities.entity import Entity

class TalkFactory(CommandFactory):
    player: Entity

    def __init__(self, world_state: object):
        self.player = world_state.player # type: ignore
