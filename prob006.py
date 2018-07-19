#!/usr/bin/env python3

'''
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

https://projecteuler.net/problem=6
'''


def solve(input_data):
    square_of_sum = sum([i for i in range(1, 101)]) ** 2
    sum_of_square = sum([i ** 2 for i in range(1, 101)])
    
    return square_of_sum - sum_of_square


def main():
    print(solve(100))


if __name__ == "__main__":
    main()
