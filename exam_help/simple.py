#!/usr/bin/env python3

import sys

#words = [s.strip() for s in sys.stdin]
words = ['string',
        'letter',
        'aaaaaa',
        'assassins'
        ]

for word in words:
    letters = set(word)
#    print(letters)
    simple = len(letters)
#    print(simple)
    counts = sorted([(word.count(c), c) for c in letters])
#    print(counts)
    deletions = 0
    while simple > 2:
        (n, c) = counts.pop(0)
        deletions += n
        simple -= 1
    print(deletions)