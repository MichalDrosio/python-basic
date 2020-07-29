
while True:
    try:
        podstawa = float(input('podaj podstawe:'))
        wyskosc = float(input('podaj wysokość:'))


        if wyskosc > 0 and podstawa > 0:
            p = wyskosc * podstawa / 2
            print(f'pole trojkata o podstawie:{podstawa} i wysokości:{wyskosc} wynosi:{p}')
            break
    except ValueError:
        print('podaj liczby')

