# Konwersja liczby dziesietnej na binarną
import unittest


def bina(a, b):
    c = a + b

    binarna = []
    while c > 0:
        if c % 2 == 0:
            binarna.append('0')
        if c % 2 != 0:
            binarna.append('1')
        c = (c / 2) - ((c % 2) / 2)
    x = binarna[::-1]
    return int(''.join(x))


class TestBinarna(unittest.TestCase):
    def test_result(self):
        self.assertEqual(bina(1, 6), 10)
