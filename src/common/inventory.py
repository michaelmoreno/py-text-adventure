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

    def remove(self, item: Item):
        self.items.remove(item)
    
    def has_by_name(self, name: str) -> bool:
        return name in [item.name for item in self.items]
    
    def get_by_name(self, name: str) -> Item:
        return [item for item in self.items if item.name == name][0]
