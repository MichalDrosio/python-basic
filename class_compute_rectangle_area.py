# Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.results = []

    def compute_area(self):
        result = self.width * self.length
        self.results.append(result)

    def print_results(self):
        for r in self.results:
            print(r)


rectangle = Rectangle(2, 2)
rectangle.compute_area()
rectangle.print_results()