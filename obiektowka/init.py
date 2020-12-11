class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        if isinstance(price, (int, float)) and price > 0:
            self.price = price
        else:
            raise TypeError('The price attribute must be a positive int or float')

    def display_instance_attrs(self):
        print(f'{self.brand}-{self.model}-{self.price}')

    def show_instance_attrs(self):
        for attr in self.__dict__:
            print(attr)

    def display_attrs_with_values(self):
        for attr, values in self.__dict__.items():
            print(f'{attr}-{values}')

    def display_keys_with_values(self):
        for keys in self.__dict__.keys():
            print(f'{keys}->{getattr(self, keys)}')

try:
    laptop = Laptop('Acer', 'Predator', 5490)
except TypeError as error:
    print(error)
laptop2 = Laptop('Acer', 'Predator', 5490)
print(laptop2.__dict__)
print('-'*100)
laptop2.display_instance_attrs()
print('-'*100)
laptop2.show_instance_attrs()
print('-'*100)
laptop2.display_attrs_with_values()
print('-'*100)
laptop2.display_keys_with_values()
print('**'*100)


class Vector:
    def __init__(self, *args):
        self.args = args

    def show_points(self):
        for key in self.__dict__.keys():
            print(f'v->{getattr(self, key)}')


v1 = Vector(1, 2)
v2 = Vector(3, 4, 5)
v1.show_points()
v2.show_points()
print(v1.args)
print('***'*100)


class Bucket:
    def __init__(self, **kwargs):
        for attr_name, attr_value in kwargs.items():
            setattr(self, attr_name, attr_value)


bucket = Bucket(apple=2, milk=4, water=1, juice=2)

print(bucket.__dict__)

print('**'*100)

class Car:
    def __init__(self, brand, model, price, type_of_car=None):
        self.brand = brand
        self.model = model
        self.price = price
        self.type_of_car = type_of_car if type_of_car else 'sedan'


car = Car(model='Gu;ia', brand='Alfa Romeo', price=200000)
print(car.__dict__)
car_2 = Car(brand='BMW', model='X3', price=300000, type_of_car='SUV')
print(car_2.__dict__)