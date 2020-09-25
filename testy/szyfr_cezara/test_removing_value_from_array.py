import unittest
from removing_values_from_list import removing_value_from_array


class TestArray(unittest.TestCase):

    def test_array(self):
        self.assertEqual(removing_value_from_array([1,2,3,24]), [1,2,3])