from engine.frontend.terminal.terminal import TerminalFrontend
from engine.frontend.io_handler import IOHandler
from engine.frontend.commands.states.grab import GrabFactory
from engine.frontend.commands.states.talk import TalkFactory
from engine.frontend.commands.factory import CommandFactory
from game.entities.agents.agent import Agent
from common.inventory import Inventory
from game.locations.location import Location
from world.world_state import WorldState
from common.dialogue import DialogueNode

if __name__ == '__main__':

    lermwick_prison_cell = Location(
        "Lermwick Prison",
        [],
        [],
        []
    )

    dia = DialogueNode(
        ...,
        "Hello, I am Dax",
        []
    )


    player = Agent(
        1,
        'Sidriel',
        Inventory(),
        100,
        {'acrobatics': 10, 'charisma': 10, 'dexterity': 10, 'intelligence': 20},
        lermwick_prison_cell
    )
    lermwick_prison_cell.entities.append(player)
    world_state = WorldState()
    factories: list[CommandFactory] = [
        GrabFactory(), TalkFactory(world_state)] # type: ignore

    io_handler = IOHandler(
        TerminalFrontend(),
        factories
    )
    io_handler.capture()