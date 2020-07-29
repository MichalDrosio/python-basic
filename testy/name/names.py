from testy.name.name_function import get_formatted_name

while True:
    name = input("\nPodaj imię:")
    if name == 'q':
        break
    surname = input("Podaj nazwisko")
    if surname == 'q':
        break

    formatted_name = get_formatted_name(name, surname)
    print(f"\timie i nazwisko to: {formatted_name}")
