import random
from time import sleep

class Warrior:
    def __init__(self, kind='', hp=0, strength=0, defence=0):
        self.kind = kind
        self.hp = hp
        self.strength = strength
        self.defence = defence

    def hit(self):
        return random.randint(0, self.strength)

    def protection(self):
        return random.randint(0, self.defence)

    def lose_life(self, value):
        self.hp -= value
        if self.hp <= 0:
            print(f'{self.kind} poległ')

    def is_he_alive(self):
        if self.hp <= 0:
            return False
        else:
            return True

    def __str__(self):
        return self.kind



def fight(warlock, knight):
    round = 1
    while (warlock.is_he_alive() and knight.is_he_alive()):
        print(f'Round: {round}')
        show_statistic(warlock, knight)

        if random.randint(0,1) == 0:
            duel(warlock, knight)
        else:
            duel(knight, warlock)

        print('')
        sleep(5)
        round += 1

    if knight.is_he_alive():
        print('Rycerz wygrał')
    else:
        print('Czarownik wygrał')


def duel(warlock, knight):
    print(f'{warlock} zostal zatakowany przez {knight}')
    damage = knight.hit() - warlock.protection()
    if damage > 0:
        print(f'{warlock} stracil {damage} punktow zycia')
        warlock.lose_life(damage)
    else:
        print(f'{warlock} obronił się i nie stracil zycia')


def show_statistic(x, y):
    for i in (x,y):
        print(f'{i} ma {i.hp} zycia')


knight = Warrior('Knight', random.randint(20, 100), random.randint(5, 30), random.randint(15, 40))
warlock = Warrior('Warlock', random.randint(10, 50), random.randint(10, 50), random.randint(5, 15))

fight(warlock, knight)
