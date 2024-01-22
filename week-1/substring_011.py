#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split()
    if line[0].lower() in line[1].lower():
        print("True")
    else:
        print("False")
