from random import randint


class OrcRace:
    def __init__(self, name, damage, defence, health):
        self.name = name
        self.damage = damage
        self.defence = defence
        self.health = health

    def attack(self):
        print(f'{self.name} zadał {randint(0, self.damage)}')
        return randint(0, self.damage)

    def block(self):
        return randint(0, self.defence)

    def lose_life(self, value):
        self.health -= value
        if self.health <= 0:
            print(f'{self.name} przegrał')

    def is_he_alive(self):
        if self.health <= 0:
            return False
        else:
            return True

    def __str__(self):
        return self.name


class Troll(OrcRace):
    def __init__(self, name, damage, defence, health):
        super(Troll, self).__init__(name, damage, defence, health)

    def throw_spear(self):
        print("Rzut włócznią")
        super().attack()


class Tauren(OrcRace):
    def __init__(self, name, damage, defence, health, special_totem=False):
        super(Tauren, self).__init__(name, damage, defence, health)
        self.special_totem = special_totem

    def use_totem(self):
        print('Uderzenie totemem')
        super().attack()
        if self.special_totem:
            print('Użyłeś totemu! Zadałeś ddatkowe 20 obrażeń')


orc = OrcRace('Orc', 5, 5, 30)
troll = Troll('Troll', 8, 3, 20)
tauren = Tauren('Tauren', 15, 15, 50, True)


