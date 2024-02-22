#!/usr/bin/env python3

import sys

def a(pos):
    '''what to do if the move is a'''
    if pos == 1:
        return 2
    elif pos == 2:
        return 1
    return pos

def b(pos):
    '''what to do if the move is b'''
    if pos == 2:
        return 3
    elif pos == 3:
        return 2
    return pos

def c(pos):
    '''what to do if the move is c'''
    if pos == 1:
        return 3
    elif pos == 3:
        return 1
    return pos

placement = int(sys.stdin.readline())
move = sys.stdin.readline().strip()


for p in move:
    if p == 'A':
        placement = a(placement)
    elif p == 'B':
        placement = b(placement)
    elif p == 'C':
        placement = c(placement)

print(placement)
