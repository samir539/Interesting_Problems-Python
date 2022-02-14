from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
from typing_extensions import Protocol
from heapq import heappush, heappop

T = TypeVar('T')

def linear_contains(iterable:Iterable[T], key:T) -> bool:
    for i in iterable:
        if i == key:
            return True
    return False


P = TypeVar("P", bound="Comparable")

class Comparable(Protocol):
    def __eq__(self, other:Any) -> bool:
        ...
        
    def __lt__(self:P, other:P) -> bool:
        ...
    
    def __gt__(self: P, other:P):
        return (not self < other) or self == other
    
    def __le__(self:P, other:P) -> bool:
        return self < other or self == other
    
    def __ge__(self:P, other: P) -> bool:
        return not self < other
    

def binary_contain(sequence:Sequence[P], key: P) -> bool:
    min:int = 0
    max:int = len(sequence) -1
    while min <= max:
        center:int = (min + max )//2
        if sequence[center] < key:
            min = center + 1
        elif sequence[center] > key:
            max = center - 1
        else:
            return True
    return False

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.container : List[T] = []
    
    @property
    def empty(self) -> bool:
        return not self.container
    
    def push(self, item:T) -> None:
        self.container.append(item)
    
    def pop(self) -> T:
        return self.container.pop()

    def __repr__(self) -> str:
        return repr(self.container)
    

class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node], cost:float = 0.0, heuristic: float = 0.0) -> None:
        self.state: T = state 
        self.parent: Optional[Node] = parent
        self.cost: float = cost
        self.heuristic: float = heuristic
        
    def __lt__(self, other:Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
        
        
def dfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    frontier:Stack[Node[T]] = Stack()
    frontier.push(Node(initial, None))
    explored: set[T] = {initial}
    
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
        return None 
 
def node_to_path(node:Node[T]) -> List[T]:
    path: List[T] = [node.state]
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path


#queues
class Queue(Generic[T]):
    def __init__(self) -> None:
        self.container: Deque[T] = Deque()
    
    @property
    def empty(self) -> bool:
        return not self.container  
    
    def push(self, item:T) -> None:
        self.container.append(item)      
    
    def pop(self) -> T:
        return self.container.popleft()
    
    def __repr__(self) -> str:
        return repr(self.container)
    
    
def bfs(inital: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    frontier: Queue[Node[T]] = Queue()


if __name__ == "__main__":
    pass

