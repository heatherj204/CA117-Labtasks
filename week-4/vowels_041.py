#!/usr/bin/env python3

import sys

def tagger(item):
    return item[1]

vowle = {"a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
}

lines = sys.stdin.read().lower().strip()

for letter in lines:
    if letter in vowle:
        vowle[letter] += 1

vowle = dict(sorted(vowle.items(), key=tagger, reverse=True))
width = 0
for key, value in vowle.items():
    if width < len(str(value)):
        width = len(str(value))

for key, value in vowle.items():
    print(f'{key} : {value:{width}}')