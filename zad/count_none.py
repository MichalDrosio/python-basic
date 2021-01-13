def count_none(array):
    counter = 0
    for i in array:
        if i == None:
            counter += 1
    return counter

print(count_none([1, None, None, 5, None, 2]))