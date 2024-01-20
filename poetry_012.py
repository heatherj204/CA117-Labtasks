#!/usr/bin/env python3

import sys


poem = []
length = 0

for line in sys.stdin:
    #add each line to the poen list
    poem.append(line.strip())
    #find the length of the longest line
    if len(line) > length:
        length = len(line)

for sen in poem:
    #center each line based on the length of the longest line
    print(f'{sen:^{length - 1}}')