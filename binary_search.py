# Please write a binary search function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.

import math


def binary_search(number, array):
    first = len(array) - 1
    last = 0
    index = -1
    while first >= last and index == -1:
        mid = int(math.floor((first+last) / 2.0))
        if array[mid] == number:
            index = mid
        elif array[mid] > number:
            first = mid -1
        else:
            last = mid + 1
    return index


array = [1,2,3,4,5,67,45,89,100]
print(binary_search(array=array, number=5))
print(binary_search(array=array, number=89))
print(binary_search(array=array, number=100))
print(binary_search(array=array, number=1))