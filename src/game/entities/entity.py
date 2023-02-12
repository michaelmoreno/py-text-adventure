from __future__ import annotations
from typing import Literal
from common.inventory import Inventory
from common.traits import TraitsDict
from game.locations.location import Location
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from common.dialogue import DialogueNode



class Entity:
    id: int
    name: str
    description: str
    inventory: Inventory
    health: float
    traits: TraitsDict
    location: Location
    dialogue_node: DialogueNode | None

    def __init__(self, id: int, name: str, description: str, inventory: Inventory, health: float, traits: TraitsDict, location: Location, dialogue_node: DialogueNode):
        self.int = id
        self.description = description
        self.name = name
        self.inventory = inventory
        self.health = health
        self.traits = traits
        self.location = location
        self.dialogue_node = dialogue_node

    def goto(self, location: Location):
        self.location = location
        location.entities.append(self)
