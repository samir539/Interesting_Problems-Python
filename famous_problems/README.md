# Some Famous Problems Solved using Python

## Fibonacci Sequence
A mathematical sequence where each number is the sequence is the sum of the two preceeding numbers (except for the first and second terms which are set to 0 and 1 respectively )

**The sequence goes:** 0, 1, 2, 3, 5, 8, 13, 21 ... 

As a formula
> fib(n) = fib(n-1) + fib(n-2)

The programs found in the 'Fibonacci Sequence' folder solve the problem in the following ways:

- a rudimentary (but flawed) recursive attempt
- a recursive attempt improved with a base case
- exploiting memoisation and automemoisation
- using an iterative approach
- Using a python generator 



## Basic Data Compression
Commonly data storage types use more memory (bits) than needed for the contents they store. If we have the case where the number of different values the type represents is less than the number of values the bits can represent we can implement a data compression scheme if needed.

An example of this is that one needs only 2 bits to represent the four possible DNA bases _(adenine (A), cytosine (C), guanine (G) and thymine (T))_. These can be stored as 00, 01, 10, 11 in binary. 
**In python however storing "A" as a string requires 8 bits of storage and as such, using a clever compression scheme we could reduce the storage required by 75%.** _(8 bits to just 2)_.


## One Time Pad Encryption
A one time pad is a encyrption scheme which _"cannot be cracked"_ which implements the use of a key which is pre-shared. We combine the orginial text with random dummy data using an XOR bitwise operation. **The dummy data itself then serves as one key and the product of the original text and dummy data serves as the other key.**

The only way to recover the data is combine the dummmy data and product data again using the XOR bitwise operation.

As a result the **requirements of the dummy data are:**
- The dummy data must of the same length as the original data
- The dummy data must be completely random (or at least pseudo random)
- The dummy data must be completely secret


## Calculating $\Pi$
This basic script implements the Leibniz' formula which states that:

<img src="https://latex.codecogs.com/svg.image?\pi&space;=&space;\frac{4}{1}&space;-&space;\frac{4}{3}&space;&plus;&space;\frac{4}{5}&space;-&space;\frac{4}{7}&space;&plus;&space;\frac{4}{9}&space;-&space;\frac{4}{11}&space;&plus;&space;..." title="\pi = \frac{4}{1} - \frac{4}{3} + \frac{4}{5} - \frac{4}{7} + \frac{4}{9} - \frac{4}{11} + ..." />

The more terms in the series which are calculated the more accurate the result.
