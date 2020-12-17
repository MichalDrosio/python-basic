class Vehicle:
    def __init__(self, brand=None, color=None, year=None, category=None,):
        self.category = category if category else 'land vehicle'
        self.brand = brand
        self.color = color
        self.year = year

    def __repr__(self):
        return f'{self.__class__.__name__}(category={self.category})'

    def display_info(self):
        print(f'{self.__class__.__name__}:{self.category}')

    def display_attrs(self):
        for attr, value in self.__dict__.items():
            print(f'{attr} -> {value}')


class LandVehicle(Vehicle):
    pass


class AirVehicle(Vehicle):
    def __init__(self, category=None):
        self.category = category if category else 'air vehicle'


class Car(Vehicle):
    def __init__(self, horsepower, *args, **kwargs):
        super(Car, self).__init__(*args, **kwargs)
        self.horsepower = horsepower

    def display_attrs(self):
        print(f'Calling from class:{self.__class__.__name__}')
        super(Car, self).display_attrs()


vehicles = [Vehicle(), LandVehicle(), AirVehicle()]

for v in vehicles:
    print(v)
    v.display_info()

tesla = Vehicle(brand='Tesla', color='red', year=2020)
print(tesla.__dict__)

car = Car(brand='Alfa', color='white', year=2020, horsepower=280)
print(car.__dict__)
car.display_attrs()


