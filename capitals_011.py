#!/usr/bin/env python3

import sys

for line in sys.stdin:
    #get the first word
    line = line.strip()
    #get letter of the word up to the send last letter
    word = line[:len(line) - 1]
    #capitilise the first letter
    word = word.capitalize()
    #get last letter of orginal word
    new_word = line[-1]
    #capitilise the last letter
    new_word = new_word.capitalize()
    #join the first letters and the last letter together
    final = word + new_word
    print(final)