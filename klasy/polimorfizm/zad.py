from abc import ABC, abstractmethod


class PublicTransport(ABC):
    def transport_people(self):
        print(f'{self.__class__.__name__} transportuje {self.capacity}')

    @abstractmethod
    def display_info(self):
       pass


class Bus(PublicTransport):
    def __init__(self, brand, capacity, color):
        self.brand = brand
        self.capacity = capacity
        self.color = color

    def display_info(self):
        msg = f'brand: {self.brand}\ncapacity: {self.capacity}\ncolor: {self.color}'
        print(msg)


class MercedesBenzBus(Bus):
    def __init__(self, air_conditioning, *args, **kwargs):
        super(MercedesBenzBus, self).__init__(*args, **kwargs)
        self.air_conditioning = air_conditioning

    def display_info(self):
        super().display_info()
        print(f'Air conditioning: {self.air_conditioning}')


class Tram(PublicTransport):
    def __init__(self, tram_type, capacity, max_speed):
        self.tram_type = tram_type
        self.capacity = capacity
        self.max_speed = max_speed

    def display_info(self):
        msg = f'tram type: {self.tram_type}\ncapacity: {self.capacity}\nmax speed: {self.max_speed}'
        print(msg)


def transport_people_to_down_town(obj):
    print('destination down town')
    print(f'{obj.__class__.__name__} waiting for people...')
    print(f'{obj.__class__.__name__} ready to go')
    obj.transport_people()


def show_transport_specification(obj):
    print('Specifications')
    obj.display_info()

t = Tram('tram', 240, 80)
b = Bus('volvo', 40, 'red')
m = MercedesBenzBus(True, 'merc', 30, 'black')

punlic_transport = [t, b , m]

for obj in punlic_transport:
    transport_people_to_down_town(obj)
    print()
    show_transport_specification(obj)
    print('---------------------------------------')