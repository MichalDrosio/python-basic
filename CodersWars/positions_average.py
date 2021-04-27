# Suppose you have 4 numbers: '0', '9', '6', '4' and 3 strings composed with them:
#
# s1 = "6900690040"
# s2 = "4690606946"
# s3 = "9990494604"
# Compare s1 and s2 to see how many positions they have in common: 0 at index 3, 6 at index 4, 4
# at index 8 ie 3 common positions out of ten.
#
# Compare s1 and s3 to see how many positions they have in common: 9 at index 1, 0 at index 3, 9
# at index 5 ie 3 common positions out of ten.
#
# Compare s2 and s3. We find 2 common positions out of ten.
#
# So for the 3 strings we have 8 common positions out of 30 ie 0.2666... or 26.666...%
#
# Given n substrings (n >= 2) in a string s our function pos_average will calculate the average percentage
# of positions that are the same between the (n * (n-1)) / 2 sets of substrings taken amongst the given n substrings.
# It can happen that some substrings are duplicate but since their ranks are not the same in s they
# are considered as different substrings.
#
# The function returns the percentage formatted as a float with 10 decimals but the result is tested at 1e.-9
# (see function assertFuzzy in the tests).
#
# Example:
# Given string s = "444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490" composing
# a set of n = 10 substrings (hence 45 combinations), pos_average returns 29.2592592593.
from itertools import permutations

def pos_average(s):
    arr = s.replace(' ', '').split(',')
    i = 0
    all = 0
    common = 0
    while i < len(arr)-1:
        j = i+1
        while j <= len(arr)-1:
            x = 0
            while x < len(arr[i]):
                all += 1
                if arr[i][x] == arr[j][x]:
                    common += 1
                x += 1
            j += 1
        i += 1
    return common / all * 100


# print(pos_average( "444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490"))
print(pos_average( "466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096"))



# def pos_average(s):
#     arr = s.replace(' ', '').split(',')
#     i = 0
#     common = 0
#     while i < len(arr)-1:
#         j = 0
#         while j < len(arr[i]):
#             if arr[i][j] == arr[i+1][j]:
#                 common += 1
#                 print(f'{arr[i]}:{arr[i][j]}, {arr[i + 1]}:{arr[i + 1][j]}')
#             j += 1
#         i += 1
#     print(common)

