from typing import TypeVar, Generic, List
T = TypeVar('T')

class stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    
    def push(self, item:T) -> None:
        self._container.append(item)
    
    def pop(self) -> T:
        return self._container.pop()
    
    def __repr__(self) -> str:
        return repr(self._container)
    
#Each tower may be represented by a stack 
disc_no:int = 5
tower_1:stack[int] = stack()
tower_2:stack[int] = stack()
tower_3:stack[int] = stack()

#Adding intial disks to tower 1
for i in range(1, disc_no+1):
    tower_1.push(i)

def hanoi_solve(start:stack[int], end:stack[int], inter:stack[int], no_of_discs:int) -> None:
    #base case
    if no_of_discs == 1:
        end.push(start.pop())
    else:
        #recursion
        hanoi_solve(start, inter, end, no_of_discs-1)
        hanoi_solve(start, end, inter, 1)
        hanoi_solve(inter, end, start, no_of_discs-1)
        

if __name__ == "__main__":
    print("TOWERS BEFORE")
    print(tower_1)
    print(tower_2)
    print(tower_3)
    hanoi_solve(tower_1, tower_3, tower_2, disc_no)
    print("TOWERS AFTER")
    print(tower_1)
    print(tower_2)
    print(tower_3)
        
    
    