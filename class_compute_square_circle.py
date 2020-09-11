
# Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.
from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return pi * self.radius ** 2


circle = Circle(2)
print(circle.compute_area())
