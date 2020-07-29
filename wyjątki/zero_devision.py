print("Podaj dwie liczby które zostaną prze siebie podzielone.")
print("Wpisz 'q' aby zakończyć działanie programu.")
results = []
while True:
    first_number = input('\nPierwsza liczba:')
    if first_number == 'q':
        break
    second_number = input('\nDruga liczba:')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
        print(answer)
        results.append(answer)
        print(results)
    except ZeroDivisionError:
        print("Nie można dzielić przez zero!")
    except ValueError:
        print('Podaj liczbe!')
