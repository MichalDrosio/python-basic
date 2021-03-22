# Given a list of integers and a single sum value,
# return the first two values (parse from the left please) in order of appearance that add up to form the sum.
#
# sum_pairs([11, 3, 7, 5],         10)
# #              ^--^      3 + 7 = 10
# == [3, 7]
#
# sum_pairs([4, 3, 2, 3, 4],         6)
# #          ^-----^         4 + 2 = 6, indices: 0, 2 *
# #             ^-----^      3 + 3 = 6, indices: 1, 3
# #                ^-----^   2 + 4 = 6, indices: 2, 4
# #  * entire pair is earlier, and therefore is the correct answer
# == [4, 2]
#
# sum_pairs([0, 0, -2, 3], 2)
# #  there are no pairs of values that can be added to produce 2.
# == None/nil/undefined (Based on the language)
#
# sum_pairs([10, 5, 2, 3, 7, 5],         10)
# #              ^-----------^   5 + 5 = 10, indices: 1, 5
# #                    ^--^      3 + 7 = 10, indices: 3, 4 *
# #  * entire pair is earlier, and therefore is the correct answer
# == [3, 7]
# Negative numbers and duplicate numbers can and will appear.
#
# NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements.
# Be sure your code doesn't time out.

def sum_pairs(ints, s):
    z = []
    len_ints = ints
    for i in range(len(ints)):
        for j in range(len(ints[i:])):
            if i != j:
                if ints[i] + ints[j] == s:
                    if i + j == s:
                        z.append(ints[j])
                        z.append(ints[i])
                        return z
                    else:
                        len_array = ints[j: i+1]

                        if len(len_ints) >= len(len_array) and len(len_array) > 0:
                            len_ints = len_array
                            z.append(len_ints[0])
                            z.append(len_ints[-1])
                            return z




array1 = [1, 4, 8, 7, 3, 15]
array2 = [1, -2, 3, 0, -6, 1]
array3 = [20, -13, 40]

array5 = [10, 5, 2, 3, 7, 5]
array6 = [4, -2, 3, 3, 4]
array7 = [0, 2, 0]
array8 = [5, 9, 13, -3]

# print(sum_pairs(array1, 8))
# print(sum_pairs(array2, -6))
# print(sum_pairs(array3, -7))
# print(sum_pairs(array4, 2))
# print(sum_pairs(array5, 10))
# print(sum_pairs(array6, 8))
# print(sum_pairs(array7, 0))
# print(sum_pairs(array8, 10))

# def sum_pairs2(lst, s):
#     cache = set()
#     for i in lst:
#         print(i, end=', ')
#         if s - i in cache:
#             return [s - i, i]
#         cache.add(i)

# print(sum_pairs2(array1, 8))
# print(sum_pairs2(array2, -6))
# print(sum_pairs2(array3, -7))
# print(sum_pairs2(array4, 2))
# print(sum_pairs2(array5, 10))
# print(sum_pairs2(array6, 8))
# print(sum_pairs2(array7, 0))
# print(sum_pairs2(array8, 10))
