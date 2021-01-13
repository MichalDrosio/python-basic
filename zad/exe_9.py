def concat(array_1, array_2):
    result = [[i[0], j[0]] for i, j in zip(array_1, array_2)]
    return result


print(concat([[1], [2]], [[3], [4]]))