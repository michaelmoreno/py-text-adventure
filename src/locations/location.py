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

    def has_item(self, name: str) -> bool:
        return any([item.name == name for item in self.items])
    
    def has_entity(self, name: str) -> bool:
        return any([entity.name == name for entity in self.entities])