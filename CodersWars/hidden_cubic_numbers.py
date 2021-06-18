# We search non-negative integer numbers, with at most 3 digits, such as the sum of the cubes of their digits is the number itself; we will call them "cubic" numbers.
#
# 153 is such a "cubic" number : 1^3 + 5^3 + 3^3 = 153
# These "cubic" numbers of at most 3 digits are easy to find, even by hand, so they are "hidden" with other numbers and characters in a string.
#
# The task is to find, or not, the "cubic" numbers in the string and then to make the sum of these "cubic" numbers found in the string, if any, and to return a string such as:
#
# "number1 number2 (and so on if necessary) sumOfCubicNumbers Lucky"
# if "cubic" numbers number1, number2, ... were found.
#
# The numbers in the output are to be in the order in which they are encountered in the input string.
#
# If no cubic numbers are found return the string: `"Unlucky"``.
#
# Examples:
#  - s = "aqdf&0#1xyz!22[153(777.777"
#    the groups of at most 3 digits are 0 and 1 (one digit), 22 (two digits), 153, 777, 777 (3 digits)
#    Only 0, 1, 153 are cubic and their sum is 154
#    Return: "0 1 153 154 Lucky"
#
# - s = "QK29a45[&erui9026315"
#   the groups are 29, 45, 902, 631, 5. None is cubic.
#   Return: "Unlucky"
import re


def is_sum_of_cubes(s):
    numbers = re.findall(r'\d{1,3}', s)

    valid = []
    for num in numbers:
        x = 0
        for n in num:
            x += int(n) ** 3
        if str(x) == num:
            valid.append(str(x))

    if not valid:
        return "Unlucky"
    else:
        return f"{' '.join(valid)} {sum(map(int, valid))} Lucky"
# s = "QK297a45[&erui9026315"
s2 = "aqdf&0#1xyz!22[153(777.777"
print(is_sum_of_cubes(s2))
# print(is_sum_of_cubes(s2))
