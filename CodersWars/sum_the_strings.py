# Create a function that takes 2 nonnegative integers in form of a string as an input,
# and outputs the sum (also as a string):
#
# Example: (Input1, Input2 -->Output)
#
# "4",  "5" --> "9"
# "34", "5" --> "39"

def sum_str(a, b):
    if not a and not b:
        return '0'
    elif not a:
        return b
    elif not b:
        return a
    else:
        return str(int(a)+int(b))