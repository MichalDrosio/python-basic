import math

class Vector:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __divmod__(self, other):
        return Vector(self.x / other.x, self.y / other.y)

    def compute_length(self):
        return math.sqrt(self.x**2+self.y**2)

    def compute_angle(self):
        return math.degrees(math.atan2(self.x, self.y))

    def print(self):
        return f'wspolrzedna x to: {self.x}, wspolrzedna y to: {self.y}. Dlugosc wektora to {round(self.compute_length(), 2)}' \
               f' kąt wektora to {round(self.compute_angle(),2)}'

v1 = Vector(4, 7)
v2 = Vector(1, 2)
v3 = v1 + v2
v3 += v2

print(v1.print())
print(v2.print())
print(v3.print())

