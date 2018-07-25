#!/usr/bin/env python3

'''
Longest Collatz sequence
Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

23.73s user 
0.00s system 
99% cpu 
23.734 total

https://projecteuler.net/problem=14
'''

def collatz_seq(n):
    length = 1
    while n != 1:
        if n % 2 == 0 : n = n // 2 
        else: n = 3 * n + 1
        length += 1
    return length


def solve(N):
    max_length = 1
    for i in range(2, N):
        if max_length < collatz_seq(i):
            max_length = collatz_seq(i)
            max_i = i

    return max_i


def main():
    print(solve(1000000))


if __name__ == "__main__":
    main()
