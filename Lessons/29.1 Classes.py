# to be concluded
from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius**2


c = Circle(1)
print(c.radius)
print(c.area)
