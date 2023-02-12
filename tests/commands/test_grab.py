from engine.frontend.commands.grab import GrabFactory, GrabCommand
from game.entities.entity import Entity
from game.items.item import Item, Rarity
from common.inventory import Inventory
from game.locations.location import Location
from engine.frontend.io_handler import IOHandler
from engine.frontend.terminal.terminal import TerminalFrontend

def test_success():
    item = Item("battleaxe", 100, 50, Rarity.COMMON, 'desc')
    location = Location('test', 'test', [item], [], [])
    player = Entity(
        1,
        'Player',
        'Desc',
        Inventory(),
        100,
        {'acrobatics': 10, 'charisma': 10, 'dexterity': 10, 'intelligence': 20},
        location,
        None # type: ignore
    )
    io = IOHandler(TerminalFrontend(), GrabFactory(['grab'], player)) # type: ignore
    
    grab_command = GrabCommand(io, player)
    grab_command.handle('grab axe')
    assert item in player.inventory.items
    assert item not in location.items
