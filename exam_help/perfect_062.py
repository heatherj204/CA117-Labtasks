def get_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return sorted(divisors)

def get_proper_divisors(n):
    dividers = get_divisors(n)
    proper_div = dividers[0:-1]
    return proper_div

def is_perfect(n):
    proper = get_proper_divisors(n)
    if sum(proper) == n:
        return True
    return False

    

#test data
#!/usr/bin/env python3

from perfect_062 import get_divisors, get_proper_divisors, is_perfect

def main():

    print(get_divisors(6))
    print(get_proper_divisors(6))
    print(is_perfect(6))

    numbers = [1, 2, 3, 4, 5, 6, 28, 496, 8128, 8129]

    for n in numbers:
        print(is_perfect(n))


if __name__ == '__main__':
    main()