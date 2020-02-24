


# Zadanie
# Napisz funkcję d6(num), która zasymuluje rzuty kostką sześcienną. num to parametr, który oznacza liczbę rzutów kostką. Funkcja ma zwrócić sumę wyrzuconych oczek.
from random import randint
def d6(num):
    array = []
    for i in range(num):
        i =randint(1,6)
        array.append(i)
    return sum(array)
print(d6(2))

# Zadanie 1
# (W tym zadaniu nie musisz pisać funkcji)
# Napisz program, w którym zdefiniujesz wielolinijkowy łańcuch tekstowy. Wpisz tam zwrotkę swojego ulubionego wiersza, po czym wyświetl go na konsoli.
print("""sandakds
sad,as.,/d
;ldsamas;l""")

# Zadanie 2
# Napisz funkcję o nazwie square_area która policzy i zwróci pole prostokąta (przyjmując dwa parametry oznaczające długość jego boków). Przyjmij, że parametry wejściowe są poprawne.
def square_area(lenght, width):
    return lenght * width
print(square_area(2,3))

# Zadanie 3
# Napisz funkcję o nazwie circle_circuit, która przyjmując średnicę okręgu zwróci jego obwód. Przyjmij, że parametry wejściowe są poprawne. Przyjmij pi=3.14.
def circle_circuit(diameter, pi=3.14):
    return diameter * pi
print(circle_circuit(5))

# Zadanie 4
# Napisz funkcję o nazwie dogs_age, który przeliczy wiek psa w psich latach.
#
#     funkcja powinna przyjmować wiek psa jako parametr,
#     dla pierwszych dwóch lat, każdy rok życia psa jest równy 10.5 ludzkiego roku,
#     powyżej dwóch lat, każdy rok życia psa, to 4 ludzkie lata,
#     funkcja powinna zwrócić wiek psa.
#
# Przykład:
#
# azor = dogs_age(1.5)  # spodziewany wynik: 1.5 * 10.5 = 15.75
#
# burek = dogs_age(5)  # spodziewany wynik: 2 * 10.5 + 3 * 4 = 33
def dogs_age(age):
    if age <= 2:
        return age * 10.5
    else:
        return (age - 2) * 4 + 21
print(dogs_age(5))
print(dogs_age(1.5))

# Zadanie 5.
# Napisz funkcję chessboard, który przyjmie parametr n jako opcjonalny. Standardowa wartość parametru ma wynosić 8.
# Funkcja ma zwrócić wielolinijkowy napis reprezentujący szachownicę złożoną ze znaków # i spacji.
# Szachownica powinna mieć wymiary n x n.
# Przykład: Przy n=8, szachownica powinna składać się 8 wierszy, każdy po 8 znaków, naprzemiennie # i spacja.
#
# c = chessboard()
# print(c)
#
# # # # #
#  # # # #
# # # # #
#  # # # #
# # # # #
#  # # # #
# # # # #
#  # # # #

def chessboard(n=8):
    s = ""
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                s += ' '
            else:
                s += '#'
        s += "\n"
    return s
print(chessboard())

# Zadanie 6.
# Napisz funkcję is_divided_by_4, która przyjmie liczbę i sprawdzi, czy liczba jest podzielna przez 4 i odpowiednio zwróci True lub False.
def is_divided_by_4(number):
    if number % 4 == 0:
        return True
print(is_divided_by_4(3))
print(is_divided_by_4(4))

# Zadanie 7.
# Napisz funkcję histogram, która przyjmie listę liczb, po czym zwróci histogram ze znaków #. Jeśli użytkownik poda wartość nie będącą liczbą, funkcja powinna zwrócić wartość None.
#
# Wynikowy histogram ma być wielolinijkowym napisem składającym się ze znaków #. Jedna linijka = jeden słupek histogramu.
# Przykład:
#
# h = histogram([2, 6, 3, 1])
# print(h)
#
# ##
# ######
# ###
# #
#
# h = histogram([1, 2, 'error!'])
# print(h)
#
# None
def histogram(array):
    his = ''
    try:
        for i in array:
            for j in range(i):
                his += '#'
            his +='\n'
        return his
    except: TypeError
print(histogram([1,2,3]))
print(histogram([1,2,'a']))

# Zadanie 8(*). Ciąg Fibonacciego.
#
# Napisz funkcję fib liczącą ciąg Fibonacciego. Funkcja powinna:
#
#     przyjmować jako parametr n - liczbę; ma to być element, dla którego liczymy wartość,
#     zwracać wartość elementu ciągu dla elementu n.
#
# Podpowiedź:
#
# Ciąg Fibonacciego to ciąg liczb naturalnych. Określa się go rekurencyjnie w sposób następujący: pierwszy element jest równy 0, drugi 1, każdy następny jest sumą dwóch poprzednich.
#
# Sprawdź w internecie, co to jest rekurencja i jak napisać funkcję, która to wykorzystuje.

def fibb(n):
    array = [1, 1]
    for i in range(n-2):
        array.append(array[i] + array[(i + 1)])
    return array
print(fibb(10))

def fibb2(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a
print(fibb2(100))

def rec_fib(n):
    if n < 2:
        return 1
    else:
        return rec_fib(n-1) + rec_fib(n-2)
print(rec_fib(10-1))

def fibb_req2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibb_req2(n-1)+fibb_req2(n-2)

print (fibb_req2(10))

def fibb_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    n_minus_dwa = 0
    n_minus_1 = 1
    for x in range(n-1):
        suma = n_minus_dwa + n_minus_1
        n_minus_dwa = n_minus_1
        n_minus_1 = suma
    return suma
print(fibb_iter(100))
