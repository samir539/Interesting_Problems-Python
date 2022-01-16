from enum import IntEnum
from typing import List, NamedTuple, Tuple
import random
from math import sqrt

#We have a maze of cells, empty cell is " ", occupied cell is "X"
#let the types of elements on the maze be with an enum

class Cell(str, Enum):
    empty = " "
    blocked = "X"
    start = "S"
    goal = "G"
    path = "*"      #indicator of path we want to take
    
class Mazeloc(NamedTuple):
    row:int
    column:int
    
    