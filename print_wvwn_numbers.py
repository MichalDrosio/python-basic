# Write a program, which will find all such numbers between first_num and 3000
# (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
def number_even(first_num, numbers):
    numbers_even = []
    for index in range(first_num, numbers+1):
        if index % 2 == 0:
            numbers_even.append(index)
    return numbers_even


def print_number():
    for i in number_even(1000, 3000):
        print(i, end=' ')


print_number()
