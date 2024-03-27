#!/usr/bin/env python3

def biggest(lst):
    if len(lst) == 1:
        return lst[0]

    if lst[0] > lst[-1]:
        return biggest(lst[:-1])
    else:
        return biggest(lst[1:])

#test data
# from biggest_102 import biggest

# def main():
#     min = None
#     print(biggest([6,5,1,3,4]))
#     print(biggest([6,5,11,3,4]))
#     print(biggest([6,15,11,13,14]))
#     print(biggest([6,15,11,13,4]))

# if __name__ == '__main__':
#     main()