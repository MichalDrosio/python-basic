import unittest
from list_with_square_of_numbers import list_with_square_of_numbers


class TestSquareNumbers(unittest.TestCase):

    def test_square_numbers(self):
        self.assertEqual(list_with_square_of_numbers(2), [1, 4])