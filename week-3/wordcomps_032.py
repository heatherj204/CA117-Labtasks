#!/usr/bin/env python3

import sys

words = [word.strip() for word in sys.stdin]

shortvowel = [i for i in words if 'a' in i.lower() and 'e' in i.lower() and 'i' in i.lower() and 'o' in i.lower() and 'u' in i.lower()]
print(f'Shortest word containing all vowels: {shortvowel}')
endiary = [i for i in words if i.endswith('iary')]
print(f'Words ending in iary: {len(endiary)}')

