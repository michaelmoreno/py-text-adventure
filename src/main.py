from engine.frontend.terminal.terminal import TerminalFrontend
from engine.frontend.io_handler import IOHandler
from engine.commands.factories.grab import GrabFactory
from engine.commands.factories.factory import CommandFactory
from entities.creatures.agents.humanoids.humanoid import Humanoid
from common.inventory import Inventory
from world.map import lermwick_prison_hallway

class GameState:
    # world: World
    player: Humanoid


if __name__ == '__main__':
    player = Humanoid(
        'Sidriel',
        Inventory(),
        100,
        {'acrobatics': 10, 'charisma': 10, 'dexterity': 10, 'intelligence': 20},
    )
    factories: list[CommandFactory] = [GrabFactory()]
    io_handler = IOHandler(
        TerminalFrontend(),
        factories
    )
    io_handler.capture()