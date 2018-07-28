import pelib


primeListShort = [i for i in range(1000) if pelib.sieve(1000)[i]]
primeListLong = [i for i in range(1000) if pelib.sieve(2001)[i]]

nMax = 0
for b in primeListShort:
    for onePlusaPlusb in primeListLong:
            a = onePlusaPlusb - 1 - b
            if abs(a) > 1000:
                continue
            
            n = 2 # We know, by construction, that for n=0 and n=1 the number will be prime
            while pelib.is_prime(n**2+a*n+b):
                n+=1
                
            if n > nMax:
                nMax = n
                maxATimesB = a*b  

print(maxATimesB)