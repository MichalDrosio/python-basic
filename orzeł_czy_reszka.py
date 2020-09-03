import unittest

from exercises_16 import bina


class CalTest(unittest.TestCase):
    def result(self):
        self.assertEqual(bina(1, 6), 10)