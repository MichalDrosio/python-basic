# Your task, is to create NxN multiplication table, of size provided in parameter.
#
# for example, when given size is 3:


def multiplication_table(size):
    array = []
    for index in range(1, size+1):
        list = []
        for i in range(1, size+1):
            list.append(index*i)
        array.append(list)
    return array
print(multiplication_table(3))