# Zadanie 1.
#
# Napisz funkcję name_sorter, która przyjmie jako parametr listę imion.
# Funkcja ma zwrócić słownik:
#
#     klucz o nazwie male ma mieć jako wartość imiona męskie z listy wejściowej,
#     klucz o nazwie female ma mieć jako wartość imiona żeńskie z listy wejściowej.
#
# Dodatkowo, posortuj imiona w ramach swoich list.
#
# Należy przyjąć, że imiona żeńskie, to te, które kończą się literą "a". Barnabę możemy spokojnie zignorować. ;-)
#
# Przykład:
#
# names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]
# print(name_sorter(names))
#
# {'female': ['Alicja', 'Barbara'], 'male': ['Andrzej', 'Cezary', 'Henryk']}
def name_sorter(array_names):
    male = []
    flemale = []
    for i in array_names:
        if i[-1] == 'a':
            flemale.append(i)
        else:
            male.append(i)
    return {'male':male, 'flemale':flemale}
print(name_sorter(['Ola', 'Michal', 'Magda', 'Jan']))


# Zadanie 2
# Napisz funkcję validate_password, która sprawdzi, czy hasło przekazane do funkcji jako parametr jest bezpieczne i zwróci True jeśli jest, False jeśli nie jest.
#
# Jak sprawdzić siłę hasła?
#
#     hasło powinno być dłuższe niż 8 znaków,
#     funkcja powinna sprawdzać, czy każda kolejna litera w haśle zawiera się w zbiorze liter wielkich, liter małych, cyfr i znaków specjalnych. Możesz w swoim zadaniu wykorzystać poniższy zbiór znaków:
#
valid_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+[{]}\|;:?/>.<,'
def validate_password(password):
    if len(password) > 8:
        for i in password:
            if i in password:
                pass
        return True
    else:
        return False


print(validate_password('Amicaaaaah7'))
print(validate_password('mi77'))

# Zadanie 3
# Napisz funkcję div, która przyjmie dwa argumenty liczbowe: a i b. Funkcja ma zwrócić True, jeśli a dzieli się przez b bez reszty, w przeciwnym przypadku – False
def div(a, b):
    if a % b == 0:
        return True
    else:
        return False
print(div(8,4))
print(div(3,2))

# Zadanie 4
# Napisz funkcję find_longest_word, która przyjmie napis w postaci łańcucha tekstowego i zwróci najdłuższe słowo z tego łańcucha.
# W przypadku, gdy w oryginalnym napisie kilka słów jest tej samej długości, zwróć pierwsze z nich.
#
# Przykład:
#
# print(find_longest_word("I find your lack of faith disturbing"))
#
# disturbing
def find_longest_word(array):
    a = array.split()
    longest_word =''
    for word in a:
        if len(word) > len(longest_word):
            longest_word = word
    print(longest_word)

print(find_longest_word('I find your lack of faith disturbing'))

# Zadanie 5
#
# Napisz funkcję poker_hand, która wylosuje i wyświetli na ekranie 5 kart z puli kart do gry. Listę z kartami znajdziesz w pliku answers.py.
# Pamietaj, że musisz usunąć kartę z puli, gdy ją wylosujesz

_card_values = ['A', 'K', 'Q', 'J',
                '10', '9', '8', '7', '6', '5', '4', '3', '2']
_card_colors = ['hearts', 'diamonds', 'spades', 'clubs']


cards = [v + ' of ' + c for v in _card_values for c in _card_colors]

import random

def poker_hand():
    cards = [v + ' of ' + c for v in _card_values for c in _card_colors]
    cards_5 = []
    while len(cards_5) != 5:
        card = random.choice(cards)
        if card not in cards_5:
            cards_5.append(card)
    return cards_5
print(poker_hand())

