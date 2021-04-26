# Create a function that returns the average of an array of numbers ("scores"), rounded to the nearest whole number.
# You are not allowed to use any loops (including for, for/in, while, and do/while loops).

def average(array):
    return round(sum(array) / len(array))


print(average([5, 78, 52, 900, 1]))