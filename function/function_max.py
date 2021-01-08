def maximum(x, y):
    if x > y:
        return x
    else:
        return y


def maximum_2(x, y, z):
    if x > y and x > z:
        return x
    elif y > z:
        return y
    else:
        return z