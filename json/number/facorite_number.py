import json

number = input("Podaj ulubioną liczbe:")
filename = 'pliki/favorite_number.json'

with open(filename, 'w') as file_object:
    json.dump(number, file_object)