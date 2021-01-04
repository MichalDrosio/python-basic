result = []

for i in range(10,101):
    if i % 11 == 0 and i % 3 != 0:
        print(i, end=',')
        result.append(str(i))
print()
print(','.join(result))