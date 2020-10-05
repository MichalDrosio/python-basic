def gen_fib(n):
    a = 0
    b = 1
    for i in range(n+1):
        yield a
        a, b = b, a + b
    print()
print(list(gen_fib(5)))


class IterFib():
    def __init__(self, n):
        self.a = 0
        self.b = 1
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > self.n:
            raise StopIteration
        self.i += 1
        x = self.a
        self.a, self.b = self.b, self.a+self.b
        return x


array = []
for x in IterFib(5):
    array.append(x)
print(array)
