#!/usr/bin/env python3

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''


def squared(input_data):
    '''return the 10001st prime number 

    :rtype: (int index, int 10001st_prime_number)
    '''
    result = None
    # Uncomment dòng sau để có kết quả đúng
    result = input_data ** 2
    return result


def main():
    print(squared(5))


if __name__ == "__main__":
    main()
