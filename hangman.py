import random
import string

def hangman():
    avengers = random.choice(['iron man', 'spiderman', 'thor', 'hulk', 'loki ', 'captain america', 'black widow',
                            'hawkeye', 'war machine', 'black panter'])
    attempts = 10
    guess_made = ''
    print(avengers)
    while len(avengers) > 0:
        hero_name = ""
        for i in avengers:
            if i in guess_made:
                hero_name += i
            else:
                hero_name = hero_name + "_" + ""
        if hero_name == avengers:
            print(hero_name)
            print('Wygrales')
            break

        print(f'zgadles litery: {hero_name}')
        answer = input()
        for i in answer:
            if i in string.ascii_lowercase or i == ' ':
                guess_made += i
            else:
                print('Podaj poprawne znaki')
                answer = input()

        if answer not in hero_name:
            attempts -= 1
            print(f'Zostało {attempts} prób')



name = input('Podaj imie:\n')
print(f'Witaj {name.title()}')
print('*'*1000)
print('Sprobuj zgadnąć słowo w mniej niż 10 prob.')
hangman()
print()
