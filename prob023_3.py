#!/usr/bin/env python3

'''
Non-abundant sums
A PERFECT NUMBER is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers. #NOQA

https://projecteuler.net/problem=23

real    0m9.006s
user    0m8.988s
sys     0m0.012s
'''

def GetPrimeFactors(n,primes):
    primefactors = []
    primefactorfreqs = []
    for p in primes:
        if p > n:
            break
        if n%p == 0:
            cnt = 0
            quotient = n
            while quotient%p==0:
                cnt += 1
                quotient /= p
            if cnt > 0:
                primefactors.append(p)
                primefactorfreqs.append(cnt)
    return {'PrimeFactors':primefactors, 'Freqs':primefactorfreqs}

def GetPrimesList(n):
    '''Return list of primes less than n
    '''
    primes = []
    p = 2
    while p <= n:
        flag = 0
        for pi in primes:
            if p%pi==0:
                flag = 1
                break
        if not flag:
            primes.append(p) 
        p=p+1
    return primes

def GetSumProperDivisors(n,PrimeList):
    P = GetPrimeFactors(n,PrimeList)
    tot = 1
    for prime,freq in zip(P['PrimeFactors'],P['Freqs']):
        tot *= ((prime**(freq+1))-1)/(prime -1)
    return tot - n

def GetAbundantNumbers(n_max, PrimeList):
    abundant = []
    for n in range(1,n_max):
        if GetSumProperDivisors(n,PrimeList) > n:
            abundant.append(n)
    return abundant

def SumNonAbundant(n_max, PrimeList):
    abundantList = GetAbundantNumbers(n_max, PrimeList)
    AbundantSumLookUp = {}
    for a in abundantList:
        for b in abundantList:
            if a+b > n_max:
                break
            AbundantSumLookUp[a+b] = 1
    return n_max*(n_max+1)/2 - sum(AbundantSumLookUp.keys())

#n_max = 28123
n_max = 1999
PrimeList = GetPrimesList(n_max)
#print(SumNonAbundant(n_max, PrimeList)) 
print(PrimeList)