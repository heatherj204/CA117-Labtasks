#!/usr/bin/env python3

import sys
low = [n.strip() for n in sys.stdin]
def qnou(w):
    w = w.lower().replace('qu', '--')
    return 'q' in w

qnous = [w for w in low if qnou(w)]
print(f'Words with q but no u: {qnous}')