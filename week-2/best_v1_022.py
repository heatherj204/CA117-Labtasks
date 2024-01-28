#!/usr/bin/env python3

import sys

file = sys.argv[1]

marks = []
students = []
try:
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split()
            mark = line[0]
            student = ' '.join(line[1:])
            marks.append(mark)
            students.append(student)
except FileNotFoundError:
        print(f'The file {file:s} could not be opened')
highest = 0
person = 0
counter = 0
for result in marks:
    if result > highest:
        highest = result
        person = counter
    counter = counter + 1
    print(f'Best student: {students[person]}')
    print(f'Best mark: {marks[person]}')
