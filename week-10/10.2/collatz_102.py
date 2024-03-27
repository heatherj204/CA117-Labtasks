#!/usr/bin/env python3

def collatz(n):
    print(int(n))
    if n == 1:
        return 1
    if n % 2 == 0:
        return collatz(n /2)
    else:
        return collatz((n * 3) + 1)

#test data
from collatz_102 import collatz

def main():
    collatz(5)

if __name__ == '__main__':
    main()