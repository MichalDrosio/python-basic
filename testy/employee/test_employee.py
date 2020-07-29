import unittest

from testy.employee.employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.earnings = Employee(name='michal', surname='drosio', year_income=10000)

    def test_defalut_raise(self):
        self.assertEqual(self.earnings.give_raise(), 15000)

    def test_give_custome_raise(self):
        self.assertEqual(self.earnings.give_raise(10000), 20000)
