import math

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, p2):
        length = math.sqrt((self.x - p2.x)**2 + (self.y - p2.y) **2)
        return length

    def __str__(self):
        return f"({self.x:.1f}, {self.y:.1f})"
