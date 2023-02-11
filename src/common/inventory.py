from game.items.item import Item

class Inventory:
    items: list[Item]
    capacity: float

    @property
    def weight(self) -> float:
        return sum([item.weight for item in self.items])

    def add(self, item: Item) -> bool:
        if self.weight + item.weight > self.capacity:
            print("You're carrying too much!")
            return False
        return True

    def drop(self, item: Item):
        ...
