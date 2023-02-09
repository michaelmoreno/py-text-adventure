from __future__ import annotations
from typing import Literal
from entities.entity import Entity
from common.inventory import Inventory
from common.traits import TraitsDict
from locations.location import Location


Relationship = Literal['Friendly', 'Hostile', 'Neutral']

class Creature(Entity):
    name: str
    inventory: Inventory
    health: float
    traits: TraitsDict
    relationships: dict[Creature, Relationship]

    def __init__(self, name: str, inventory: Inventory, health: float, traits: TraitsDict):
        self.name = name
        self.inventory = inventory
        self.health = health
        self.traits = traits

    def goto(self, location: Location):
        self.location = location
        location.entities.append(self)