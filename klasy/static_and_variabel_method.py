class Cat:
    quantity_cats = 0

    def __init__(self, name):
        self.name = name
        Cat.quantity_cats += 1

    @staticmethod
    def get_quantity_cats():
        print(f'Liczba kotów to {Cat.quantity_cats}')

    def __del__(self):
        print(f'Kot {self.name} zostal usniety')
        Cat.quantity_cats -= 1


Cat.get_quantity_cats()

c1 = Cat('nala')

Cat.get_quantity_cats()

c2 = Cat('nikson')

Cat.get_quantity_cats()

del c2
