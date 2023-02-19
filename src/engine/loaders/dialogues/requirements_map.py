from typing import Any, Callable
from world.world_state import WorldState

class RequirementsMap:
    fn_lookup: dict[str, Callable[[WorldState, Any], bool]]
    
    def __init__(self):
        self.fn_lookup = { # type: ignore
            'HasItemByName': self.has_item_by_name,
            'TraitAtleast': self.trait_atleast # type: ignore
            }

    def __getitem__(self, key: str) -> Callable[[WorldState, Any], bool]:
        try:
            return self.fn_lookup[key]
        except KeyError:
            raise KeyError(f"No function implemented for '{key}'")

    def has_item_by_name(self, world: WorldState, name: str) -> bool:
        return world.player.inventory.has_by_name(name)

    def trait_atleast(self, world: WorldState, trait: str, value: int) -> bool:
        return world.player.traits[trait.lower()] >= value
