#!/usr/bin/env python3

import sys

for pas in sys.stdin:
    total = 0
    d = 0
    u = 0
    l = 0
    sc = 0
    for c in pas.strip():
        if c.isupper():
            u = u + 1
        elif c.islower():
            l = l + 1
        elif c.isdigit():
            d = d + 1
        else:
            sc = sc + 1
    if d > 0:
        total = total + 1
    if u > 0:
        total = total + 1
    if l > 0:
        total = total + 1
    if sc > 0:
        total = total + 1
    print(total)
    