# A Leyland number is a number of the form x^y+y^x
# where xxx and yyy are integers greater than 1.


# The first few such numbers are:
# 8 = 2^2 + 2^2
# 17 = 2^3 + 3^2
# 32 = 2^4 + 4^2
# 54 = 3^3 + 3^3

# Return all Leyland numbers up to 1012 as a list, in ascending order.
#
# Your code can be maximum 80 characters long.
def f():
    f = lambda r=range(2, 40): sorted({x ** y + y ** x for x in r for y in r})[:121]

print(f())