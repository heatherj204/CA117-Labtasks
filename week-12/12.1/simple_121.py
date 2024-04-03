#!/usr/bin/env python3

import sys

words = [s.strip() for s in sys.stdin]

for word in words:
    letters = set(word)
    simple = len(letters)
    counts = sorted([(word.count(c), c) for c in letters])
    deletions = 0
    while simple > 2:
        (n, c) = counts.pop(0)
        deletions += n
        simple -= 1
    print(deletions)