def get_formatted_name(name, surname, middle=''):
    if middle:
        full_name = f'{name} {middle} {surname}'
    else:
        full_name = f'{name} {surname}'
    return full_name.title()