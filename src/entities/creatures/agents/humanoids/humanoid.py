from enum import Enum
from entities.creatures.agents.agent import Agent

class Race(Enum):
    HUMAN = 0
    HYOTL = 1
    ORC = 2

class Humanoid(Agent):
    race: Race