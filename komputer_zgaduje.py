# Odwróćmy teraz sytuację z warsztatu "Gra w zgadywanie liczb": to użytkownik pomyśli sobie liczbę z zakresu 1-1000,
# a komputer będzie zgadywał i zrobi to maksymalnie w 10 ruchach (pod warunkiem, że gracz nie będzie oszukiwał).
#
# Zadaniem gracza będzie udzielanie odpowiedzi "więcej", "mniej", "trafiłeś".

print('Pomyśl liczbę od 0 do 1000 a ja zgadnę w max 10 próbach. Odpowiadaj "za dużo","za mało" lub "ok"')

min = 0
max = 1000

próby = 10

while próby != 0:
    print(f'zgaduje, (pozostałych prób:{próby})', int((min + max) / 2))
    odp = input('oceń')
    if odp == 'za duzo':
        max = (min + max) / 2
        próby -= 1
    else:
        if odp == 'za mało':
            min = (min + max) / 2
            próby -= 1
        else:
            if odp == 'ok':
                print('wygrałeś')
                break
            print('błędna odp')
 



