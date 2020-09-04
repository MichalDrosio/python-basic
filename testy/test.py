import unittest

from generate_dictionary import generate_dictionary
from compute_the_factorial_of_a_given_numbers import compute_the_factorial_of_a_given_numbers
from simple_calss import Example

class TestNum(unittest.TestCase):
    def test_num(self):
        self.assertEqual(compute_the_factorial_of_a_given_numbers(3), {3: 5})

    def test_generate_dictionary(self):
        self.assertEqual(generate_dictionary(5), {1: 1, 2: 4, 3: 9, 4: 16, 5: 25})
