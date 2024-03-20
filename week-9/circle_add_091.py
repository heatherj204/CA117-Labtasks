#!/usr/bin/env python3

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def midpoint(self, p2):
        midX = (self.x + p2.x) / 2
        midY = (self.y + p2.y) / 2
        return Point(midX, midY)

    def __str__(self):
        return f"({self.x:.1f}, {self.y:.1f})"

class Circle(object):
    def __init__(self, centre:Point=None, radius:float=1):
        self.radius = radius

        if centre:
            self.centre = centre
        else:
            self.centre = Point(0,0)

    def __str__(self):
        return f"Centre: {self.centre}\nRadius: {self.radius}"

    def __add__(self, other):
        centre = self.centre.midpoint(other.centre)
        radius = self.radius + other.radius
        return Circle(centre, radius)

#test data
# def main():
#     p1 = Point()
#     p2 = Point(4, 6)

#     c1 = Circle(p1, 10)
#     c2 = Circle(p2, 5)

#     c3 = c1 + c2
#     assert(isinstance(c3, Circle))
#     print(c3)

# if __name__ == '__main__':
#     main()
