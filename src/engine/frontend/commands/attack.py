from game.entities.entity import Entity
from common.state_machine import State
from engine.frontend.io_handler import IOHandler
from engine.frontend.commands.command import CommandFactory, Command
from world.world_state import WorldState


class BattleState(State):
    context: IOHandler
    npc: Entity
    world: WorldState

    def __init__(self, npc: Entity, world: WorldState):
        self.npc = npc
        self.world = world

    def sneak_attack(self) -> bool:
        return False

    def enter(self):
        if sneak_attack():

        weapon = self.world.player.inventory

    def execute(self) -> None:
        


        return super().execute()

class AttackCommand(Command):
    context: IOHandler
    world: WorldState

    def __init__(self, context: IOHandler, world: WorldState):
        self.context = context
        self.world = world

    def find_entity(self, name: str) -> Entity | None:
        entities = self.world.player.location.entities
        candidates = [entity for entity in entities
            if name in entity.name.lower()]
        
        match len(candidates):
            case 0:
                return None
            case 1:
                return candidates[0]
            case _:
                return self.io.select_option(
                    candidates,
                    'There are multiple entities with that name. Which are you referring to?')

    def handle(self, message: str) -> None:
        action, *args = message.strip().lower().split()
        if len(args) == 0:
            return self.context.output('Attack who? attack <name>')
        target = self.find_entity(*args)
        if target:
            self.context.enter(BattleState(target, self.world))
        else:
            self.context.output('No entity with that name found.') 

class TalkFactory(CommandFactory):
    world: WorldState

    def __init__(self, keywords: list[str], world_state: WorldState):
        super().__init__(keywords)
        self.world = world_state

    def build(self, context: IOHandler) -> TalkCommand:
        return TalkCommand(context, self.world)
