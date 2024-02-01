#!/usr/bin/env python3


import sys

def mulit(n):
    if n % 3:
        return 0
    else:
        return n

nums = [int(n.strip()) for n in sys.stdin]
for num in nums:
    allnum = [mulit(i) for i in range(1, num + 1)]
    print(f'Non-multiples of 3 replaced: {allnum}')