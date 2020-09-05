# Write a program, which will find all such numbers between 1000 and 3000
# (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
def number_even(numbers):
    numbers_even = []
    for index in range(1000, numbers+1):
        if index % 2 == 0:
            numbers_even.append(index)
    return numbers_even

def print_number():
    for i in number_even(3000):
        print(i, end=' ')


print_number()