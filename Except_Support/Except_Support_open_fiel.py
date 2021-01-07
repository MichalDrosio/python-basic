try:
    with open('file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('nie znaleziono')