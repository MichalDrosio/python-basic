import uuid


class Product:
    def __init__(self, product_name, price):
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return f'{self.__class__.__name__}(product_name={self.product_name}, price={self.price})'

    def __str__(self):
        return f'{self.__class__.__name__}:{self.product_name}|{self.price}'

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[6]


class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product_name, price):
        product_names = [product.product_name for product in self.products]
        if product_name not in product_names:
            self.products.append(Product(product_name, price))

    def remove_product(self, product_name):
        for product in self.products:
            if product_name == product.product_name:
                self.products.remove(product)

    def display_products(self):
        for item in self.products:
            print(f'{item}')

    def sort_by_price(self, ascending=False):
        return sorted(self.products, key=lambda product: product.price,
                      reverse=not ascending)

    def search_product(self, query):
        return [item for item in self.products if query in item.product_name]



warehouse = Warehouse()
print(warehouse.__dict__)
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2990.0)
print(warehouse.products)
print(warehouse.__dict__)
warehouse.remove_product('Laptop')
print(warehouse.__dict__)
warehouse.display_products()
for product in warehouse.sort_by_price():
    print(product)
print(warehouse.search_product('Ca'))