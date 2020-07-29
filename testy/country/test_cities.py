import unittest

from testy.country.country import country_and_city


class CityTest(unittest.TestCase):

    def test_city_country(self):
        name = country_and_city(country='Italy', city='Rzym')
        self.assertEqual(name, 'Rzym, Italy')

    def test_city_country_population(self):
        name = country_and_city(city='New York', country='USA', population='10000000')
        self.assertEqual(name, 'New York, USA-populacja 10000000')