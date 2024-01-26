#!/usr/bin/env python3

import sys
uniquetext = []

def no_pun(words):
    '''returns the words without any puncuation'''
    nopun = ''
    for c in words:
        if c.isalnum():
            nopun = nopun + c

    return nopun

def unique(line):
    '''if the word is unique then it is added to the text list'''
    text = line.lower().split()
    for word in text:
        removepun = no_pun(word)
        if removepun not in uniquetext and len(removepun) > 0:
            uniquetext.append(removepun)

for l in sys.stdin:
    l = l.strip()
    unique(l)
print(len(uniquetext))
