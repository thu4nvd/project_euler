# The Collection of reused code for Project Euler problems
import math


# Check whether the given number interger is a prime number
def is_prime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else: 
        for i in range(3, int(x ** 0.5) + 1, 2):
            if x % i == 0:
                return False
        return True


# Sieve Eratosthenes
# For 0 <= i <= n, result[i] is True if i is a prime number, False otherwise
def sieve(n):
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(n ** 0.5) + 1):
        if result[i]:
            for j in range(i * i, len(result), i):
                result[j] = False
    return result