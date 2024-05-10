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

class Rectangle:

    def __init__(self, upper_left, lower_right):
        self.upper_left = upper_left
        self.lower_right = lower_right

    def __repr__(self):
        return f"Rectangle({self.upper_left},{self.lower_right})"
    
    def area(self):
        width = self.lower_right.x - self.upper_left.x
        height = self.upper_left.y - self.lower_right.y
        return abs(width * height)
    
    def perimeter(self):
        width = self.lower_right.x - self.upper_left.x
        height = self.upper_left.y - self.lower_right.y
        return abs(2 * (width + height))

    def translate(self, dx, dy):
        upper_left = Point(self.upper_left.x + dx, self.upper_left.y + dy)
        lower_right = Point(self.lower_right.x + dx, self.lower_right.y + dy)
        return Rectangle(upper_left, lower_right)
