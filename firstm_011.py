#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    i = 0
    find = True
    while i < len(line) and find == True:
        if line[i] == 'm':
            line = line[i].replace(line[i], 'M', 1)
            find = False
        i = i + 1
    print(line)