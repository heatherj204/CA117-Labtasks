#!/usr/bin/env python3
#this is not my code (gotten from ellie)
import sys

num_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]


translations = {}
with open(sys.argv[1], "r") as f:
    for line in f:
        splitted = line.split()
        translations[splitted[0]] = splitted[1]

d = {k: v for k, v in zip(range(11), num_words)}

for line in sys.stdin:
    words = [translations[d[int(n)]] for n in line.split()]

    print(" ".join(words))
