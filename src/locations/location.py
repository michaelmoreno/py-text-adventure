from __future__ import annotations
from items.item import Item
from entities.entity import Entity

class Location:
    items: list[Item]
    entities: list[Entity]
    entrances: list[Location]
