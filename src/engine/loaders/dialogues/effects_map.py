from typing import Any, Callable
from world.world_state import WorldState

class EffectsMap:
    fn_lookup: dict[str, Callable[[WorldState, Any], None]]

    def __init__(self):
        self.fn_lookup = { # type: ignore
            'GiveItemByName': self.give_item_by_name,
            'IncrementTrait': self.increment_trait # type: ignore
        }

    def __getitem__(self, key: str) -> Callable[[WorldState, Any], None]:
        try:
            return self.fn_lookup[key]
        except KeyError:
            raise KeyError(f"No function implemented for '{key}'")
        
    def give_item_by_name(self, world: WorldState, name: str) -> None:
        ...

    def increment_trait(self, world: WorldState, trait: str, value: int) -> None:
        world.player.traits[trait.lower()] += value
