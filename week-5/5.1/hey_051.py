#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    h = line[0]
    y = line[-1]
    e = line[1:-1]
    print(h + e * 2 + y)