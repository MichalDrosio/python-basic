import math

def check_number(data):
    data_int = data.split(',')
    array = []
    if len(data_int) == 2:
        try:
            for i in data_int:
                i = int(i)
                array.append(i)
            return array
        except ValueError:
            print('podaj liczby')
    else:
        return 'podja 2 liczby'


def ellipse_area():
    numbers = check_number(data=input('dwie liczby oddzielone przecinkami'))
    num_1 = numbers[0]
    num_2 = numbers[1]
    if num_1 > 0 and num_2 > 0:
        if num_1 != num_2:
            return math.pi * num_1 * num_2

print(ellipse_area())