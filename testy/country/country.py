def country_and_city(city, country, population=''):
    if population:
        name = f'{city}, {country}-populacja {population}'
    else:
        name = f'{city}, {country}'
    return name