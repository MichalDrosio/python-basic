class Ship:
    def __init__(self, damage):
        self.damage = damage

    def deal_damage(self):
        print(f'{self.__class__.__name__} {self.damage}')


class BattleShip(Ship):
    def __init__(self, special_damage, *args, **kwargs):
        super(BattleShip, self).__init__(*args, **kwargs)
        self.special_damage = special_damage

    def deal_special_damage(self):
        print(f'{self.__class__.__name__} {self.special_damage}')


class BigBattleShip(BattleShip):
    def __init__(self, bomb_damage, *args, **kwargs):
        super(BigBattleShip, self).__init__(*args, **kwargs)
        self.bomb_damage = bomb_damage

    def deal_special_damage_twice(self):
        for _ in range(2):
            super().deal_special_damage()

    def use_bomb(self):
        print(f'{self.__class__.__name__} {self.bomb_damage}')


class CargoShip(Ship):
    def __init__(self, capacity, *args, **kwargs):
        super(CargoShip, self).__init__(*args, **kwargs)
        self.capacity = capacity

    def transport(self):
        print(f'{self.__class__.__name__} {self.capacity}')

ship = Ship(10)
battle_ship = BattleShip(special_damage=10, damage=10)
ship.deal_damage()
battle_ship.deal_special_damage()
big_battle_ship = BigBattleShip(special_damage=10, damage=10, bomb_damage=20)
cargo_ship = CargoShip(damage=10, capacity=50)
print('------------')
big_battle_ship.use_bomb()
print('------------')
big_battle_ship.deal_special_damage_twice()
print('------------')
big_battle_ship.deal_damage()
print('------------')
cargo_ship.transport()
cargo_ship.deal_damage()