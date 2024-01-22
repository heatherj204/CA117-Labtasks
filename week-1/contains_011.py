#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.split()
    word = line[1].lower()

    contains = True
    for c in line[0]:
        if contains:
            c = c.lower()
            contains = c in word
            word = word.replace(c, "", 1)
    print(contains)


