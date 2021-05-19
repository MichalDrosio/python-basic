def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2

number = 8

function_array = [double, root, negative, div2]
tmp_return_value = number
for fun in function_array:
    tmp_return_value = fun(tmp_return_value)
    print(tmp_return_value)
