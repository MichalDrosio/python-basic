# Napisz funkcję shorten, która przyjmie dowolnie długi napis, po czym zwróci skrót napisu, jak w przykładzie:
#
# shortened = shorten("Don't repeat yourself")
# print(shortened)
#
# DRY
#
# shortened = shorten("Read the fine manual")
# print(shortened)
#
# RTFM
#
# shortened = shorten("All terrain armoured transport")
# print(shortened)
#
# ATAT
def shorten(word):
    x = word.upper()
    y = x.split()
    array = []
    for i in y:
        array.append(i[0])
    z = ''.join(array)
    return z

def sho(slowo):
    slowo = slowo.split()
    print(slowo)
    x =[a[0].upper() for a in slowo]
    print(x)
    litera=''
    for y in x:
        litera += y
    return litera

print(shorten("All terrain armoured transport"))
print(sho("All terrain armoured transport"))


# Napisz funkcję check_palindrome, która pobierze dowolnie długi łańcuch tekstowy i sprawdzi, czy jest palindromem.
# Funkcja powinna zwracać True, jeśli łańcuch jest palindromem, False, jeśli nie jest.
# Podpowiedzi:
#
# Palindrom to słowo lub zdanie, które czytane wspak brzmi tak samo, jak od początku, np. "kajak", "radar", czy "Kobyła ma mały bok".
#
#     Podczas sprawdzania palindromu, pamiętaj o spacjach.
def chesk_palindrome(words):
    word = words.lower()
    word = word.replace(' ', '')
    if word == word.lower()[::-1]:
        return True
    return False

print(chesk_palindrome("Kobyła ma mały bok"))


# Napisz funkcję div, która przyjmie 2 argumenty liczbowe. Argumenty to początek i koniec zakresu liczb.
# Funkcja ma jako wynik, zwrócić listę liczb w podanym zakresie, które jednocześnie są podzielne przez 2 i niepodzielne przez 3.
# Wprowadzony zakres powinien być domknięty, tzn. należy sprawdzić także liczby, które są początkiem i końcem zakresu.
# Przykład:
#
# result = div(0, 20)
# print(result)
#
# [2, 4, 8, 10, 14, 16, 20]
def div(a,b):
    array = []
    x = range(a, b+1)
    for i in x:
        if i % 2 == 0 and i % 3 != 0:
            array.append(i)
    return array
print(div(0,20))


# Napisz funkcję roll, która przyjmie 3 parametry:
#
#     liczbę kostek,
#     opcjonalnie: typ kostki (dozwolone kostki 3, 4, 6, 8, 10, 12 i 100 ścienne), standardowa wartość, to 6 ,
#     opcjonalnie: modyfikator wyniku (liczba dodana, lub odjęta od wyniku kośćmi), standardowa wartość, to 0.
#
# Następnie funkcja ma zasymulować rzut odpowiednią liczbą kostek, zsumować wyniki i dodać (lub odjąć) modyfikator. Wynik ma zwrócić.
#
# Dla uproszczenia możesz przyjąć, że wszystkie liczby podane jako parametry są liczbami naturalnymi.
#
# Jeśli użytkownik wpisze kostkę, której nie ma w powyższym zestawieniu, funkcja ma wyrzucić wyjątek Exception z komunikatem "No such dice!"
# Podpowiedź
#
# roll(2, 10, 20)  # rzut 2 kostkami 10-ściennymi, do wyniku dodać 20
# roll(3, 6, -3)  # rzut 3 kostkami 6-ściennymi, od wyniku odjąć 3

import random
def roll(rzuty, ilosc_scianek=6,modulator=0):
    if ilosc_scianek in [3, 4, 6, 8, 10, 12,100]:
        proby = []
        for cyfry in range(rzuty):
            proby.append(random.randint(1, ilosc_scianek))
        print(proby)
        proby = sum(proby) + modulator

    return proby
try:
    print(roll(4))
except:
    print('nie ma tylu scianek')