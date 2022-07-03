import unittest
from CodersWars.Unique_In_Order import unique

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        test_word = 'OollknDnn'
        self.unique = unique(test_word)
        self.results = ['O', 'o', 'l', 'k', 'n', 'D', 'n']
        self.bad_result =['O', 'l', 'k', 'n', 'D']

    def test_unique(self):
        self.assertEqual(self.unique, self.results)

    def test_unique_fail(self):
        self.assertNotEqual(self.unique, self.bad_result)




if __name__ == '__main__':
    unittest.main()