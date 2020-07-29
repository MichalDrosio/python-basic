guest = input('Podaj imie:')
guest_file = 'pliki tekstowe/guest.txt'
with open(guest_file, 'w') as file_object:
    file_object.write(guest)