#!/usr/bin/env python3

import sys

def palindrome(s):
    '''checking to see if this is a palindrome'''
    s = s.lower()
    keep = []
    for c in s:
        if c.isalnum():
            keep.append(c)

    return keep == keep[:: -1]

for line in sys.stdin:
    print(palindrome(line.strip()))
