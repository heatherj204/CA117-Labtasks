#!/usr/bin/env python3
#not my code got from the elliecopter

import sys

for line in sys.stdin:
    prev = []
    output = ""
    for c in line.strip():
        if not prev:
            prev.append(c)
        elif prev[-1] == c:
            prev.append(c)

        else:
            char = prev[-1]
            output += f"{prev.count(char)}{char}"
            prev.clear()
            prev.append(c)
    output += f"{prev.count(prev[-1])}{prev[-1]}"
    print(output)
