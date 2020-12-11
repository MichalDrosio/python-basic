class Laptop:
    def __init__(self, brand, model, price,):
        self.brand = brand
        self._model = model
        self.__price = price

    def show_attributes(self):
        for key, value in self.__dict__.items():
            print(f'{key}->{value}')

class Laptop2(Laptop):
    def __init__(self, code, margin, *args, **kwargs):
        super(Laptop2, self).__init__(*args, **kwargs)
        self.code = code
        self.__margin = margin

    def display_private_attrs(self):
        for attr in self.__dict__:
            if attr.startswith(f'_{self.__class__.__name__}__'):
                print(attr)

    def display_protected_arrts(self):
        for attr in self.__dict__:
            if attr.startswith('_') and not attr.startswith(f'_{self.__class__.__name__}'):
                print(attr)

laptop = Laptop('Acer', 'Predator', 5500)
print(laptop.__dict__)
laptop.show_attributes()
laptop2 =Laptop2(brand='Acer', model='Predator', price=5500, code='Ac-100', margin=1)
laptop2.display_private_attrs()
laptop2.display_protected_arrts()