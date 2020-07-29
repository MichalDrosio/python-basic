def bulid_profile(first, last, **user_info):
    profile = {}
    profile['imie'] = first
    profile['nazwisko'] = last
    for key, value in user_info.items():
        profile[key] = value

    return profile
user_profile = bulid_profile('michal', 'drosio', miejsce='warszawa', zawod='programista')
u_p = bulid_profile('magda', 'drosio', praca='microsoft', stanowisko='account menager')
print(user_profile)
print(u_p)


def list_sandwich(*ingredients):
    print('twoja kanapka z dodatkami jest gotowa: ')
    for ingred in ingredients:
        print(f'-{ingred}')
list_sandwich('ser', 'szynka', 'pomidor')

def car_info(brand, model, **info):
    car = {}
    car['marka'] = brand
    car['model'] = model
    for key, value in info.items():
        car[key] = value
    return car

c = car_info('alfa romeo', 'gulia', kolor='niebieski', moc='280km', rok_produkcji=2020)
print(c)

def show_car():
    car_info(brand='brand',model= 'model',info= '**info')
    for k, v in c.items():
        print(f'{k}:{v}')
show_car()