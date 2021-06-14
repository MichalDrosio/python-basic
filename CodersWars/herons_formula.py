# Write function heron which calculates the area of a triangle
# with sides a, b, and c.
#
# Heron's formula: sqrt (s * (s - a) * (s - b) * (s - c)),
# where s = (a + b + c) / 2. Output should have 2 digits precision.
from math import sqrt


def heron(a, b, c):
    s = (a + b + c) / 2
    return round(sqrt(s * (s - a) * (s - b) * (s - c)), 2)


print(heron(3, 4, 5))