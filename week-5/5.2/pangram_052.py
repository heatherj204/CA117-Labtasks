#!/usr/bin/env python3
import sys
alpha = 'abcdefghijklmnopqrstuvwxyz'
for line in sys.stdin:
    missing = ''
    line = line.strip()
    line = line.lower()
    for c in alpha :
        if c not in line:
            missing = missing + c
    print(f'missing {missing}' if missing else 'pangram')
