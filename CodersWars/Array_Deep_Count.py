# len(a) will give you the number of top-level elements in the list/array named a.
#
# Your task is to create a function deepCount that returns the number of ALL elements within an array,
# including any within inner-level arrays.
#
# For example:
#
# deepCount([1, 2, 3]);
# //>>>>> 3
# deepCount(["x", "y", ["z"]]);
# //>>>>> 4
# deepCount([1, 2, [3, 4, [5]]]);
# //>>>>> 7

def deep_count(array):
    count = 0
    for item in array:
        count += 1
        if isinstance(item, list):
            count += deep_count(item)
    return count



print(deep_count([1, 2, [3, 4, [5]]]))

