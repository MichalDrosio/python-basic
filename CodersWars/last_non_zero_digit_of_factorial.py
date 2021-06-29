# Your task is to find the last non-zero digit of n!n!n! (factorial).
#
# n!=1×2×3×⋯×nn! = 1 \times 2 \times 3 \times \dots \times nn!=1×2×3×⋯×n
#
# Example:
# If n=12n = 12n=12, your function should return 666 since 12!=47900160012 != 479001\bold{6}0012!=479001600
#
# Input
# Non-negative integer n
# Range: 0 - 2.5E6
#
# Output
# Last non-zero digit of n!n!n!
from functools import reduce


def last_digit(n):
    # num = 1
    # for i in range(2, n+1):
    #     num *= i
    num = reduce(lambda x, y: x*y, range(2, n+1))
    new_num = str(num).replace('0', '')
    return int(new_num[-1])

print(last_digit(387))