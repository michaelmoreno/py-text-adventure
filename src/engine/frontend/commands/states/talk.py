from game.entities.entity import Entity
from common.state_machine import State
from common.dialogue import DialogueOption, DialogueNode
from engine.frontend.io_handler import IOHandler
from engine.frontend.commands.factory import CommandFactory
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

    def display_choices(self, options: list[DialogueOption]):
        s = ''
        for i, option in enumerate(options):
            s += f'[ {i+1}: {option.text} ]'
        self.context.output(s)

    def requirements_met(self, option: DialogueOption) -> bool:
        return all(predicate(self.world) for predicate in option.requirements)

    def valid_number(self, choice: str, options: list[DialogueOption]) -> bool:
        return choice.isdigit() and int(choice) <= len(options) 


    def select_choice(self, options: list[DialogueOption]) -> DialogueOption:
        choice = self.context.capture()
        if not self.valid_number(choice, options):
            self.context.output('Invalid choice. Try again.')
            return self.select_choice(options)
            
        if not self.requirements_met(options[int(choice)-1]):
            self.context.output('Requirements not met!')
            return self.select_choice(options)

        return options[int(choice)-1]

    def apply_effects(self, option: DialogueOption):
        for effect in option.effects:
            effect(self.world)

    def execute(self):
        dialogue = self.npc.dialogue_node

        if dialogue is None:
            self.context.output(f'{self.npc.name} has nothing to say.')
            return 
        if dialogue.options is None:
            return
        
        self.display_choices(dialogue.options)
        choice = self.select_choice(dialogue.options)
        self.apply_effects(choice)
        self.npc.dialogue_node = choice.next
        self.context.enter(
            DialogueState(self.npc, self.world))


class Talk(State):
    context: IOHandler
    world: WorldState

    def __init__(self, context: IOHandler, world: WorldState):
        self.context = context
        self.world = world

    def execute(self):
        npc = self.world.player.location.find_entity('Dax')
        if npc:
            self.context.enter(DialogueState(npc, self.world))
        else:
            self.context.output('No entity found')
        

class TalkFactory(CommandFactory):
    world: WorldState

    def __init__(self, keyword: str, world_state: object):
        super().__init__(keyword)
        self.world = world_state # type: ignore

    def build(self, context: IOHandler) -> Talk:
        return Talk(context, self.world)