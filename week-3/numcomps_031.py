#!/usr/bin/env python3

import sys
nums = [int(n.strip()) for n in sys.stdin]

for num in nums:
    multi3 = [int(i) for i in range(1, num + 1) if i % 3 == 0]
    sqr3 = [int(i**2) for i in range(1, num + 1) if i % 3 == 0]
#    multi4 = [int(i) for i in range(1, num + 1) if i % 4 == 0]
    sqr4 = [int(i*2) for i in range(1, num + 1) if i % 4 == 0 ]
    multi3o4 = [int(i) for i in range(1, num + 1) if i % 3 == 0 or i % 4 == 0]
    multi3a4 = [int(i) for i in range(1, num + 1) if i % 3 == 0 and i % 4 == 0]

    print(f'Multiples of 3: {multi3}')
    print(f'Multiples of 3 squared: {sqr3}')
    print(f'Multiples of 4 doubled: {sqr4}')
    print(f'Multiples of 3 or 4: {multi3o4}')
    print(f'Multiples of 3 and 4: {multi3a4}')