class Animal:
    def __init__(self, kind, name, age):
        self.kind = kind
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.kind} {self.name} ma {self.age} lat'

    def make_noise(self):
        if self.kind == 'kot':
            print('mial')
        elif self.kind == 'pies':
            print('hau hau')


if __name__ == '__main__':

    cat = Animal('kot', 'Nala', 1)
    dog = Animal('pies', 'Red', 10)
    print(cat.__str__())
    print(cat.make_noise())
    print(dog.__str__())
    print(dog.make_noise())
