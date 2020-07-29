class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'restauracja {self.name} serwoje {self.type}')

    def open_restaurant(self, open, close):
        print(f'restauracja {self.name} jest otwarta w godzinach od {open} do {close}')

    def client_served(self, client):
        if client >= self.number_served:
            self.number_served = client
            print(f'Obsłużono {self.number_served} klientow')
        else:
            print('nie mozna odejmowac')

    def set_number_served(self, client):
        if client > 0:
            self.number_served += client
            print(f'{self.name} Obsłużono {self.number_served} klientow')
        else:print('dupa')

res = Restaurant('Jadło', 'dania polskie')
res.describe_restaurant()
res.open_restaurant(12,24)
res.client_served(10)
res.client_served(-1)
res.set_number_served(10)
res.number_served =30
res.set_number_served(2)
res.client_served(40)

class IceCream(Restaurant):
    def __init__(self, name, type, flavors):
        self.flavors = flavors
        super(IceCream, self).__init__(name, type)

    def list_flavors(self):
        print(f'lodziarnia {self.name} oferuje smaki: ')
        for self.flavor in self.flavors:
            print(f'-{self.flavor}')

ice = IceCream('Lody naturalne', 'włoskie',['śmietankowe', 'pistacjowe', 'waniliowe'])
ice.list_flavors()
ice.set_number_served(20)