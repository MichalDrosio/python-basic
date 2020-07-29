import json


def greet_stored_username():
    filename = 'pliki/username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("Jak masz na imię?")
    filename = 'pliki/username.json'
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username

def greet_user():
    username = greet_stored_username()
    if username:
        print(f"Witamy ponownie {username.title()}")
    else:
        username = get_new_username()
        print(f"{username.title()}, twoje imię zostało zapisane")

greet_user()