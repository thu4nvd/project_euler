#!/usr/bin/env python3

'''
Non-abundant sums
A PERFECT NUMBER is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers. #NOQA

https://projecteuler.net/problem=23

real    0m5.065s
user    0m5.044s
sys     0m0.004s
'''

from math import ceil

def sum_of_divisors(stop):
    sd=[0 for i in range(stop)]
    for divisor in range(1,ceil(stop/2)):
       k=2
       while k*divisor<stop:
           sd[k*divisor]+=divisor
           k+=1
    return sd


stop=28123
sd=sum_of_divisors(stop)
sum=0
for n in range(1,stop):
    vaild=True
    i=1
    while n>i:
        if sd[i]>i and sd[n-i]>n-i:
            vaild=False
            break
        i+=1
    if vaild:sum+=n
print(sum)
