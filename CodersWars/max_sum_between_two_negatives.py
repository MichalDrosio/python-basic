# You have a list of integers. The task is to return the maximum sum of the elements located
# between two negative elements, or -1, Nothing, or a similar empty value, if there is no such sum.
# No negative element should be present in this sum.
#
# Example:
#
# [4, -1, 6, -2, 3, 5, -7, 7] -> 8
#      ^      ^         ^

def max_sum_between_two_negatives(arr):
    fl = 0
    n = 0
    res = []
    for x in arr:
        if x < 0:

            if fl:
                res.append(n)

                n = 0
            else:
                fl = 1
        else:
            if fl:
                n += x
                
    return max(res) if res else -1


print(max_sum_between_two_negatives([-1, 6, -2, 3, 5, -7]))
# print(max_sum_between_two_negatives([5, -1, -2]))
# print(max_sum_between_two_negatives([1, -2]))
# print(max_sum_between_two_negatives([-2, 7, 7, 1, 3, -5, -1, 3, 4, -6]))