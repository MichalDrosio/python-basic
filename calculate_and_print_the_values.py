# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
import math


def check_values(d):
    d = input('Podja wartości liczbowe oddzielone przecinkami:\n')
    D = d.split(',')
    array = []
    try:
        for i in D:
            int_i = int(i)
            array.append(int_i)
        return array
    except ValueError:
        print('Tylko liczby')


def calculate():
    c = 50
    h = 30
    array = []
    for d in check_values(d='d'):
        q = round(math.sqrt((2 * c * d)/h))
        array.append(q)
    return array


def print_results():
    for i in calculate():
        print(i, end=',')


print_results()
