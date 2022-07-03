import unittest
from CodersWars.squares_sums import square_sum


class MyTestCase(unittest.TestCase):
    def test_square_sums_true(self):
        self.assertEqual(square_sum([1,2,2]), 9)

    def test_square_sums_false(self):
        self.assertNotEqual(square_sum([1, 2, 2, 3]), 9)


if __name__ == '__main__':
    unittest.main()
