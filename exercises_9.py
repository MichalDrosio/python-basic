# Napisz prostą grę w zgadywanie liczb. Komputer musi wylosować liczbę w zakresie 1 – 100. Następnie:
#
#     Zadać pytanie: "Zgadnij liczbę" i pobrać liczbę z klawiatury.
#     Sprawdzić, czy wprowadzony napis, to rzeczywiście liczba i w razie błędu wyświetlić komunikat "To nie jest liczba", po czym wrócić do pkt. 1
#     Jeśli liczba podana przez użytkownika jest mniejsza niż wylosowana, wyświetlić komunikat "Za mało!", po czym wrócić do pkt. 1.
#     Jeśli liczba podana przez użytkownika jest większa niż wylosowana, wyświetlić komunikat "Za dużo!", po czym wrócić do pkt. 1.
#     Jeśli liczba podana przez użytkownika jest równa wylosowanej, wyświetlić komunikat "Zgadłeś!", po czym zakończyć działanie programu.
#
# Przykład:
#
# Zgadnij liczbę: cześć
# To nie jest liczba.
# Zgadnij liczbę: 50q
# Za mało!
# Zgadnij liczbę: 75
# Za dużo!
# Zgadnij liczbę: 63
# Zgadłeś!
from random import randint
number = randint(0, 100)
print(number)
while True:
    try:
        num = input('podaj cyfre')
        numb = int(num)
        if number > numb:
            print('za mało')
        if number < numb:
            print('za dużo')
        if number == numb:
            print('wygrałeś')
            break
    except ValueError:
        print("To nie jest liczba."
              "Jeszcze raz")

