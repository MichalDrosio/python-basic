# Define a class named Shape and its subclass Square.
# The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, value):
        super(Shape, self).__init__()
        self.value = value

    def area(self):
        return self.value * self.value


square = Square(5)
print(square.area())

