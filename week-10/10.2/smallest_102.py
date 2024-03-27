#!/usr/bin/env python3

def smallest(lst):
    if len(lst) == 1:
        return lst[0]

    if lst[0] < lst[-1]:
        return smallest(lst[:-1])
    else:
        return smallest(lst[1:])

#test data
# from smallest_102 import smallest

# def main():
#     MnotIN = None
#     print(smallest([6,5,1,3,4]))
#     print(smallest([6,5,11,3,4]))
#     print(smallest([6,15,11,13,14]))
#     print(smallest([6,15,11,13,4]))

# if __name__ == '__main__':
#     main()