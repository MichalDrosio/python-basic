# Jak wszystkim wiadomo, LOTTO to gra liczbowa polegająca na losowaniu 6 liczb z zakresu 1–49.
# Zadaniem gracza jest poprawne wytypowanie losowanych liczb. Nagradzane jest trafienie 3, 4, 5 lub 6 poprawnych liczb.
#
# Napisz program, który:
#
#     zapyta o typowane liczby, przy okazji sprawdzi następujące warunki:
#         czy wprowadzony ciąg znaków jest poprawną liczbą,
#         czy użytkownik nie wpisał tej liczby już poprzednio,
#         czy liczba należy do zakresu 1-49,
#     po wprowadzeniu 6 liczb, posortuje je rosnąco i wyświetli na ekranie,
#     wylosuje 6 liczb z zakresu i wyświetli je na ekranie,
#     poinformuje gracza, czy trafił przynajmniej "trójkę".
from random import randint
lotto = []
while len(lotto) != 6:
    digit = randint(1,49)
    if digit not in lotto:
        lotto.append(digit)


x = 6
player = []
while len(player) != 6:
    try:
        number = int(input(f'Podaj {x} liczb z zakresu 1-49:'))
        if number >= 1 and number <= 49:
            if number not in player:
                player.append(number)
                x -= 1
        else:
            print('Liczba poza zakresem')
    except ValueError:
        print('Tylko liczby całkowite')

game = sorted(lotto)
user = sorted(player)

print(f'Wylosowane liczby to:{game}')
print(f'Liczby gracza:{user}')

win =[]
for index in lotto:
    if index in player:
        win.append(index)
if len(win) < 3:
    print('Zagraj jeszcze raz')
if len(win) == 3:
    print('Trafiłeś 3')
if len(win) == 4:
    print('Trafiłeś 4')
if len(win) == 5:
    print('Trafiłeś 5')
if len(win) == 6:
    print('Trafiłeś 6')



