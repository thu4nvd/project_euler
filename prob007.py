#!/usr/bin/env python3

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
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


def solve(n):
    '''return the 10001st prime number 

    :rtype: (int index, int 10001st_prime_number)
    '''
    test_prime = 2
    index = 1

    while index < n:
        test_prime += 1
        if is_prime(test_prime):
            index += 1

    return (index, test_prime)


def main():
    print(solve(10001))


if __name__ == "__main__":
    main()
