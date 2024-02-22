#!/usr/bin/env python3

import sys
refuse = 0
people = 0
cap = sys.stdin.readline().strip()
for line in sys.stdin:
    line = line.strip()
    line = line.split()
    if line[0] == 'enter':
        if people  + int(line[1]) <= int(cap):
            people += int(line[1])
        elif people  + int(line[1]) >= int(cap):
            refuse += 1
    elif line[0] == 'leave':
        people = people - int(line[1])

print(refuse)