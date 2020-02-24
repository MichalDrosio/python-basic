# Zadanie 9.
#
# Napisz funkcję make_tuple, która przyjmie cztery parametry: a, b, c i d. Niech parametry c i d bedą opcjonalne i ich standardowe wartości będą wynosiły odpowiednio 3 i 4.
# Zwróć krotkę czterech elementów, której kolejnymi elementami będą wartości parametrów.
# Przykład:
#
# a = make_tuple("mama", "tata")
# print(a)
#
# ('mama', 'tata', 3, 4)
#
# a = make_tuple(0, 0, 0, 0)
# print(a)
#
# (0, 0, 0, 0)
def make_tuple(a,b,c=3,d=4):
    return (a,b,c,d)
print(make_tuple('ja','ty'))



# Zadanie 10.
# Napisz funkcję find_first_and_last, która przyjmie listę lub krotkę. Następnie zwróć krotkę, która będzie zawierać pierwszy i ostatni element parametru.
def find_first_and_last(array):
    return (array[0],array[-1])
print(find_first_and_last([1,2,3,4]))
print(find_first_and_last(('ja', 1,2,'ty')))

# Zadanie 11.
# Napisz funkcję format_date, która przyjmie 3 parametry:
#
#     day: dzień,
#     month: miesiąc,
#     year: rok.
#
# Funkcja powinna sprawdzić, czy data jest poprawna:
#
#     miesiąc powinen być w granicach (1, 12),
#     dzień nie może być większy od 30 - 31 (lub 28 w przypadku lutego, pomiń sprawdzanie lat przestępnych).
#
# Jeśli któryś z warunków będzie niezgodzny z kalendarzem, funkcja ma zwrócić None.
#
# Funkcja powinna zwrócić sformatowany łańcuch tekstowy w formacie "dzień miesiąc rok".
# Przykład
#
# d = format_date(12, 1, 2017)
# print(d)
#
# 12 stycznia 2017
#
# d = format_date(12, 13, 2017)
# print(d)
#
# None
dzien = (31,28,31,30,31,30,31,31,30,31,30,31)
miesiac = ('styczen', 'luty', 'marzec', 'kwiecen', 'maj', 'czerwiec', 'lipiec', 'sierpien', 'wrzesien', 'pazdziernik','listopad', 'grudzien')
def format_data(day, month, year):
    if month < 1 or month > 12:
        return None
    if day < 1:
        return None
    return f"{day}-{month}-{year}"
q = format_data(12,12,1987)
print(q)


# Zadanie 12.
#
# Napisz funkcję find_boundaries, która przyjmie listę liczb. Funkcja powinna zwrócić krotkę z najmniejszą i największą liczbą w zestawie.
# Jeśli na liście będzie element, nie będący liczbą, powinien zostać zignorowany. W przypadku wprowadzenia pustej listy, funkcja powinna zwrócić None.
# Przykład:
#
# b = find_boundaries([1, 5, 2, 3.5, -1])
# print(b)
#
# (-1, 5)
#
# b = find_boundaries([0, 2, "a kuku!", 10])
# print(b)
#
# (0, 10)
def skrajne_wartosci (x):
    return type(x)is int or type(x) is float

def find_bound(lst):
    n = 0
    while n < len(lst):
        if skrajne_wartosci(lst[n]):
            min = lst[n]
            max = lst[n]
            break
        n += 1

    while n < len(lst):
        if skrajne_wartosci(lst[n]):
            if lst[n] < min:
                min = lst[n]
            elif lst[n] > max:
                max = lst[n]
        n += 1
    return min, max

print(find_bound(['a','b','c',7,'dupa','12',123]))
#
# Zadanie 13.
#
# Napisz funkcję censor, która przyjmie jako parametr dowolnie długi łańcuch tekstowy. Następnie:
#
#     rozbije łańcuch tekstowy na listę wyrazów,
#     sprawdzi, czy nie znajdują się w nim słowa niedozwolone,
#     jeśli tak -- zamieni je na cztery gwiazdki (****)
#     ponownie połączy listę w string i zwróci wartość.
#
# Słowa niedozwolone:
#
# Java, C#, Ruby, PHP. (zwróć uwagę na wielkość znaków np. 'PhP' nie powinno być ocenzurowane)
#
# Słowa niedozwolone trzymaj jako listę wewnątrz funkcji censor.
# Przykład
#
# c = censor("Java is the best, but PHP is the bestest!")  # ;-)
# print (c)
#
# **** is the best, but **** is the bestest!
def censor(x):
    cen = ['Java', 'C#', 'Ruby', 'PHP']
    array = x.split()
    print(array)
    for i in array:
        if i in cen:
            stars = i.replace(i,'***')
            print(stars, end=' ')
    print()
    s = ''
    for z in array:
        s += z+" "
    print(s)

print(censor("Java is the best, but PHP is the bestest!"))




# Zadanie 14.
#
# Napisz funkcję check_palindrome, która pobierze jeden wyraz i sprawdzi, czy jest palindromem.
# Funkcja powinna zwracać True, jeśli łańcuch jest palindromem, False, jeśli nie jest.
def check_palindrome(inscription):
    if inscription == inscription[::-1]:
        return True
    else:
        return False
print(check_palindrome('ala ala'))