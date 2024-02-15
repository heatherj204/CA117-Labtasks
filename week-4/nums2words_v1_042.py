#!/usr/bin/env python3

import sys

def lookupnum(number):
    '''looks up numbe in dict and returns the value '''
    if number in nummap:
        return nummap[number]


nummap = {'0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
}

numwordlst = []

for line in sys.stdin:
    tokens = line.strip().split()
    for num in tokens:
        numwordlst.append(lookupnum(num))
    print(' '.join(numwordlst))
    numwordlst = []