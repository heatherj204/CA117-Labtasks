#!/usr/bin/env python3

def power(n, p):
    if p == 0:
        return 1
    return n * power(n, p-1)

#test data
# from power_102 import power

# def main():
#     print(power(2,3))
#     print(power(4,4))
#     print(power(2,32))
#     print(power(10,3))
#     print(power(8,0))

# if __name__ == '__main__':
#     main()