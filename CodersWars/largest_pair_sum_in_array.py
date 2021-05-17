# Given a sequence of numbers, find the largest pair sum in the sequence.
#
# For example
#
# [10, 14, 2, 23, 19] -->  42 (= 23 + 19)
# [99, 2, 2, 23, 19]  --> 122 (= 99 + 23)

def largest_pair_sum(numbers):
    max_1 = max(numbers)
    numbers.remove(max_1)
    max_2 = max(numbers)
    return max_1 + max_2


print(largest_pair_sum([10,14,2,23,19]))