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
        #add in start and end
        self.grid[start.row][start.column] = Cell.start
        self.grid[goal.row][goal.column] = Cell.goal
        
    def random_fill(self, rows:int, columns:int , occupancy:float):
        for row in range(rows):
            for columns in range(columns):
                if random.uniform(0, 1.0) < occupancy:
                    self.grid[row][columns] = Cell.blocked
    
    #for printing purposes
    def __str__(self) -> str:
        output:str = ""
        for row in self.grid:
            output += "".join([c.value for c in row]) + "\n"
        return output
    
    def goal_check(self, ml: Mazeloc) -> bool:
        return ml == self.goal
    
    
    def next_loc(self, ml:Mazeloc) -> List[Mazeloc]:
        locations: List[Mazeloc] = []
        if ml.row + 1 < self.rows and self.grid[ml.row + 1][ml.column] != Cell.blocked:
            locations.append(Mazeloc(ml.row + 1, ml.column))
        if ml.row - 1 >= 0 and self.grid[ml.row -1][ml.column] != Cell.blocked:
            locations.append(Mazeloc(ml.row - 1, ml.column))
        if ml.column + 1 < self.columns and self.grid[ml.row][ml.column + 1] != Cell.blocked:
            locations.append(Mazeloc(ml.row, ml.column + 1))
        if ml.column -1 >= 0 and self.grid[ml.row][ml.column - 1 ] != Cell.blocked:
            locations.append(Mazeloc(ml.row, ml.column -1))
        return locations
        
        
