# class A:
#     def __init__(self):
#         print("__init__")
#
#     def __call__(self, *args, **kwargs):
#         print("__init__")
#
#
# a = A()
# print(callable(a))
# a()


class Fib:
    def __init__(self):
        self.cach = {
            0: 0,
            1: 1
        }

    def __call__(self, number):
        if number not in self.cach:
            self.cach[number] = self.__call__(number-1) + self.__call__(number-2)
        return self.cach[number]

    def __repr__(self):
        return f'{self.cach}'


f = Fib()
print(f(10))
print(f)