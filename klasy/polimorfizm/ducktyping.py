class Duck:
    def make_sound(self):
        print('kwa kwa')

    def fly(self):
        print('kaczka lata')


class Human:
    def make_sound(self):
        print('czlowiek nasladuje kaczke: kwa kwa')

    def fly(self):
        print('czlowiek nie lata')


d = Duck()
h = Human()
array = [d, h]

for object in array:
    try:
        object.make_sound()
        object.fly()
        object.jump()
    except AttributeError as exc:
        print(f'brak atrybutu {exc}')
