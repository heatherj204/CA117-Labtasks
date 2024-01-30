#!/usr/bin/env python3

import sys

file = sys.argv[1]

marks = []
students = []
try:
    with open(file, 'r') as f:
        for line in f:
            try:
                line = line.strip()
                line = line.split()
                mark = int(line[0])
                student = ' '.join(line[1:])
                marks.append(mark)
                students.append(student)
            except ValueError:
                print(f'Invalid mark {line[0]:s} encountered. Skipping.')
except FileNotFoundError:
        print(f'The file {file:s} could not be opened')

highest = 0
person = 0
counter = 0
beststu = ''
for result in marks:
    if result > highest:
        highest = result
        person = counter
    counter = counter + 1
ncount = 0
for result in marks:
    if result == highest:
        beststu += students[ncount] + ', '
    ncount += 1
beststu = beststu[0:len(beststu) - 2]
print(f'Best student(s): {beststu}')
print(f'Best mark: {marks[person]}')