# Your goal in this kata is to implement a difference function, which subtracts one list from another
# and returns the result.
# It should remove all values from list a, which are present in list b.


def array_diff(a, b):
    array = []
    for i in a:
        if i not in b:
            array.append(i)
    return array

a = [1,2,2,2]
b = [1]
print(array_diff(a,b))


def array_diff_lambda(a, b):
    result = filter(lambda i: i not in b, a)
    return list(result)
print(array_diff_lambda(a, b))