from _collections import OrderedDict
from random import randint
fav_lang = OrderedDict()
fav_lang['ola'] = 'python'
fav_lang['janek'] = 'sas'
fav_lang['michal'] = 'python'
fav_lang['magda'] = 'java'

for name, lang in fav_lang.items():
    print(f'Ulubiony jezyk {name} to {lang}')


class Die():
    def __init__(self, sides=6, roll=3):
        self.sides = sides
        self.roll = roll
        self.suma = 0

    def roll_die(self):
        oczka = randint(1,self.sides)
        print(oczka)
        for i in range(self.roll):
            oczka = randint(1,self.sides)
            print(f'{i+1}:kostka o liczbie scianek {self.sides} wyrzucono {oczka} oczka')
            self.suma += oczka
        print(f'laczna suma oczek to {self.suma}')
d =Die(roll=6)
d.roll_die()