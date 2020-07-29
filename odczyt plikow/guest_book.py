active = True
guests = 'pliki tekstowe/guest_book.txt'

while active:
    name = input("Podaj imię")
    if name == 'q':
        active = False
    else:
        print(f'Witaj {name.title()}')
        with open(guests, 'a') as file_object:
            file_object.write(f'{name.title()}\n')


