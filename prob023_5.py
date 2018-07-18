#!/usr/bin/env python3

'''
Non-abundant sums
A PERFECT NUMBER is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers. #NOQA

https://projecteuler.net/problem=23

real    0m1.351s
user    0m1.336s
sys     0m0.008s
'''

import time


def time_decorator(f):
  def wrapper(*args):
    start_time = time.time()
    a = f()
    print(time.time()- start_time)
    return a
  return wrapper

abundants = []
dabundants = {}


def num_divisors(n):
  if n ** .5 == n ** .5 // 1:
    a = sum(i for i in range(1,int(n)) if n % i == 0)
  else:
     a = sum(i + n // i for i in range(2,int(n ** .5 + 1)) if n % i == 0) + 1
  return a

def check_abundants(x):
  for i in abundants:
    if i > x/2:
      return False
    elif x - i in dabundants:
      return True
  return False


@time_decorator
def main():
  count = 0
  for i in range(1,28123):
    if num_divisors(i) > i:
      abundants.append(i)
      dabundants[i] = 1
    if check_abundants(i) == 0:
      count+=i

  return count

print(main())