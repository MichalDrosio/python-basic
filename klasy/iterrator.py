class MyIterator:
    def __init__(self, max):
        self.x = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        x = self.x
        if x > self.max:
            raise StopIteration
        self.x += 1
        return x


for i in MyIterator(10):
    print(i)


class Reverse():
    def __init__(self, data='michal'):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


for i in Reverse():
    print(i, end='')


