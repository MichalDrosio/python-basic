import unittest

from testy.name.name_function import get_formatted_name


class NameTestCase(unittest.TestCase):

    def test_name_surname(self):
        formatted_name = get_formatted_name(name='ola', surname='drosio')
        self.assertEqual(formatted_name, 'Ola Drosio')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name(name='magda', middle='monika', surname='drosio')
        self.assertEqual(formatted_name, 'Magda Monika Drosio')

