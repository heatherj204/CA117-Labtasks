#!/usr/bin/env python3

import sys

def endings(word):
    '''find the endings to give the correct plural version of the word'''
    es = ('ch', 'sh', 'x', 'z', 's', 'o')
    y_vowle = ('ay', 'ey', 'iy', 'oy', 'uy')
    if word.endswith(es):
        word = word + 'es'
        return word
    elif word.endswith('fe'):
        word = word.replace('fe', 'ves')
        return word
    elif word.endswith('f'):
        word = word.replace('f', 'ves')
        return word
    elif word.endswith('y') and word[len(word) -2:] not in y_vowle:
        word = word.replace('y', 'ies')
        return word
    else:
        word = word + 's'
        return word

for line in sys.stdin:
    print(endings(line.strip()))
