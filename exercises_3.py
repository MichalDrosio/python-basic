# To zadanie ma zapoznać Was z budową funkcji i pokazać, jak działa instrukcja return.
#
#     Napisz funkcję square(num), która zwróci wartość num podniesione do kwadratu.
#     Stwórz funkcję square_print(num). Niech ta funkcja będzie identyczna z funkcją z punktu poprzedniego podpunktu, jednak zamiast zwracać (return), niech wypisuje wynik (print).
def square(num):
    return num**2
print(square(2))

def square_print(num):
    print(num**2)
print(square_print(3))

# Zadanie 2
# Napisz funkcję multiply(subject, times), która zwróci wartość zmiennej subject pomnożoną przez wartość argumentu times. Zwróć uwagę, co się stanie, gdy jako wartość argumentu subject wpiszesz liczbę, a co, jeśli string.
def multipy(subject, times):
    return subject*times
print(multipy(2,3))
print(multipy('2',3))

# Zadanie 3
# Napisz funkcję power, która przyjmuje dwa argumenty:
#
#     base: obowiązkowy,
#     exponent: opcjonalny o standardowej wartości równej 2.
#
# Funkcja ma zwrócić wartość base podniesione do potęgi exponent.
def power(base, exponent=5):
    return base**exponent
print(power(2))
print(power(2,3))

# Zadanie 4
# Napisz funkcję convert_to_usd, która przyjmuje parametr zlotys, czyli kwotę w złotówkach. Funkcja ma zwrócić podaną kwotę w dolarach amerykańskich. Jako przelicznik przyjmij wartość 3,85 PLN = 1 USD.
def convert_to_usd(zlotys, usd=3.85):
    return zlotys/usd
print(convert_to_usd(1000))


# Zadanie 5
# Napisz funkcję to_celsius, która przyjmie parametr fahrenheit, czyli temperaturę w stopniach Fahrenheita. Funkcja ma przeliczyć temperaturę podaną w parametrze, na stopnie Celsjusza.
#
# Użyj wzoru:
#
#      (F - 32) * 5
# C =  ------------
#           9
#
# gdzie:
#
#     C – temperatura w stopniach Celsjusza,
#     F – temperatura w stopniach Fahrenheita.
def to_celsius(fahrenheit):
    return ((fahrenheit-35)*5)/9
print(to_celsius(50))



# Zadanie 6
#
# Napisz funkcję calculate_net, która przyjmie argumenty:
#
#     gross, czyli kwotę brutto ceny zakupu,
#     vat, czyli wartość podatku VAT. Możesz założyć, że VAT ma być liczbą zmiennoprzecinkową z zakresu 0 – 1.
#
# Funkcja ma zwrócić wartość netto ceny. Jakie obliczenia musisz wykonać?
def calculate_net(gross, vat):
    return gross/(1+vat)
print(calculate_net(123, 0.23))

# Zadanie 7
#
#     Napisz funkcję is_even, która przyjmie parametr number – dowolną liczbę całkowitą (możesz założyć, że programista wprowadzi prawidłową liczbę, nie musisz tego sprawdzać).
#     Funkcja ma zwrócić True, jeśli liczba jest parzysta, False – jeśli nie.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(3))

print('-'*100)
#     Napisz funkcję iterate_through, która przyjmie parametr number (nie musisz sprawdzać poprawności).
#     Następnie funkcja w pętli powinna przeitrerować od 1 do wartości number i sprawdzić parzystość kolejnej liczby.
#     Wynik należy wypisać na ekranie (nie zwrócić). Do sprawdzenia parzystości wykorzystaj funkcję is_even, napisaną przed chwilą.
def iterate_through(number):
    for i in range(number+1):
        print(i,':',is_even(i))
print(iterate_through(4))