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
        
    

if __name__ == "__main__":
    pass

