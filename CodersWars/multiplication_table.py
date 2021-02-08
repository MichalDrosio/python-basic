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


print(multiplication_table(2))


def multiplication_table_2(rows, column):
    array = []
    for i in range(1, column+1):
        result = []
        for j in range(1, rows+1):
            result.append(i*j)
        array.append(result)
    return array


print(multiplication_table_2(3, 3))