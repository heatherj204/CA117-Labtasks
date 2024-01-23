#!/usr/bin/env python3

import sys
data = []
length = 0

for line in sys.stdin:
    line = line.strip()
    data = data.append(line.split())
    club = data[1]
    if len(club) > length:
        length = len(club)

for sen in data:
    #center each line based on the length of the longest line
    print(f'{sen:<{length - 1}}')
