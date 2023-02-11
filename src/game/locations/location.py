from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.entities.entity import Entity
from game.items.item import Item


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
    
    def find_entity(self, name: str) -> Entity | None:
        for entity in self.entities:
            if entity.name == name:
                return entity
