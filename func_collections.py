#!/usr/bin/env python3

'''
Collections of functions : is_prime, is_factorial, is_fibonacci, etc..
https://projecteuler.net/problem=7
'''


def is_prime(number):
    if number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
    return True


def main():
    print('This is collections of functions')


if __name__ == "__main__":
    main()
