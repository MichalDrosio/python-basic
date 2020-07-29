import json

filename = 'pliki/username.json'

with open(filename) as file_object:
    username = json.load(file_object)
    print(f"Witamy ponownie {username.title()}")