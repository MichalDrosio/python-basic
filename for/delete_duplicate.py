items = [1, 5, 3, 2, 2, 4, 2, 4]
result = []
for i in items:
    if i not in result:
        result.append(i)
print(result)

print(list(set(items)))