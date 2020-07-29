



with open('pliki tekstowe/pi_m.txt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Podaj datę urodzin (w formacie ddmmrr):")
if birthday in pi_string:
    print('twoja liczba znajduje sie w pi')
else:
    print('brak twojej liczby')

