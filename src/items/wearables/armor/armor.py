from typing import Literal
from items.wearables.wearable import Wearable

ArmorCoverage = Literal[1,2,3,4,5,6,7,8,9,10]

class Armor(Wearable):
    defense: float
    coverage: ArmorCoverage
