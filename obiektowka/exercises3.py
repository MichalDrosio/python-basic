def stick(*args):
    args = [arg for arg in args if isinstance(arg, str)]
    result = '#'.join(args)
    return result


print(stick('sport', 'winter'))
print(stick('snowboard', 2, 'salomon', 2, 'dc'))
print(stick(False, 2, True, 1, 'workout', [], 'snow'))


def display(company, **kwargs):
    print(f'company:{company}')
    if 'price' in kwargs:
        print(f'price:{kwargs["price"]}')

display(company='kazar', price=299)

