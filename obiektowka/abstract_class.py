from abc import ABC, abstractmethod

class SpaceShip(ABC):

    @abstractmethod
    def attack(self):
        pass


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