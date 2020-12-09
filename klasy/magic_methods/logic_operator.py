class Point:
    no_of_points = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.no_of_points += 1

    @staticmethod
    def show_no_of_point():
        print(f'{Point.no_of_points}')

    def __repr__(self):
        return f'x, y: {self.x}, {self.y}'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Point(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        return Point(x, y)



p1 = Point(5, 5)
Point.show_no_of_point()
p2 = Point(5, 5)
Point.show_no_of_point()
p3 = p1 + p2
print(f'__add__:{p3}')
Point.show_no_of_point()
p4 = p1 * p2
print(f'__mul__:{p4}')
Point.show_no_of_point()
p5 = p1 - p2
print(f'__sub__:{p5}')
Point.show_no_of_point()
p6 = p1 / p2
print(f'__truediv__:{p6}')
Point.show_no_of_point()