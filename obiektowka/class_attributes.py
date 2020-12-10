class Phone:
    brand = 'Apple'
    model = 'iPhone X'


print(Phone.brand)
print(getattr(Phone, 'brand'), getattr(Phone, 'model'))
samsung = Phone()
samsung.brand = 'Samsung'
samsung.model = 'Galaxy'
print(f'brand:{samsung.brand}, model:{samsung.model}')
print('-'*100)


class Laptop:
    brand = 'Acer'
    model = 'Predator'

laptop = Laptop()
setattr(Laptop, 'brand', 'Lenovo')
setattr(Laptop, 'model', 'ThinkPad')
print(f'brand:{getattr(laptop, "brand")}')
print(f'model:{getattr(laptop, "model")}')

print('-'*100)


class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False

    @staticmethod
    def get_sector():
        return OnlineShop.sector


OnlineShop.country = 'Poland'
attrs = [attr for attr in OnlineShop.__dict__.keys() if not attr.startswith('_')]
print(attrs)

del OnlineShop.sector_code
attrs = [attr for attr in OnlineShop.__dict__.keys() if not attr.startswith('_')]
print(attrs)
delattr(OnlineShop, 'sector')
attrs = [attr for attr in OnlineShop.__dict__.keys() if not attr.startswith('_')]
print(attrs)

for attr, value in OnlineShop.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')

print('-'*100)


def describe_attrs():
    for attr, value in OnlineShop.__dict__.items():
        if not attr.startswith('_'):
            print(f'{attr} -> {value}')

describe_attrs()


class HouseProject:
    numbers_of_floors = 3
    area = 50

    @staticmethod
    def describe_project():
        print(f'floor number:{HouseProject.numbers_of_floors}, area:{HouseProject.area}')

print(HouseProject.describe_project())