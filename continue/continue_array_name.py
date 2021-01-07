names = ['Jack', 'Leon', 'Alice', None, 'Bob', 2]

for name in names:
    if name is None or type(name) == int:
        continue
    print(name)