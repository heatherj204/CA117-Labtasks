#!/usr/bin/env python3

import sys

num_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

d = {k: v for k, v in zip(range(20), num_words)}

translations = {2:"twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
        }
for line in sys.stdin:
    line = [int(n) for n in line.split()]

    output = []
    for n in line:
        if n >= 0 and n < 20:
            output.append(d[n])
        elif n == 100:
            output.append("one hundred")
        else:
            first = str(n)[0]
            second = str(n)[1]
            if second == "0":
                output.append(translations[int(first)])
            else:
                output.append(translations[int(first)] + "-" + d[int(second)])
    print(" ".join(output))
