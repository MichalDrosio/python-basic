import json

def read_favorite_number():
    filename = 'pliki/favorite_number.json'
    try:
        with open(filename) as file_object:
            number = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return number

def save_number():
    number = input("Podaj ulubioną liczbe")
    filename ='pliki/favorite_number.json'
    with open(filename, 'w') as file_object:
        json.dump(number, file_object)
    return number

def know_number():
    number = read_favorite_number()
    if number:
        print(f"Twoja ulubiona liczba to {number}")
    else:
        number = save_number()
        print(f"Twoja ulubiona liczba została zapisana {number}")

know_number()