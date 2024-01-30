#!/usr/bin/env python3

import sys

data = []

nameWidth = 0

for line in sys.stdin:
    d = line.strip().split()
    newData = [d[0]]
    namePos = d[1:-8]

    name = " ".join(namePos)
    name = name.strip()

    newData.append(name)

    i = len(namePos) + 1
    while i < len(d):
        newData.append(d[i].strip())
        i += 1

    width = len(name)
    if width > nameWidth:
        nameWidth = width

    data.append(newData)
print(f"{'POS':3} {'CLUB':{nameWidth:d}} {'P':>2} {'W':>3} {'D':>3} {'L':>3} {'GF':>3} {'GA':>3} {'GD':>3} {'PTS':3}")

for i in data:
    print(f"{i[0]:>3} {i[1]:{nameWidth:d}} {i[2]:>2} {i[3]:>3} {i[4]:>3} {i[5]:>3} {i[6]:>3} {i[7]:>3} {i[8]:>3} {i[9]:>3}")
