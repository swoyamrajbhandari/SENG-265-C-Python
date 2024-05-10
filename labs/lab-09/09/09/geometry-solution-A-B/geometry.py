import math


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%r, %r)" % (self.x, self.y)

    def delta_x(self, d):
        return Point(self.x + d, self.y)

    def delta_y(self, d):
        return Point(self.x, self.y + d)

    def translate(self, d_x, d_y):
        return Point(self.x + d_x, self.y + d_y)

