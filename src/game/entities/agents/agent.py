from game.entities.entity import Entity
from common.inventory import Inventory
from common.traits import TraitsDict
from game.locations.location import Location
from common.dialogue import DialogueNode

class Agent(Entity):
    def __init__(self, id: int, name: str, inventory: Inventory, health: float, traits: TraitsDict, location: Location, dialogue_node: DialogueNode):
        super().__init__(id, name, 'blank', inventory, health, traits, location, dialogue_node)

