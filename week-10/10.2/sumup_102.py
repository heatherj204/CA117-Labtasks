#!/usr/bin/env python3

def sumup(n):
    if n == 0:
        return 0
    return n + sumup(n-1)

#test data
# from sumup_102 import sumup

# def main():
#     print(sumup(0))
#     print(sumup(1))
#     print(sumup(12))

# if __name__ == '__main__':
#     main()