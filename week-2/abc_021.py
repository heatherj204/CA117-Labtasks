#!/usr/bin/env python3

import sys

order_map = {"A": 0, "B": 1, "C": 2}

nums, order = sys.stdin.readlines()

numlist = []

for num in nums.split():
    numlist.append(int(num))

numlist.sort()

output = []
for i in range(3):
    index = order_map[order[i]]
    output.append(str(numlist[index]))

print(" ".join(output))
