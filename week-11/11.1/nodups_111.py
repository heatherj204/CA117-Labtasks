#!/usr/bin/env python3

import sys
import string

ocr = []
output = ''


for line in sys.stdin:
    for word in  line.split():
        word_only = word.lower().strip(string.punctuation)
        if word_only not in ocr:
            ocr.append(word_only)
            output += word + ' '
        else:
            output += '. '
    output = output.rstrip() + '\n'
print(output.strip())


