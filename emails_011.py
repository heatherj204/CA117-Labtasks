#!/usr/bin/env python3

import sys

for email in sys.stdin:
    email = email.strip()
    #get the first name only
    parts = email.split('.')
    first = parts[0].capitalize()

    #get the last name and the folowing number
    last = parts[1].split('@')
    last = last[0]

    lastn = ""
    i = 0
    while i < len(last) and "a" <= last[i] and "z" >= last[i]:
        lastn = lastn + last[i]
        i = i + 1
    lastn = lastn.capitalize()
    print(first + " " + lastn)
