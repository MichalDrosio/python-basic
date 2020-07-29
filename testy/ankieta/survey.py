class AnonymousSurey():
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_reponse):
        self.responses.append(new_reponse)

    def show_results(self):
        print("Oto wyniki ankiety:")
        for response in self.responses:
            print(f'-{response}')

survey = AnonymousSurey('Jaki jes twój ulubiony język programowania?')
survey.show_question()

while True:
    response = input('Język:')
    if response == 'q':
        break
    survey.store_response(response)

print('Dziękuje za udział w ankiecie')
survey.show_results()