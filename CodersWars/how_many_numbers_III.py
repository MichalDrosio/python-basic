# We want to generate all the numbers of three digits where:
#
# the sum of their digits is equal to 10.
#
# their digits are in increasing order (the numbers may have two or more equal contiguous digits)
#
# The numbers that fulfill the two above constraints are: 118, 127, 136, 145, 226, 235, 244, 334
#
# Make a function that receives two arguments:
#
# the sum of digits value
#
# the desired number of digits for the numbers
#
# The function should output an array with three values: [1,2,3]
#
# 1 - the total number of possible numbers
#
# 2 - the minimum number
#
# 3 - the maximum number
#
# The example given above should be:

def find_all(sum_dig, digs):
    count_num = 0
    min_num = None
    max_num = None
    for num in range(1, 300):
        if len(str(num)) == digs:
            x = 0
            if '0' not in str(num):
                for n in str(num):
                        x += int(n)
                if x == sum_dig:
                    count_num += 1
                    if min_num == None or min_num > num:
                        min_num = num
                    if max_num == None or max_num < num:
                        max_num = num

    return count_num, min_num, max_num


print(find_all(10, 3))

from itertools import combinations_with_replacement

def find_all2(sum_dig, digs):
    combs = combinations_with_replacement(list(range(1, 10)), digs)
    target = [''.join(str (x) for x in list(comb)) for comb in combs if sum(comb) == sum_dig]
    print(target)
    if not target:
        return []
    return [len(target), int(target[0]), int(target[-1])]

print(find_all2(10, 3))

