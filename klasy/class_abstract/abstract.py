from abc import ABC, abstractmethod

class SpaceShip:

    @abstractmethod
    def attack(self):
        pass

class LightSpaceShip(SpaceShip):
    dmg = 5

    def atack(self):
        print(f'light attack: {self.dmg} dmg')


class HeavySpaceShip(SpaceShip):
    dmg = 10

    def atack(self):
        print(f'heavy attack: {self.dmg} dmg')

class MagicSpaceShip(SpaceShip):
    dmg = 15

    def atack(self):
        print(f'magic attack: {self.dmg} dmg')

class TankSpaceShip(SpaceShip):
    dmg = 25

    def atack(self):
        print(f'tank attack: {self.dmg} dmg')

l_s = LightSpaceShip()
h_s = HeavySpaceShip()
m_s = MagicSpaceShip()
t_s = TankSpaceShip()

ships_array = [l_s, h_s, m_s, t_s]
for ship in ships_array:
    ship.atack()


class A():

    def __init__(self):
        print(f'{self.__class__.__name__}:class A')


class B(A):

    def __init__(self):
        super().__init__()

        print(f'{self.__class__.__name__}:class B')


class C(A):

    def __init__(self):
        super().__init__()

        print(f'{self.__class__.__name__}:class C')


class D(B, C):

    def __init__(self):
        super().__init__()

        print(f'{self.__class__.__name__}: class D')


d = D()