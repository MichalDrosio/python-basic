from math import pi, atan


def tankvol(h, d, vt):
    if h == d:
        return vt
    elif h == d/2:
        return int(vt/2)
    r = d / 2
    a = r - h
    b = ((r ** 2) - (a ** 2)) ** 0.5
    x = vt / 2
    y = (r ** 2) * pi
    res = x * 2 * ((atan(b / a) / pi) - (a * b / y))
    if res < 0:
        res = vt + res
    return int(res)


print(tankvol(40, 120, 3500))