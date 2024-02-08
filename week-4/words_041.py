#!/usr/bin/env python3

import sys
import string
data = {}

lines = sys.stdin.read().lower().split()
words = [word.strip(string.punctuation) for word in lines]

for word in words:
    if word in data:
        data[word] += 1
    else:
        data[word] = 1


for w in sorted(data):
    print(f'{w} : {data[w]}')
