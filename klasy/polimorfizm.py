class Shape:
    def __init__(self, name='ksztalt'):
        self.name = name

    def area(self):
        print(f'Brak danych na temat {self.name}')


class Triangle(Shape):
    def __init__(self, name='trojkat', a=2, h=2):
        self.name = name
        super(Triangle, self).__init__(name)
        self.a = a
        self.h = h

    def area(self):
        print(f'Pole figury {self.name}')
        print(self.a*self.h/2)


class Square(Shape):
    def __init__(self, name='kwadrat', a=2):
        self.name = name
        super(Square, self).__init__(name)
        self.a = a


    def area(self):
        print(f'Pole figury {self.name}')
        print(self.a**2)

class Rectangle():
    def __init__(self, name='prostokat', a=2, b=2):
        self.name = name
        self.a = a
        self.b = b

    def area(self):
        print(f'Pole figury {self.name}')
        print(self.a*self.b)


s = Shape()
t = Triangle()
sq = Square()
r = Rectangle()


def show_area(array):
    for i in array:
        print(type(i))
        i.area()

show_area([s, t, sq, r])