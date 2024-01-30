#!/usr/bin/env python3

import sys

file = sys.argv[1]
def mainfun(file):
    marks = []
    students = []
    try:
        with open(file, 'r') as f:
            for line in f:
                line = line.strip()
                line = line.split()
                mark = int(line[0])
                student = ' '.join(line[1:])
                marks.append(mark)
                students.append(student)
    except ValueError:
        print(f'Invalid mark {line[0]:s} encountered. Exiting.')
        return None, None
    highest = 0
    person = 0
    counter = 0
    for result in marks:
        if result > highest:
            highest = result
            person = counter
        counter = counter + 1
    return students[person], marks[person]


student, mark = mainfun(file)
if student:
    print(f'Best student: {student}')
    print(f'Best mark: {mark}')
