from engine.frontend.terminal.terminal import TerminalFrontend
from engine.frontend.io_handler import IOHandler
from engine.frontend.commands.grab import GrabFactory
from engine.frontend.commands.talk import TalkFactory
from engine.frontend.commands.look import LookFactory
from engine.frontend.commands.drop import DropFactory
from engine.frontend.commands.inspect import InspectFactory
from engine.frontend.commands.command import CommandFactory
from game.entities.agents.agent import Agent
from common.inventory import Inventory
from game.locations.location import Location
from game.items.item import Item, Rarity
from world.world_state import WorldState
from common.dialogue import DialogueNode, DialogueOption
from typing import Any



if __name__ == '__main__':
    lermwick_prison_cell = Location(
        "Lermwick Prison",
        "A dank, dark cell. You can see a small window to the north, and a door to the south.",
        [],
        [],
        []
    )
    WorldState.x = 1 # type: ignore

    dialogue = DialogueNode("Who are you?",
        [
            DialogueOption("I'm a prisoner.",
                DialogueNode("What did you do?",[]),
                [lambda world: world.x == 1],
                [lambda world: setattr(world, "x", 2)]),
            DialogueOption("I'm a guard.",
                DialogueNode("What are you doing here?",[]),
                [lambda world: world.x == 2],
                [lambda world: setattr(world, "x", 3)]),
        ])

    dax = Agent(
        2,
        "Dax",
        Inventory(),
        100, 
        {'acrobatics': 10, 'charisma': 10, 'dexterity': 10, 'intelligence': 20},
        lermwick_prison_cell,
        dialogue
    )

    player = Agent(
        1,
        'Sidriel',
        Inventory(),
        100,
        {'acrobatics': 10, 'charisma': 10, 'dexterity': 10, 'intelligence': 20},
        lermwick_prison_cell,
        None
    )
    lermwick_prison_cell.entities.append(player)
    lermwick_prison_cell.entities.append(dax)
    lermwick_prison_cell.items.append(Item("Dax's battleaxe", 100, 50, Rarity.COMMON, 'An embelished battleaxe crafted by Dax.'))
    world_state = WorldState()
    world_state.player = player # type: ignore
    factories: list[Any] = [
        GrabFactory(['grab'], player),
        TalkFactory(['talk'], world_state),
        LookFactory(['look'], player),
        InspectFactory(['inspect'], player),
        DropFactory(['drop'], player)]
    
    io_handler = IOHandler(
        TerminalFrontend(),
        factories
    )
    while True:
        io_handler.update()