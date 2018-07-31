#!/usr/bin/env python3

'''
Digit fifth powers
Problem 30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

https://projecteuler.net/problem=31
'''


def solve():
    # As stated in the problem, 1 = 1^5 is excluded.
	# If a number has at least n >= 7 digits, then even if every digit is 9,
	# n * 9^5 is still less than the number (which is at least 10^n).

    result = sum(i for i in range(2, 1000000) if i == fifth_power_digit_sum(i))
    return str(result)


def fifth_power_digit_sum(n):
    return sum(int(c) ** 5 for c in str(n))


def main():
    print(solve())


if __name__ == "__main__":
    main()
