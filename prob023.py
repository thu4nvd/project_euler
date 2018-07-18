#!/usr/bin/env python3

'''
Non-abundant sums
A PERFECT NUMBER is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers. #NOQA

https://projecteuler.net/problem=23
'''

N = 28124
isAbundant = [False for i in range(N)]
isSum2Abundants = [False for i in range(N)]

def setListAbundant():
    for number in range(N):
        sum_divisors = sum([d for d in range(1, int(number / 2 + 1)) if number % d == 0])
        if sum_divisors > number :
            isAbundant[number] = True
        

def setListSumTwoAbundant():
    for number in range(N):
        for i in range(12, int(number / 2 + 1 )):
            if isAbundant[i] and isAbundant[number - i]:
                isSum2Abundants[number] = True
                break


def main():
    setListAbundant()
    setListSumTwoAbundant()

    result = sum([i for i in range(1,28124) if not isSum2Abundants[i]])
    print(result)

    
if __name__ == "__main__":
    main()