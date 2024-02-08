#!/usr/bin/env python3

import sys

file = sys.argv[1]
phone_book = {}

def lookup(name):
    if name in phone_book:
        return (f'Name: {name}')
    return  (f'Name: {name}')

def phone(name):
    if name in phone_book:
        return (f'Phone: {phone_book[name]}')
    return('No such contact')

with open(file, 'r') as f:
    for line in f:
        line = line.strip()
        line = line.split()
        name = line[0]
        number = line[1]
        phone_book[name] = number

for line in sys.stdin:
    person = line.strip()
    print(lookup(person))
    print(phone(person))