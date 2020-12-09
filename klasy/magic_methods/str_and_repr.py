class Car:
    no = 0

    def __init__(self, color, model):
        self.color = color
        self.model = model
        Car.no += 1

    def __str__(self):
        return f'{self.color} {self.model}'

    def __repr__(self):
        return f'{self.__class__.__name__} ({self.color!r} {self.model!r})'

    @staticmethod
    def no_of_cars():
        print(f'{Car.no}')


Car.no_of_cars()
alfa = Car('Red', 'Alfa')
print(alfa)
Car.no_of_cars()
print(repr(alfa))
alfa2 = Car('Red', 'Alfa')
Car.no_of_cars()