from __future__ import annotations
from items.item import Item
from entities.entity import Entity

class Location:
    name: str
    items: list[Item]
    entities: list[Entity]
    entrances: list[Location]

    def __init__(self, name: str, items: list[Item], entities: list[Entity], entrances: list[Location]):
        self.name = name
        self.items = items
        self.entities = entities
        self.entrances = entrances

    