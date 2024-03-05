#!/usr/bin/env python3

def get_divisors(n):
    divider = []
    for number in range(1, n+1):
        if n % number == 0:
            divider.append(number)
    return divider

def get_proper_divisors(n):
    dividers = get_divisors(n)
    return dividers[0:-1]

def is_perfect(n):
    proper_div = get_proper_divisors(n)
    if sum(proper_div) == n:
        return True
    return False