#!/usr/bin/env python3

'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?
https://projecteuler.net/problem=16
'''


def solve(input_data):
    '''return the sum of digits of 2**input_data 

    :rtype: int
    '''
    result = sum([int(i) for i in str(2**input_data)])
    return result


def main():
    print(solve(1000))


if __name__ == "__main__":
    main()
