def sort_list(items):
    return sorted(items, key=lambda item: item[1])


print(sort_list([(1, 3), (4, 6), (5, 2), (4, 1)]))