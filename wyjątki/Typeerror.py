
lista = []
while True:
    def cal(num1):
        while type(num1) != float:
            number1 = input('Podaj pierwszą liczbę:\n')
            try:
                num1 = float(number1)
            except ValueError:
                print('to nie liczba')
        return num1
    c1 = cal(num1='number1')

    def cal2(num2):
        while type(num2) != float:
            number2 = input('Podaj drugą liczbę:\n')
            try:
                num2 = float(number2)
            except ValueError:
                print('to nie liczba')
        return num2
    c2 = cal2(num2='number2')

    wynik = c1+c2
    print(wynik)
    lista.append(wynik)
    end = input("Czy chcesz zakończyć działanie programu?\n"
                "Jeśli tak wpisz '(T/N)'")
    if end == 'T':
        break
print(lista)






