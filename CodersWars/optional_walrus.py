# Re-write the initial function below so that it is 31 characters or less:
#
# def f(iterable, integer):
#     length = len(iterable)
#     if length > integer:
#         return length
#     else:
#         return 0
# This simple function takes an input iterable and an integer.
# If the length of the iterable is larger than the integer it returns that length.
# Otherwise it returns zero. All inputs will be valid and and all iterables will have a defined length.


def f(iterable, integer):
    length = len(iterable)
    if length > integer:
        return length
    else:
        return 0


print(f('abc', 2))
print(f([1,2,"a", "b"]*10, 10))