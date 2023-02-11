from __future__ import annotations
from typing import Literal
from common.inventory import Inventory
from common.traits import TraitsDict
from locations.location import Location
from common.dialogue import DialogueNode



class Entity:
    id: int
    name: str
    inventory: Inventory
    health: float
    traits: TraitsDict
    location: Location
    # relationships: dict[Entity, Relationship]
    dialogue_node: DialogueNode

    def __init__(self, id: int, name: str, inventory: Inventory, health: float, traits: TraitsDict, location: Location):
        self.int = id
        self.name = name
        self.inventory = inventory
        self.health = health
        self.traits = traits
        self.location = location
        # self.relationships = {}
        # self.dialogue_node = None

    def goto(self, location: Location):
        self.location = location
        location.entities.append(self)
