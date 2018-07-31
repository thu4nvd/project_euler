#!/usr/bin/env python3

'''
Coin sums
Problem 31

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

https://projecteuler.net/problem=31
'''

# At the start of each loop iteration, ways[i] is the number of ways to use {any copies
# of the all the coin values seen before this iteration} to form an unordered sum of i

def solve():
    TOTAL = 14
    ways = [1] + [0] * TOTAL
    #for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
    for coin in [1, 2, 5, 10]:
	    for i in range(len(ways) - coin):
		    ways[i + coin] += ways[i]
    return str(ways[-1])


def main():
    print(solve())


if __name__ == "__main__":
    main()
