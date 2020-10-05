def generator(a ,b):
    while a < b:
        yield a
        a += 3


for i in generator(1,20):
    print(i, end='')
print()


def reverse_gen(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]


for i in reverse_gen('magda'):
    print(i, end='')

