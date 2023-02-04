from __future__ import annotations
from typing import Optional
from abc import ABC
from enum import Enum

class Rarity(Enum):
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    ARCANE = 4


class Item(ABC):
    name: str
    worth: float
    rarity: Rarity
    description: str

    def __init__(self, name: str, worth: float, rarity: Rarity, description: str):
        self.name = name
        self.worth = worth
        self.rarity = rarity
        self.description = description
    
    def use(self, additions: Optional[list[Item]]) -> bool:
        print('This item cannot be used.')
        return False
