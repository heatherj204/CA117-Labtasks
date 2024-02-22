#!/usr/bin/env python3
#this is not my code (i am too silly to be this good) #elliecode4life
import sys

for line in sys.stdin:
    nums = line.strip().split()

    unique = [n for n in nums if nums.count(n) == 1]

    print(max(unique, default="none"))