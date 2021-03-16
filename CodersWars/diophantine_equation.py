# In mathematics, a Diophantine equation is a polynomial equation, usually with two or more unknowns,
# such that only the integer solutions are sought or studied.
#
# In this kata we want to find all integers x, y (x >= 0, y >= 0) solutions of a diophantine equation of the form:
#
# x2 - 4 * y2 = n
# (where the unknowns are x and y, and n is a given positive number) in decreasing order of the positive xi.
#
# If there is no solution return [] or "[]" or "". (See "RUN SAMPLE TESTS" for examples of returns)

def sol_equa(n):
    res = []
    for num in range(n+1):
        for number in range(n+1):
            if num**2 - 4 * number**2 == n:
                res.append([num, number])
    return res


import math


def sol_equa2(n):
    res = []
    print(int(math.sqrt(n)))
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(i)
            j = n // i
            if (i + j) % 2 == 0 and (j - i) % 4 == 0:
                x = (i + j) // 2
                y = (j - i) // 4
                res.append([x, y])

    return res


print(sol_equa(12))
print(sol_equa(13))
print(sol_equa(16))
print(sol_equa(17))

print(sol_equa2(90005))

