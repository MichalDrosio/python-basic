from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Figure):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a * self.a

    def perimeter(self):
        return 4 * self.a

try:
    Figure()
except TypeError as error:
    print(error)

square = Square(10)
print(square.area())
print(square.perimeter())