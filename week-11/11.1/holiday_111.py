#!/usr/bin/env python3

import sys

def highestTemp(nums):
  if nums[0] > nums[2]:
    return nums[0]
  else:
    return nums[2]

nums = list(map(int, sys.stdin.read().strip().split()))
htemp = max(nums)
start = 0

i = 0
while i < len(nums) - 2:
  temp = highestTemp(nums[i:i + 3])
  if temp < htemp:
    htemp = temp
    start = i
  i += 1

print(f'{start + 1} {htemp}')