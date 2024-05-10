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
    
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.center}, {self.radius})"

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def translate(self, dx, dy):
        new_center = Point(self.center.x + dx, self.center.y + dy)
        return Circle(new_center, self.radius)