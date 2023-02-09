from entities.creatures.creature import Creature
from common.state.state_machine import StateMachine
from common.state.state import State
from common.dialogue import Dialogue

class Talk(State):
    def __init__(self, context: StateMachine, player: Creature):
        self.context: StateMachine
        self.player: Creature


    def execute(self):
        if self.player.location.has_entity('dax'):
            dialogue = Dialogue # type: ignore
            self.context.enter(dialogue)
        