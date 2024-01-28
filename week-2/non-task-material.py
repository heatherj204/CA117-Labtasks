#!/usr/env/python3

import sys

order_map = {"A": 0, "B": 1, "C": 2}

nums, order = sys.stdin.readlines()

num_list = []

for num in nums.split():
    num_list.append(int(num))

num_list.sort()

output = []
for i in range(3):
    index = order_map[order[i]]
    output.append(str(num_list[index]))

print(" ".join(output))


#!/usr/bin/env python3

import sys

order_map = {"A": 0, "B": 1, "C": 2}
num = sys.stdin.readline().rstrip()
order = sys.stdin.readline()

numlist = []
for nums in num.split(): #this is to be plit first becuse they are all uin one lline otherwise it wouold not take thr proper numbers and i thibnk i would have tgo add in a while loop (im not sure tho, all i nkow is uit just would not wrok)
    numlist.append(int(num))

numlist.sort()

output = []
for i in range(3):
    index = order_map[order[i]]
    output.append(str(numlist[index]))

print(" ".join(output))
