def euclidean_distance(x, y):
    result = [(i - j) ** 2 for i, j in zip(x, y)]
    return (sum(result)) ** 0.5


print(euclidean_distance([0, 3], [4, 0]))


