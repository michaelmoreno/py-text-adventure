from engine.frontend.terminal.terminal import TerminalFrontend
from engine.frontend.io_handler import IOHandler
from engine.frontend.commands.states.grab import GrabFactory
from engine.frontend.commands.states.talk import TalkFactory
from engine.frontend.commands.factory import CommandFactory
from game.entities.agents.agent import Agent
from common.inventory import Inventory
from game.locations.location import Location
from world.world_state import WorldState
from common.dialogue import DialogueNode, DialogueOption

if __name__ == '__main__':

    lermwick_prison_cell = Location(
        "Lermwick Prison",
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
    world_state = WorldState()
    world_state.player = player # type: ignore
    factories: list[CommandFactory] = [
        GrabFactory('grab', player), TalkFactory('talk',world_state)] # type: ignore

    io_handler = IOHandler(
        TerminalFrontend(),
        factories
    )
    while True:
        io_handler.handle()