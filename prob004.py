#!/usr/bin/env python3

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the lardigitsest palindrome made from the product of two 3-digit numbers.

https://projecteuler.net/problem=4
'''


def isPalindrom(number):
    return str(number) == str(number)[::-1]

def palindrom(digits):
    max_num = ((10 ** digits -1) // 11) * 11
    min_num = 10 ** (digits -1)
    max_palindrome = 0
    for a in range(max_num, min_num, -11):
        for b in range(10 ** digits -1, 10 ** (digits -1), -1):
            if isPalindrom(a * b) and a * b > max_palindrome:
                max_palindrome = a * b

    return max_palindrome


def main():
    print(palindrom(4))


if __name__ == "__main__":
    main()
