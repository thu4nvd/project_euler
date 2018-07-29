#!/usr/bin/env python3

'''
Number spiral diagonals
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

https://projecteuler.net/problem=28
'''

'''
Compute sum of 4 vertex of each square whose width equals i ( i is odd value)
for i in range(1, 1002, 2):

v1 = 		(i - 2) ** 2 + (i -1)
v2 = v1 + (i - 1) 
v3 = v2 + (i - 1) = v1 + 2 * (i - 1)
v4 = v3 + (i - 1) = v1 + 3 * (i - 1)

sum 	= v1 + v2 + v3 + v4
	= 4 * v1 + 6*(i - 1)
	= 4 * (i - 2) ** 2 + 10 * (i - 1)
    = 4 * i ** 2 - 6 * i + 6
'''


def solve():
    result = sum((4 * i ** 2 - 6 * i + 6) for i in range(3, 1002, 2))
    return result + 1


def main():
    print(solve())


if __name__ == "__main__":
    main()
