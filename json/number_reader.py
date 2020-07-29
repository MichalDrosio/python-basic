import json

filename = 'pliki/numbers.json'

with open(filename) as file_object:
    numbers = json.load(file_object)

print(numbers)