#!/usr/bin/env python3

def overlap(x1 = 0, y1 = 0, r1 = 1, x2 = 0, y2 = 0, r2 = 1):
    import math
    d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    if(d <= r1 - r2):
        return True
    elif(d <= r2 - r1):
        return True
    elif(d < r1 + r2):
        return True
    elif(d == r1 + r2):
        return False
    return False