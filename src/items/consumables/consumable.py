from items.item import Item
from items.consumables.effects.effect import Effect

class Consumable(Item):
    effects: list[Effect]

    def __init__(self, effects: list[Effect]):
        self.effects = effects
