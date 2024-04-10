#!/usr/bin/env python3

import sys

pairs = {}
inp = sys.stdin.read().split('\n')
inp.pop()
for line in inp:
  pairs[len(line)] = list()
for name in inp:
  pairs[len(name)].append(name)
for word in pairs:
  print(f'{pairs[word][0]}')
for word in reversed(pairs):
  try:
    print(f'{pairs[word][1]}')
  except IndexError:
    continue