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


