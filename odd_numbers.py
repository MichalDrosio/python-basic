# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9


def odd_numbers(numbers):

    return [index for index in numbers.split(',') if int(index) % 2 != 0]


def print_num():
    for i in odd_numbers('1,2,3,4,5,6,7,8,9'):
        print(i)


print_num()
