#!/usr/bin/env python3

'''
Highly divisible triangular number
Problem 12

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

https://projecteuler.net/problem=12
'''
#Su dung sang erathostens

def solve(N):
    # tao sang erathostens kich co N
    sieve = [1 for i in range(N)]
    sieve[0], sieve[1] = 0, 0
    for i in range(2, N):
        if sieve[i]:
            for j in range(2 * i, N, i):
                sieve[j] = 0

    n = 1
    tri_n_mark = 1
    while True:
        #tinh so triangle thu n
        n += 1
        tri_n_mark += n
        tri_n = tri_n_mark
        factor = [0 for i in range(N)]
        # Tim bieu dien prime factor cua so tri_n
        num_divisors = 1
        for i in range(2, N):
            if sieve[i] == 0: 
                continue
            while tri_n % i == 0:
                factor[i] += 1
                tri_n = tri_n // i
            num_divisors = num_divisors * (factor[i] + 1)
            if tri_n == 1:
                break
        if num_divisors > N:
            return tri_n_mark


def main():
    print(solve(500))


if __name__ == "__main__":
    main()
