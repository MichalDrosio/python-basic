import uuid

class Product:
    def __init__(self, name, price):
        self.product_id = self.get_id()
        self.name = name
        self.price = price

    def __repr__(self):
        return f'Name:{self.name}, price:{self.price}'

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]

for name in Product.__dict__:
    print(name)


class Phone(Product):
    def __init__(self, phone_id, *args, **kwargs):
        super(Phone, self).__init__(*args, **kwargs)
        self.phone_id = phone_id


p = Phone(name='Phone', price=2999, phone_id=100)
print(p.__dict__)