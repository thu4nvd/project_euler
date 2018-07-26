#!/usr/bin/env python3

'''
Amicable numbers
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

https://projecteuler.net/problem=21
'''


def d(n):
    result = sum(i for i in range(1, n) if n % i == 0)
    return result

def solve(N):
    #result = sum(i + d(i) for i in range(1, N) if i == d(d(i)))
    result = 0
    for i in range(1, N):
        if i == d(d(i)) and i != d(i) and d(i) < N: 
            result += i + d(i)
            print(i, d(i))
    return result // 2

def main():
    print(solve(10000))


if __name__ == "__main__":
    main()
