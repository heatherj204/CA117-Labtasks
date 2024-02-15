#!/usr/bin/env python3

import sys

line = sys.stdin.readline().strip()
order = sys.stdin.readline().strip()
letters = 'ABCDEF'

tokens = line.strip().split()
numbers = [int(t) for t in tokens]
snumbers = sorted(numbers)
#print(list(zip(letters, snumbers))) #builds a tuple from corrispoinding entries in letters and order

#dictionary comprihetion
d = {k : v for k, v in zip(letters, snumbers)}

output = [str(d[c]) for c in order]
print(' '.join(output))
