import unittest

from exercises_16 import bina
from testy.szyfr_cezara.szyfr import cezar

class TestCezar(unittest.TestCase):

    def test_codowania(self):
        self.assertEqual(cezar('baca', 3), 'edfd')

    def test_odkodowania(self):
        self.assertEqual(cezar('edfd', -3), 'baca')

    def test_result(self):
        self.assertEqual(bina(1, 1), 10)