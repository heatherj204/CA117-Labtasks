#!/usr/bin/env python3

import sys
numbers = [int(i) for i in sys.stdin.readline().split()]
x = numbers[0]
y = numbers [1]
n = numbers[2]


for num in range(1, n + 1):
    if num % x  == 0 and num % y == 0:
        print('fizzbuzz')
    elif num % x == 0:
        print('fizz')
    elif num % y == 0:
        print('buzz')
    else:
        print(num)