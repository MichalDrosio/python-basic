import json

filename = 'pliki/favorite_number.json'

with open(filename) as file_object:
    number = json.load(file_object)
    print(f"Twoja ulubiona liczba to {number}")