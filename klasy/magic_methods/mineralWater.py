class MineralEater:
    no_of_mineral_water = 0

    def __init__(self, sodium, calcium):
        self.sodium = sodium
        self.calcium = calcium

    def __eq__(self, other):
        return self.calcium == other.calcium and \
               self.sodium == self.sodium

    def __ne__(self, other):
        return not self == other

    def __le__(self, other):
        return self.sodium <= other.sodium and \
               self.calcium <= other.calcium

    def __lt__(self, other):
        return self <= other and not self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other


w1 = MineralEater(30, 123)
w2 = MineralEater(30, 123)
print({w1 == w2})
print({w1 != w2})
print({w1 <= w2})
print({w1 < w2})
print({w1 >= w2})
print({w1 > w2})