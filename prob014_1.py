#!/usr/bin/env python3

'''
Longest Collatz sequence
Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

https://projecteuler.net/problem=14

2.88s user 
0.11s system 
99% cpu 
3.000 total
'''

def countCollatz(n, counts):
    ''' recursive solution. Each time a number's chain count is acquired, record it, 
    so that when the same number is encountered again, its chain count can be acquired directly instead of calculating all over again.
    Use python's dictionary to easily achieve this. Do not use a list and try to hash the target number,
    because the size of the list can become so gigantic that it actually takes much much more time'''
    if str(n) in counts.keys():
        return counts[str(n)]
    else:
        if n % 2:
            counts[str(n)] = 1 + countCollatz((3 * n +1), counts)
            return counts[str(n)]
        else:
            counts[str(n)] = 1 + countCollatz((n // 2), counts)
            return counts[str(n)]

LIMIT = 1000000
counts = {'1' : 1}
currentMax = 0
desiredNum = 0
n = 500001 # optimization, start from 500001, because any n smaller than this would have its chain included in 2n. And the chain of 2n is always bigger.

while (n < LIMIT):
    countCollatz(n, counts)
    if counts[str(n)] > currentMax:
        currentMax = counts[str(n)]
        desiredNum = n
    n += 2 # optimiaztion, only check odd number, as its chain is longer than even ones.


print("The starting number is {} to create max chain length {}".format(desiredNum, currentMax))

# recursive runtime = 4.2 s