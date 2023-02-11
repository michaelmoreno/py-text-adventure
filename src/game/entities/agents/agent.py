from game.entities.entity import Entity
from common.inventory import Inventory
from common.traits import TraitsDict
from game.locations.location import Location

class Agent(Entity):
    def __init__(self, id: int, name: str, inventory: Inventory, health: float, traits: TraitsDict, location: Location):
        super().__init__(id, name, inventory, health, traits, location)

