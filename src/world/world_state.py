from typing import Literal
from game.entities.entity import Entity
from game.locations.location import Location


Relationship = Literal['friendly', 'neutral', 'hostile']

class WorldState:
    relationships: dict[Entity, dict[Entity, Relationship]]
    questlines: list[object] # type: ignore
    locations: list[Location] # type: ignore
    player: Entity

    def __init__(self):
        self.relationships = {}
        self.questlines = []
        self.locations = []
        # self.player