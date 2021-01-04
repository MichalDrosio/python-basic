items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
d = {}
for i in items:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

print(d)