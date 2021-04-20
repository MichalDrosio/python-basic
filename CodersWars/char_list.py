class CircularList():
    def __init__(self, *args):
        self.l = [v for v in args]
        if not self.l:
            raise Exception("")
        self.i = -1

    def next(self):
        self.i = self.i + 1
        self.i = self.i if len(self.l) > self.i else 0
        return self.l[self.i]

    def prev(self):
        self.i = self.i - 1
        self.i = self.i if self.i >= 0 else len(self.l) - 1
        return self.l[self.i]

c = CircularList(1,2,3,4,5,6)
print(c.prev())


