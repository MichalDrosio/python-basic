
def animal(file_animals):
    try:
        with open(file_animals) as file_animals_objects:
            content = file_animals_objects.read()
    except FileNotFoundError:
        print(f"Plik {file_animals} nie istnieje")
    else:
        pets = content.split()
        print(f'Plik {file_animals} zawiera następujące zwierzęta:')
        for pet in pets:
            print(f'\t-{pet}')

file_animals = ['pliki_tekstowe/cats', 'pliki_tekstowe/dogs', 'pets']
for file_animal in file_animals:
    animal(file_animal)




