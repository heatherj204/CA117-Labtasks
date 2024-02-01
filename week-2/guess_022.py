#!/usr/bin/env python3
#this is not mine (poopy heads code <3)
import sys

lines = sys.stdin.read().split()

def is_fair(lines):
    i = 1
    while i < len(lines) - 1:
        prev_no = int(lines[i-1].strip())
        guess = lines[i].strip()
        next_no = int(lines[i + 1].strip())
        correct = None
        if guess == "higher":
            correct = prev_no < next_no
        elif guess == "lower":
            correct = prev_no > next_no
        # print(prev_no, guess, next_no, correct)
        if not correct:
            return False
        i += 2

    return True

fair = is_fair(lines)

if fair:
    print("Bert can be trusted")
else:
    print("Bert is not to be trusted")
