#!/usr/bin/env python3

import sys

def timetosec(t):
    mins, secs = t.split(':')
    return int(mins) * 60 + int(secs)

def tagger(item):
    return timetosec(item[1])

d = {}
for line in sys.stdin:
    line = line.strip().split()
    name = line[0]
    times = line[1:]
    try:
        timesinsecs = [timetosec(t) for t in times]
        d[name] = min(times, key=timetosec)
    except ValueError:
        continue

k, v = min(d.items(), key=tagger)
print(f'{k} : {v}')
