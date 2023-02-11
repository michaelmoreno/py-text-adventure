from typing import Literal
from game.entities.entity import Entity


Relationship = Literal['friendly', 'neutral', 'hostile']

class WorldState:
    relationships: dict[Entity, dict[Entity, Relationship]]
    questlines: list[Questline] # type: ignore
    locations: list[Location] # type: ignore

    def __init__(self):
        self.relationships = {}
        self.questlines = []
        self.locations = []