import unittest

from testy.ankieta.survey import AnonymousSurey


class TestAnonmyousSurvey(unittest.TestCase):

    def setUp(self):
        question = 'Jaki jes twój ulubiony język programowania?'
        self.my_survey = AnonymousSurey(question)
        self.responses = ['sas', 'python', 'java']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

