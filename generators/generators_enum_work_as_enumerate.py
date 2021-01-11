def enum(array):
    counter = 0
    for index in array:
        yield (counter, index)
        counter += 1


print(list(enum([1, 2, 3, 4, 5])))
