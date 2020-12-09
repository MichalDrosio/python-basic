class SpaceShip:
    def attack(self):
        raise NotImplementedError('Attack method must be implemented')


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

