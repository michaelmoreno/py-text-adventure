from entities.creatures.creature import Creature
from common.state_machine import StateMachine, State

class Grab(State):
    def __init__(self, context: StateMachine, player: Creature):
        self.context = context
        self.player: Creature

    def execute(self):
        if self.player.location.has_item('sword'):
            self.player.inventory.add('sword')
            self.context.prompt = 'Sword added to inventory' # type: ignore
        return 'There is no such item nearby!'