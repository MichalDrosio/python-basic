import unittest

from CodersWars.Duplicate_Encoder import duplicate_encode



class MyTestCase(unittest.TestCase):

    def setUp(self):
        word = 'din'
        self.encoder = duplicate_encode(word)
        self.results = '((('


    def test_duplicate_encode_true(self):
        self.assertEqual(self.encoder, self.results)





if __name__ == '__main__':
    unittest.main()
