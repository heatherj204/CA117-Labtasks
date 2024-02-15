#!/usr/bin/env python3

def celsius2far(temp):
    far = (temp * 1.8) + 32
    return far

celsius = 21

print(f'That is {celsius2far(celsius):.1f} degrees fahrenheit')#
