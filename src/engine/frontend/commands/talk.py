from game.entities.entity import Entity
from common.state_machine import State
from common.dialogue import DialogueOption
from engine.frontend.io_handler import IOHandler
from engine.frontend.commands.command import CommandFactory, Command
from world.world_state import WorldState


class DialogueState(State):
    context: IOHandler
    npc: Entity
    world: WorldState

    def __init__(self, npc: Entity, world: WorldState):
        self.npc = npc
        self.world = world

    def enter(self):
        if self.npc.dialogue_node is None:
            self.context.output(f'{self.npc.name} has nothing to say.')
            return 
        self.context.output(self.npc.dialogue_node.text)

    def requirements_met(self, option: DialogueOption) -> bool:
        return all(predicate(self.world) for predicate in option.requirements)

    def pick_response(self, options: list[DialogueOption]) -> DialogueOption:
        choice = self.context.select_option(
            options,
            prompt='',
            template='[ {index}: {text} ]')
        if not self.requirements_met(choice):
            self.context.output('Requirements not met!')
            return self.pick_response(options)
        return choice

    def apply_effects(self, option: DialogueOption):
        for effect in option.effects:
            effect(self.world)

    def execute(self):
        dialogue = self.npc.dialogue_node

        if dialogue is None:
            self.context.output(f'{self.npc.name} has nothing to say.')
            return 
        if len(dialogue.options) == 0:
            return self.context.reset()
        
        choice = self.pick_response(dialogue.options)
        self.apply_effects(choice)
        self.npc.dialogue_node = choice.next
        self.context.enter(
            DialogueState(self.npc, self.world))


class TalkCommand(Command):
    context: IOHandler
    world: WorldState

    def __init__(self, context: IOHandler, world: WorldState):
        self.context = context
        self.world = world

    def find_entity(self, name: str) -> Entity | None:
        entities = self.world.player.location.entities
        candidates = [entity for entity in entities if name in entity.name]
        
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
        action, *args = message.lower().split()
        if len(args) == 0:
            return self.context.output('Talk to who? talk <name>')
        target = self.find_entity(*args)
        if target:
            self.context.enter(DialogueState(target, self.world))
        else:
            self.context.output('No entity with that name found.') 

class TalkFactory(CommandFactory):
    world: WorldState

    def __init__(self, keywords: list[str], world_state: WorldState):
        super().__init__(keywords)
        self.world = world_state

    def build(self, context: IOHandler) -> TalkCommand:
        return TalkCommand(context, self.world)
