#!/usr/bin/env python3

import sys
multi3 = []
sqr3 = []


for i in range(8):
    if i % 3 == 0 and i != 0:
        multi3.append(i)
        square3 = i*i
        sqr3.append(square3)
    if i % 3

print(f'Multiples of 3: {multi3}')
print(f'Multiples of 3 squared: {sqr3}')