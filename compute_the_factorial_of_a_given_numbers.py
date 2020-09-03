# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
import unittest

array = {}

def compute_the_factorial_of_a_given_numbers(num):
    r = 1
    try:
        num = int(input('Podaj liczbe calkowita'))
        if num > 0:
            for index in range(1, num+1):
                r *= index
            array[num] = r

        else:
            print('Dodatnia')
        return array

    except ValueError:
        print("Podaj liczbe")


while True:
    compute_the_factorial_of_a_given_numbers(num='num')
    print(array)
    end = input('Chcesz zakonczyć? wpisz"t"')
    if end == 't':
        break

