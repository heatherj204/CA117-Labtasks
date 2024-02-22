#!/usr/bin/env python3

import sys

n = sys.stdin.read()
n = int(n.replace("0", ""))

while n > 9:
    n = str(n).replace("0", "")
    new_n = 1
    for i in n:
        new_n *= int(i)
    n = new_n
print(n)
