#!/usr/bin/env python3

import sys
from math import pi

for num in sys.stdin:
    num = num.strip()
    num = int(num)
    print(f'{pi:.{num}f}')
