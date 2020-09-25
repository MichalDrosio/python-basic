import unittest

from odd_numbers import odd_numbers


class TestOddNumbers(unittest.TestCase):

    def test_odd_numbers(self):
        self.assertEqual(odd_numbers('1,2,3,4,5,6'), ['1', '3', '5'])
