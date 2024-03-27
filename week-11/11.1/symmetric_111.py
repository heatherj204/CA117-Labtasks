#!/usr/bin/env python3

import sys
ordered_names = ''

names = [names.strip() for names in sys.stdin.read()]
if len(names) % 2 != 0:
    longest_name = names[-1]
else:
    longest_name = names[-2:]

shortest_name = names[0:2]

for name in names:
    ordered_names += '.\n'

ordered_names = ordered_names.replace(ordered_names[0], shortest_name[0], 1)
print(ordered_names)
print(names)
print(longest_name)
print(shortest_name)