#!/usr/bin/env python3

import sys

xs = []
ys = []
for line in sys.stdin:
    x, y = [int(n) for n in line.split()]
    xs.append(x)
    ys.append(y)

for x in xs:
    if xs.count(x) != 2:
        missing_x = x
for y in ys:
    if ys.count(y) != 2:
        missing_y = y
print(missing_x, missing_y)