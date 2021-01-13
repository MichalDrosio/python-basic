def trace(array):
    total = 0
    for idx, item in enumerate(array):
        total += item[idx]
    return total


print(trace([[1, 2, 1], [4, 2, 1], [5, 6, 7]]))