#!/usr/bin/env python3

import sys

def getspeed(time, dist):
    '''this will return the speedf'''
    speed = dist // time
    return speed

speeds = []
start = sys.stdin.readline().strip().split()
otime = int(start[0])
odist = int(start[1])

for line in sys.stdin:
    line = line.strip().split()
    ntime = int(line[0])
    ndist = int(line[1])
    diftime = ntime - otime
    difdist = ndist - odist
    speeds.append(getspeed(diftime, difdist))
    otime = ntime
    odist = ndist

print(max(speeds))