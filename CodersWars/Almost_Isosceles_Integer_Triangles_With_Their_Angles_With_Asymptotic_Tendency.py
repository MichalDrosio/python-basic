# An Almost Isosceles Integer Triangle is a triangle that all its side lengths are integers and also,
# two sides are almost equal, being their absolute difference 1 unit of length.
#
# We are interested in the generation of the almost isosceles triangles by the diophantine equation
# (length sides of triangles are positive and not 0):
#
# x³-(x-1)³ = y² Eq.1
#
# So the first solution (x,y) for this equation is that may generate a real triangle and almost isosceles is (8,13),
# being the first nearly isosceles triangle (7,8,13).
#
# Equation 1 has infinite solutions (x,y), so the corresponding triangles will be (x-1,x,y)
#
# We need a code that can find those triangles with huge sides.
#
# You will be given an integer p (always valid and positive, and p ≠ 0) and your code should output
# the closest perimeter to p, let's name it p_, of the corresponding triangle.
#
# Examples:
#
# find_closest_perim(500) === 390 # (104, 105, 181) is the triangle with the closest perimeter to 500
#
# find_closest_perim(5000) === 5432 # perimeter of triangle (1455, 1456, 2521)
# In the case that you have two possible solutions, p_1 and p_2 being p_1 < p_2, because p = p_1 + (p_2 - p1)/2,
# you select the highest solution p_2.
#
# If p coincides with a perimeter of these triangles the output should be p.
#
# Features of the random tests: 1000 <= p <= 1e180

def perim(p):
    p_1, p_2 = 28, 390
    while p_2 < p:
        p_2, p_1 = 14*p_2 - p_1, p_2
    yield p_1, p_2


def find_closest_perim(p):
    return min(*perim(p), key=lambda p_: (abs(p_-p), -p_))

print(find_closest_perim(28))

