#!/usr/bin/env python3
import sys

s = sys.stdin.read().split('\n')
highest = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for word in s:
  prev = ''
  count = 0
  for char in word:
    if char == prev and char in vowels:
      count += 1
      prev = ''
    else:
      prev = char
  if count > highest:
    highest = count
    hWord = word

print(hWord)