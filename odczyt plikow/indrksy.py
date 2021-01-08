with open('pliki tekstowe/indeksy.txt', 'r') as file:
    lines = file.read().splitlines()

indexes = [index for index in lines if index.startswith('WIG')]
print(indexes)