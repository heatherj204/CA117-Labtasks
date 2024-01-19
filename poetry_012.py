#!/usr/bin/env python3

import sys

# poen = sys.stdin.readlines()

for line in sys.stdin:
    line = line.strip()
    print(f'{line:^10}')