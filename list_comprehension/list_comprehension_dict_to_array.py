data = dict(zip(('a', 'b', 'c', 'd', ' e', 'f'),(1, 2, 3, 4, 5, 6)))
print(data)
array = [[x, y] for x, y in data.items()]
print(array)