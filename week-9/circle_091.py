class Circle(object):
    # def __init__(self, centre=Point(0,0), radius=1) -> None:
    def __init__(self, centre=None, r=1) -> None:
        self.radius = r
        self.centre = Point(0,0) if centre is None else centre
        # if centre:
        #     self.centre = centre
        # else:
        #     self.centre = None

    def __str__(self):
        lines = []
        lines.append(f"Centre: {self.centre}")
        lines.append(f"Radius: {self.radius}")
        return "\n".join(lines)

    def __add__(self, other):
        radius = self.radius + other.radius
        centre = self.centre.midpoint(other.centre)
        return Circle(centre, radius)

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def midpoint(self, other):
        midx = (self.x + other.x) / 2
        midy = (self.y + other.y) / 2
        return Point(midx, midy)

    def __str__(self):
        return '({:.1f}, {:.1f})'.format(self.x, self.y)

#test data
# def main():
#     p1 = Point(2, 3)
#     c1 = Circle(p1, 5)
#     assert(c1.centre is p1)
#     assert(c1.radius == 5)

#     c2 = Circle()
#     assert(isinstance(c2.centre, Point))
#     assert(c2.radius == 1)

#     c3 = Circle()
#     assert(c3.centre is not c2.centre)

#     print(c1)
#     print(c2)
#     print(c3)

# if __name__ == '__main__':
#     main()