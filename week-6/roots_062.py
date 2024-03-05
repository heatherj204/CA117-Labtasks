#!/usr/bin/env python3

import sys

def findroots(a, b, c):
    import math
    try:
        root_one = -(b + math.sqrt(b * b - 4 * a * c)) / (a * 2)
        root_two = -(b - math.sqrt(b * b - 4 * a * c)) / (a * 2)
    except ValueError:
        return None
    return [root_one, root_two]

for line in sys.stdin:
    a, b, c, = [int(r) for r in line.strip().split()]
    realroot = findroots(a, b, c)

    if realroot:
        print(f"{min(realroot):.1f}, {max(realroot):.1f}")
    else:
        print(None)

