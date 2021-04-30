# Data: an array of integers, a function f of two variables and an init value.
#
# Example: a = [2, 4, 6, 8, 10, 20], f(x, y) = x + y; init = 0
#
# Output: an array of integers, say r, such that
#
# r = [r[0] = f(init, a[0]), r[1] = f(r[0], a[1]), r[2] = f(r[1], a[2]), ...]
#
# With our example: r = [2, 6, 12, 20, 30, 50]
#
# Task:
# Write the following functions of two variables
#
# som : (x, y) -> x + y
# mini : (x, y) -> min(x, y)
# maxi : (x, y) -> max(x, y)
# lcmu : (x, y) -> lcm(abs(x), abs(y) (see note for lcm)
# gcdi : (x, y) -> gcd(abs(x), abs(y) (see note for gcd)
# and
#
# function oper_array(fct, arr, init) (or operArray or oper-array) where
#
# fct is the function of to variables to apply to the array arr (fct will be one of som, mini, maxi, lcmu or gcdi)
#
# init is the initial value
#
# Examples:
# a = [18, 69, -90, -78, 65, 40]
# oper_array(gcd, a, a[0]) => [18, 3, 3, 3, 1, 1]
# oper_array(lcm, a, a[0]) => [18, 414, 2070, 26910, 26910, 107640]
# oper_array(sum, a, 0) => [18, 87, -3, -81, -16, 24]
# oper_array(min, a, a[0]) => [18, 18, -90, -90, -90, -90]
# oper_array(max, a, a[0]) => [18, 69, 69, 69, 69, 69]


def gcdi(x, y):
    x, y = abs(x), abs(y)
    while (y != 0):
        x, y = y, x % y
    return x


def lcmu(a, b):
    return abs(a * b) // gcdi(a, b)


def som(a, b):
    return (a + b)


def maxi(a, b):
    return max(a, b)


def mini(a, b):
    return min(a, b)


def oper_array(fct, arr, init):
    n, res = init, []
    for r in arr:
        n = fct(n, r)
        res.append(n)
    return res


arr = [18, 69, -90, -78, 65, 40]

