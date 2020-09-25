import unittest

from question import solve


class TestSolve(unittest.TestCase):

    def test_solve(self):
        self.assertEqual(solve(2, 6),(1, 1))
