import random


def bubble_sort(array):
    shift = True
    i = 0
    while i < len(array) - 1 and shift:
        j = 0
        shift = False
        while j < len(array) - 1 - i:
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                shift = True
            j += 1
        i += 1
        print(array)


