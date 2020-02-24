# Zadanie 1 - Zmienne
#
#     Stwórz zmienną o nazwie temp i wartości 15
#     Stworz zmienną o nazwie temp_2 i wartości '15'
#     Czym różnią się zmienne temp i temp_2?
#     Spróbuj wykonać operacje (dodawania, mnożenie itp) na tych zmiennych i zobcz jake będą efekty tych działań

temp = 15.0
temp_2 = '15'
# print(temp*temp_2)

    # print(temp+temp_2)
    # print(temp-temp_2)
    # print(temp/temp_2)



# Zadanie 2 - Typy
#
# Aby sprawdzić typ zmiennej należy użyć słówka kluczowego type i tak jeśli mamy zadelkarowaną zmienną title to poleceniem type(title) sprawdzimy typ zmiennej title
#
#     Sprawdz typy zmiennych zadeklerowanych w pierwszym ćwiczeniu
#     Napisz program w którym sprawdzsz typ zmiennej:
#     Jeśli jest integer to wypiszesz na ekran zmienną pomnożoną przez 5
#     Jeśli jest Float to wypiszesz na ekran zmienną podzieloną przez 5
#     Jeśli jest stringiem to poprosu wypiszesz ten string na ekran

if type(temp) == int:
    print(temp*5)
elif type(temp) == float:
    print(temp/5)
else:
    print(temp)

# Zadanie 3 - Pętla for
#
#     Zadeklaruj zmienną no_of_stars w której będzie losowa liczba z zakreso od 1 do 20.
#
#     Wyświetl na ekranie wylosowaną liczbę.
#     Wyśwetl na ekranie tyle gwiazdek (*) ile wynosi wartość liczby.
#
# Przykład działania programu:
#
# Wylosowana liczba: 6
#
# ******
from random import randint
no_of_stars = randint(1,20)
print(no_of_stars)
print(no_of_stars*"*")
for i in range(no_of_stars):
    print('*', end='')
print()


# Zadanie 4 - Pętla for
#
#     Zadeklaruj zmienne rows i columns w której będą losowe liczby z zakreso od 5 do 15.
#     Wyświetl na ekranie wylosowane liczby.
#     Wyśwetl na ekranie prostokąt zbudowany z gwiazdek (*) o wylosowanych rozmiarach.
#
# Przykład działania programu:
#
# Wartość zmiennej rows: 5
# Wartość zmiennej columns: 10
#
# **********
# **********
# **********
# **********
# **********

rows = randint(5,15)
columns = randint(5,15)
print(rows, columns)
for i in range(rows):
    for x in range(columns):
        print('*',end='')
    print()

# Zadanie 5 - Pętla for
#
#     Zadeklaruj zmienne size w której będzie losowa liczba z zakreso od 3 do 9.
#     Wyświetl na ekranie wylosowaną liczbę.
#     Wyśwetl na ekranie choinkę zbudowaną z gwiazdek (*) o wylosowanych rozmiarach.
#
# Przykład działania programu:
#
# Wielkość choinki: 5
#
# *
# **
# ***
# ****
# *****

number = randint(3,9)
print(number)
for i in range(number+1):
    for x in range(i):
        print('*', end='')
    print()