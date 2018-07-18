#!/usr/bin/env python3

'''
Non-abundant sums
A PERFECT NUMBER is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers. #NOQA

https://projecteuler.net/problem=23


'''

from util import sumProperDivisors  # See &quot;efficient&quot; algorithm: https://www.geeksforgeeks.org/sum-factors-number/
from time import time
Start = time()

# http://mathworld.wolfram.com/AbundantNumber.html: Every number greater than 20161 can be expressed as a sum of two abundant numbers.
limit = 20161

abundantNumbers = set()
answer = 0
for i in range(1, limit + 1):
    # Check to see if the current number can be produced by the abundant numbers we have so far
    if not any(True for n in abundantNumbers if i - n in abundantNumbers):
        answer += i

    # Is this number abundant?
    if i < sumProperDivisors(i):
        abundantNumbers.add(i)

End = time()

print("\n--------------")
print(answer)
print("it took {:.3f} seconds".format(End - Start))