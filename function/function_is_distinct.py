def is_distinct(array):
    return len(array) == len(set(array))

print(is_distinct([1,2,2,3,4]))