def dot_product(array_1, array_2):
    return sum([i * j for i, j in zip(array_1, array_2)])


print(dot_product([1, 2], [5, 2]))