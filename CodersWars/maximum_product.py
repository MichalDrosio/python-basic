# Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array.
#
# Notes
# Array/list size is at least 2.
#
# Array/list numbers could be a mixture of positives, negatives also zeroes .

def adjacent_element_product(array):
    i = 0
    max_num = None
    while i < len(array)-1:
        num = array[i] * array[i+1]
        i += 1
        if max_num == None or max_num < num:
            max_num = num

    return max_num

def adjacent_element_product2(array):
    return max( a*b for a, b in zip(array, array[1:]) )

# print(adjacent_element_product([1, 2, 3]))
print(adjacent_element_product2([9, 5, 10, 2, 24, -1, -48]))