# Find the sum of the digits of all the numbers from 1 to N (both ends included).
#
# Examples
# # N = 4
# 1 + 2 + 3 + 4 = 10
#
# # N = 10
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46
#
# # N = 12
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51


def compute_sum(number):
    result = 0
    for num in range(1, number+1):
        if num < 10:
            result += num
        else:
            num_s = str(num)
            for n in num_s:
                result += int(n)

    return result

# print(compute_sum(12))

