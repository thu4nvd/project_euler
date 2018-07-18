#!/usr/bin/env python3

'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
https://projecteuler.net/problem=3
'''


def maxPrimeFactor(n):
    i = 2
    while i <= n ** 0.5 :
        if n % i == 0:
            n = n/i
        else:
            i+=1
    return int(n)


def main():
    print(maxPrimeFactor(600851475143))


if __name__ == "__main__":
    main()
