import pytest
import unittest
from square_value import sqquare_value


class TestSquare(unittest.TestCase):

    def test_square(self):
        self.assertEqual(sqquare_value(2), 4)

