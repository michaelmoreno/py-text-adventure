from game.items.item import Item

class Inventory:
    items: list[Item]
    capacity: float

    def __init__(self, items: list[Item] = [], capacity: float = 100):
        self.items = items
        self.capacity = capacity

    @property
    def weight(self) -> float:
        return sum([item.weight for item in self.items])

    def add(self, item: Item) -> bool:
        if self.weight + item.weight > self.capacity:
            return False
        self.items.append(item)
        return True

    def drop(self, item: Item):
        ...
