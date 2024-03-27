#!/usr/bin/env python3

def reverse(lst, newl=None):
    newl = [] if not newl else newl
    if len(lst) == 0:
        return newl
    newl.insert(0, lst[0])
    return reverse(lst[1:], newl)

#test data
# from reverse_102 import reverse

# def main():
#     print(reverse([1,2,3]))
#     print(reverse([3,4,5,6]))
#     print(reverse([1,2]))

# if __name__ == '__main__':
#     main()