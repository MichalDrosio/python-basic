# A Leyland number is a number of the form xy+yxx^y + y^xx y +y where xxx and yyy are integers greater than 1.
# The first few such numbers are:
# 8=2^2 + 2^2
# 17=2^3+3^2
# 32 = 2^4 + 4^2
# 54=3^3 = 3^3 + 3^3
# Return all Leyland numbers up to 1012 as a list, in ascending order.

# Your code can be maximum 80 characters long.

r = range(2,40)
f = lambda: sorted({i**j+j**i for i in r for j in r})[:121]

