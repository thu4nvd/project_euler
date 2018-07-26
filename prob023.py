#!/usr/bin/env python3

'''
Factorial digit sum
Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

https://projecteuler.net/problem=20
'''


def solve():
    import functools
    product = functools.reduce(lambda x, y: x * y, range(1, 101))
    return sum(int(c) for c in str(product))


def main():
    print(solve())


if __name__ == "__main__":
    main()
