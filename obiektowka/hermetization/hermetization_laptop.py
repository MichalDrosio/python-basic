class Laptop:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        print(self._price)

    def set_price(self, value):
        if isinstance(value, (int, float)):
            if value > 0:
                self._price = value
            else:
                raise ValueError('The price attribute mus be a positive int or '
                                 'float value.')
        else:
            raise TypeError('The price attribute must be an int or float type.')

try:
    laptop = Laptop(-2000)
    laptop.get_price()
# try:
#     laptop.set_price(-3000)
except ValueError as error:
    print(error)
