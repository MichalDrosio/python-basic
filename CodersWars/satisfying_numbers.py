# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
def smallest(n):
    x = 1
    m = 1
    while m <= n:
        if x % m == 0:
            m += 1
            y = x
        else:
            x += y
    return x

print(smallest(10))

