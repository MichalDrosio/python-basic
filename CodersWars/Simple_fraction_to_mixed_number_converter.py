# Given a string representing a simple fraction x/y, your function must return a string representing
# the corresponding mixed fraction in the following format:
#
# [sign]a b/c
#
# where a is integer part and b/c is irreducible proper fraction. There must be exactly one space between a and b/c.
# Provide [sign] only if negative (and non zero) and only at the beginning of the number
# (both integer part and fractional part must be provided absolute).
#
# If the x/y equals the integer part, return integer part only. If integer part is zero,
# return the irreducible proper fraction only. In both of these cases, the resulting string must not contain any spaces.
def to_int(string):
    result = []
    string = string.split('/')
    for i in string:
        result.append(int(i))
    return result


def fractal(num1, num2):
    num1 = abs(num1)
    num2 = abs(num2)
    if num1 != 1:
        num1_list = list(range( num1))
        for n1 in num1_list[::-1]:
            if num2 % n1 == 0 and num1 % n1 == 0:
                second_num = num2 / n1
                first_num = num1 / n1
                return f'{round(first_num)}/{round(second_num)}'
    else:
        return f'{num1}/{num2}'





def mixed_fraction(s):
    numbers = to_int(s)
    first_to_int = abs(numbers[0])
    second_to_int = abs(numbers[1])
    try:
        division_f_s = first_to_int// second_to_int
        rest_of_division = first_to_int % second_to_int
        other = first_to_int % second_to_int
        second_part_of_number = fractal(num1=other, num2=second_to_int)
        if first_to_int == 0:
            return '0'
        else:
            if division_f_s == 0:
                return f'{second_part_of_number}'
            else:
                if rest_of_division != 0:
                    result = f'{division_f_s} {second_part_of_number}'
                    if numbers[0] > 0 or (numbers[0] < 0 and numbers[1] < 0):
                        return result
                    return f'-{result}'
                else:
                    result = f'{division_f_s}'
                    if numbers[0] > 0 or (numbers[0] < 0 and numbers[1] < 0):
                        return result
                    return f'-{result}'
    except ZeroDivisionError:
        return 'Must raise ZeroDivisionError', lambda: mixed_fraction(s)



print(mixed_fraction('42/9'))
print(mixed_fraction('6/3'))
print(mixed_fraction('4/6'))
print(mixed_fraction('0/18891'))
print(mixed_fraction('-10/7'))
print(mixed_fraction('-22/-7'))
print(mixed_fraction('32/0'))




