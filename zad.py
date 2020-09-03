import unittest

while True:

    def stawka_vat(vat):
        while vat != 23 and vat != 8 and vat != 5:
            try:
                vat = float(input('Podaj wartość vat:23%, 8% albo 5% wpisując wartość jako liczbę całkowitą\n'))

            except ValueError:
                print('Podaj wartość liczbową')
        return vat
    vat = stawka_vat(vat='vat')


    def wartosc_netto(netto):
        while type(netto) != float or netto <= 0:
            try:
                netto = float(input('Podaj cenę netto towaru:\n'))
                if netto <= 0:
                    print('Cena musi być większa od "0"')
            except ValueError:
                print('Podaj wartość liczbową')
        return netto
    netto = wartosc_netto(netto='netto')


    def obliczenia(netto, stawka_vat):
        brutto = netto + (netto * (stawka_vat / 100))
        return round(brutto, 2)
    cena_brutto = obliczenia(netto=netto, stawka_vat=vat)


    print(f'Cena brutto:{cena_brutto} zł, stawka vat {vat}%')
    print(f'Cena netto: {netto} zł')



    end = input("Czy chcesz zakończyć działanie programu?\n"
                "Jeśli tak wpisz 't' ")
    if end == 't':
        break


