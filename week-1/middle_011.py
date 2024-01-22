#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    if len(line) % 2 != 0:
        l = (len(line) // 2)
        print(line[l])
    else:
        print("No middle character!")
