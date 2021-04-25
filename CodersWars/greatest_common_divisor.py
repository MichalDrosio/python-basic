

def mygcd(x, y):
    if x % y == 0:
        return y
    else:
        return mygcd(y, x % y)


def mygcd2(x, y):
    while y > 0:
        x, y = y, x % y
    return x


print(mygcd2(30, 12))