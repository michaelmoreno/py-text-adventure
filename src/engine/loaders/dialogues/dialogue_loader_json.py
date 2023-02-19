from typing import Optional, Any, Callable, cast
from common.dialogue import DialogueNode, DialogueOption
from world.world_state import WorldState
import json
from engine.loaders.dialogues.requirements_map import RequirementsMap
from engine.loaders.dialogues.effects_map import EffectsMap

class DialogueLoaderJSON:
    path: str
    requirements_map: RequirementsMap
    effects_map: EffectsMap
    
    def __init__(self, path: str, requirements_map: RequirementsMap, effects_map: EffectsMap):
        self.path = path
        self.requirements_map = requirements_map
        self.effects_map = effects_map

    def package_requirement(self, requirement: tuple[str, ...]) -> Optional[Callable[[WorldState], bool]]:
        fn_label, *args  = requirement
        fn = self.requirements_map[fn_label]
        packaged = cast(
            Callable[[WorldState], bool],
            lambda world: fn(world, *args))
        return packaged
    
    def package_requirements(self, requirements: list[tuple[str, ...]]) -> list[Optional[Callable[[WorldState], bool]]]:
        return [self.package_requirement(requirement)
            for requirement in requirements]

    def package_effect(self, effect: tuple[str, ...]) -> Optional[Callable[[WorldState], None]]:
        fn_label, *args = effect
        fn = self.effects_map[fn_label]
        packaged = cast(
            Callable[[WorldState], None],
            lambda world: fn(world, *args))
        return packaged

    def package_effects(self, effects: list[tuple[str, ...]]) -> list[Optional[Callable[[WorldState], None]]]:
        return [self.package_effect(effect)
            for effect in effects]

    def _recursive_build(self, root: dict, node_id: str = "0") -> DialogueNode:
        node = root[node_id]
        return DialogueNode(
            node['text'],
            [DialogueOption(
                option['text'],
                self.package_requirements(option['requirements']),
                self.package_effects(option['effects']),
                self._recursive_build(root, option['next']))
                for option in node['options']])

    def load(self, npc_id: str) -> Optional[DialogueNode]:
        with open(self.path, 'r') as f:
            data = json.load(f)
            root = data[npc_id]
            dialogue = self._recursive_build(root)
            return dialogue
