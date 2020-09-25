import unittest

from remove_duplicate_from_list import remove_duplicate_from_list


class TestRemoveDuplicate(unittest.TestCase):

    def test_remove(self):
        self.assertEqual(remove_duplicate_from_list([1, 1, 2, 3, 3, 3]), [1, 2, 3])