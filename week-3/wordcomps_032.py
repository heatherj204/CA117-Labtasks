#!/usr/bin/env python3

import sys

words = [word.strip() for word in sys.stdin]

shortvowel = [i for i in words if 'a' in i.lower() and 'e' in i.lower() and 'i' in i.lower() and 'o' in i.lower() and 'u' in i.lower()]
print(f'Shortest word containing all vowels: {min(shortvowel, key=len)}')
endiary = [i for i in words if i.lower().endswith('iary')]
print(f'Words ending in iary: {len(endiary)}')
eword = max([w.count("e") for w in words])
moste = [w for w in words if w.count("e") == eword]
print(f"Words with most e's: {moste}")
