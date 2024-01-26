#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.split()
    word = line[1].lower()
    if len(line[0]) == len(word):
        anag = True
        for c in line[0]:
            if anag:
                c = c.lower()
                anag = c in word
                word = word.replace(c, "", 1)
    else:
        anag = False
    print(anag)

