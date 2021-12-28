##using lru_cache

from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:               #base case 
        return n 
    return fib4(n-1) + fib4(n-2)        #recursion  

if __name__ == "__main__":
    print(fib4(50))

#this feels terrible compared to memoisation