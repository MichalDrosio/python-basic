# Write a class decorator @remember which makes the class remember its own objects,
# storing them in a dictionary with the creating arguments as keys.
#
# Also, you have to avoid creating a new member of the class with the
# same initial arguments as a previously remembered member.
#
# Additionally, if the (decorated) class is A, you will have to reach that dictionary of remembered objects directly
# on A, i.e. by A[args] and by the loop for x in A over the keys.

# Example
# A sample usage:
#
# @remember
# class A(object):
#   def __init__(self, x,y=0,z=0):
#     pass
#
# a = A(1)
# b = A(2,3)
# c = A(4,5,6)
# d = A(1)
#
# >>> A[1] is a is d
# True
# >>> A[2,3] is b
# True
# >>> A[4,5,6] is c
# True
# >>> for x in A: print x,
# (2,3) (4,5,6) 1

def remember(cls):

    class decorated_class:
        def __call__(self, *args):
            if len(args) == 1:
                args = args[0]
            if args not in self.cache:
                self.cache[args] = cls(*args) if hasattr(args, '__iter__') else cls(args)
            return self.cache[args]

        def __init__(self, *args):
            self.cache = {}

        def __getitem__(self, *args):
            return self.cache[args[0]]

        def __iter__(self):
            return self.cache.keys().__iter__()

    return decorated_class()


