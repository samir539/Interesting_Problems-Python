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
    
#Maze generating class
class Maze:
    def __init__(self, rows:int = 10, columns:int = 10, occupancy: float = 0.1, start: Mazeloc = Mazeloc(0,0), goal: Mazeloc =Mazeloc(9,9)) -> None:
        self.rows: int = rows
        self.colums: int = columns
        self.start: Mazeloc = start
        self.goal: Mazeloc = goal
        self.grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        self.random_fill(rows, columns, occupancy)
        
        
        pass  