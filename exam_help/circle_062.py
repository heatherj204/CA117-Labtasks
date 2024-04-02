def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    import math
    d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    if(d <= r1 - r2):
        return True
    elif(d <= r2 - r1):
        return True
    elif(d < r1 + r2):
        return True
    elif(d == r1 + r2):
        return False
    return False


#test data
#!/usr/bin/env python3
from circle_062 import overlap
def main():
    print(overlap())
    print(overlap(10))
    print(overlap(10,10))
    print(overlap(10,10,10))
    print(overlap(10,0,10))
    print(overlap(10,0,1,8,0,1))
    print(overlap(10,0,1,8,0,2))


if __name__ == '__main__':
    main()