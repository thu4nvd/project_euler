#!/usr/bin/env python3

'''
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

https://projecteuler.net/problem=9
'''


def solve(N):
    #result = []
    for c in range(N//3, N):
        for a in range(1, (N - c)//2):
            #for a in range(1, b):
            b = N - a - c
            if a**2 + b**2 == c**2:
                #result.append((a, b, c))
                return a*b*c
    #return result


def main():
    print(solve(1000))


if __name__ == "__main__":
    main()
