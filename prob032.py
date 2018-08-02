#!/usr/bin/env python3

'''
Pandigital products
https://projecteuler.net/problem=32
'''


def solve():
    	# For contradiction suppose a candidate (x, y, z) has z >= 10000.
	# Then x*y consumes at least 5 digits. With the 4 (or fewer) remaining digits, even the
	# upper bound of x=99 and y=99 produces a product of x*y < 10000, which is unequal to z.
	# Therefore we need the product z < 10000 to be able to find possible x and y values.
	ans = sum(i for i in range(1, 10000) if has_pandigital_product(i))
	return str(ans)


def has_pandigital_product(n):
	# Find and examine all factors of n
	for i in range(1, int(n ** 0.5) + 1):
		if n % i == 0:
			temp = str(n) + str(i) + str(n // i)
			if "".join(sorted(temp)) == "123456789":
				return True
	return False


def main():
    print(solve())


if __name__ == "__main__":
    main()
