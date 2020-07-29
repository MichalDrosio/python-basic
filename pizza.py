def make_pizza(size, *toppings):
    print(f'\nPrzygotowuję pizzę o wielkości {size}cm z nastepującymi dodatkami:')
    for topping in toppings:
        print(f'-{topping}')

def list_sandwich(*ingredients):
    print('twoja kanapka z dodatkami jest gotowa: ')
    for ingred in ingredients:
        print(f'-{ingred}')

