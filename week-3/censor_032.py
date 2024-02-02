#!/usr/bin/env python3

import sys

file = sys.argv[1]
with open(file, 'r') as f:
    censorword = [w.strip() for w in f]

lines = sys.stdin.read()

for word in censorword:
    lines = lines.replace(word, '@'*len(word))
print(lines.strip())
