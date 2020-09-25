import unittest

from print_wvwn_numbers import number_even


class TestEvenNumber(unittest.TestCase):

    def test_number(self):
        self.assertEquals(number_even(0, 10), [0, 2, 4, 6, 8, 10])
