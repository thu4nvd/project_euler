#!/usr/bin/env python3

'''
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

https://projecteuler.net/problem=10
'''


def solve(N):
    sieve = [1 for i in range(N)]
    sieve[0], sieve[1] = 0, 0
    for i in range(2, N):
        if sieve[i]:
            for j in range(i * 2, N, i):
                sieve[j] = 0
    return sum([j for j in range(2, N) if sieve[j]])


def main():
    print(solve(2000000))


if __name__ == "__main__":
    main()
