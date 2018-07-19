#!/usr/bin/env python3

'''
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

https://projecteuler.net/problem=5
Tips: use Eratosthene
https://en.wikipedia.org/wiki/Eratosthenes#Prime_numbers
'''


def solve(n):
    sieve_eratosthenes = [1 for i in range(n + 1)]
    sieve_eratosthenes[0] = 0
    sieve_eratosthenes[1] = 0
    index = 2
    while index <= n:
        if sieve_eratosthenes[index]:
            for i in range(index * 2, n + 1, index):
                sieve_eratosthenes[i] = 0
        index += 1

    import math
    product = 1
    for i in range(2, n+1):
        if sieve_eratosthenes[i]:
            #sieve_eratosthenes[i] = int(math.log(n, i))
            product = product * i ** int(math.log(n, i))

    return product


def main():
    print(solve(200))


if __name__ == "__main__":
    main()
