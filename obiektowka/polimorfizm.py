class Duck:
    def make_sound(self):
        print('kwa kwa')

    def fly(self):
        print('duck fly')

class Human:
    def make_sound(self):
        print('Human say kwa kwa')

    def fly(self):
        print('Human not fly')

duck = Duck()
human = Human()
array = {duck, human}
for obiekt in array:
    try:
        obiekt.fly()
        obiekt.make_sound()
        obiekt.jump()
    except AttributeError as exe:
        print(f'Brak atrybitu {exe}')


class SpaceShip:
    def attack(self):
        raise NotImplementedError('Attack method must be implemented')

class LightSpaceShip(SpaceShip):
    dmg = 10
    def attack(self):
        print(f'{self.__class__.__name__} attack {self.dmg}')

class HeacySpaceShip(SpaceShip):
    dmg = 15
    def attack(self):
        print(f'{self.__class__.__name__} attack {self.dmg}')

class MagicSpaceShip():
    dmg = 20
    def attack(self):
        print(f'{self.__class__.__name__} attack {self.dmg}')

class TanksSpaceShip(SpaceShip):
    dmg = 25
    def attack(self):
        print(f'{self.__class__.__name__} attack {self.dmg}')

ls = LightSpaceShip()
hs = HeacySpaceShip()
ms = MagicSpaceShip()
ts = TanksSpaceShip()
array_ships = [ls, hs, ms, ts]

for ship in array_ships:
    ship.attack()