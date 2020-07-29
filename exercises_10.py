# Napisz program "parzyste.py", który wczyta od użytkownika liczbę całkowitą i wyświetli informację, czy jest to liczba parzysta, czy nieparzysta.
while True:
    try:
        l = int(input('podja liczbe:'))
        print(f"Liczba {l} jest parzysta?:",l % 2 == 0)
        break
    except ValueError:
        print('to nie liczba')
