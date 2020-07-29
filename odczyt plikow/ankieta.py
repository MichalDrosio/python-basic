users = 'pliki tekstowe/guest_book.txt'

questionnaire = 'pliki tekstowe/ankieta.txt'

with open(users) as file_objects:
    user = file_objects.readlines()

while user:
    if len(user) != 0:
        answer = input("Ankieta anonimowa. Dlaczego lubisz programować?")
        user.pop()
        with open(questionnaire, 'a') as file_questionnaire:
            file_questionnaire.write(f'{answer}\n')


