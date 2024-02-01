#!/usr/bin/env python3

import sys
nums = [int(n.strip()) for n in sys.stdin]
def checkprime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in nums:
    primenums = [num for num in range(2, num + 1) if checkprime(num)]
    print(f'Primes: {primenums}')

