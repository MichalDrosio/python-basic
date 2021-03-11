from abc import ABC, abstractmethod

class Vehicle(ABC):

    def transport_people(self):
        print(f'{self.__class__.__name__} przewozi {self.capacity} ludzi')

    @abstractmethod
    def display_info(self):
        pass

class Tram(Vehicle):
    def __init__(self, capacity, tram_type, max_speed):
        self.tram_type = tram_type
        self.max_speed = max_speed
        self.capacity = capacity


    def display_info(self):
        msg = f'{self.tram_type}\n{self.capacity}\n{self.max_speed}'
        print(msg)

class Bus(Vehicle):
    def __init__(self, capacity, brand, color):
        self.capacity = capacity
        self.brand = brand
        self.color = color


    def display_info(self):
        msg = f'{self.brand}\n{self.capacity}\n{self.color}'
        print(msg)

class MercedesBenzBus(Bus):
    def __init__(self, air_conditioning, *args, **kwargs):
        super(MercedesBenzBus, self).__init__(*args, **kwargs)
        self.air_conditioning = air_conditioning


    def display_info(self):
        super().display_info()
        print(f'{self.air_conditioning}')



def transport_people_to_downtown(obj):
    print('destination downtown')
    print(f'{obj.__class__.__name__} waiting for people...')
    print(f'{obj.__class__.__name__} ready to go!')
    obj.transport_people()

def show_transport_specification(obj):
    print('Specification')
    obj.display_info()


merc = MercedesBenzBus(capacity=40, color='black', air_conditioning=True, brand='Merc')
avenio_tram = Tram(tram_type='Avenio', max_speed=240, capacity=100)
volvo_bus = Bus(brand='Volvo', capacity=200,color='black')
p_t_a = [merc, avenio_tram, volvo_bus]
for i in p_t_a:
    transport_people_to_downtown(i)
    print()
    show_transport_specification(i)
    print('-------------------')
#

