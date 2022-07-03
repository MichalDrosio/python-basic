import math


def binary_search(number, array):
    first = len(array) - 1
    last = 0
    index = -1

    while first >= last and index == -1:
        mid = (first+last) // 2

        print(f'traf:{array[mid]}(index:{mid}), szukana liczba:{number}')
        if array[mid] == number:
            index = mid
        elif array[first] == number:
            index = first
        elif array[last] == number:
            index = last
        elif array[mid] > number:
            first = mid - 1
        else:
            last = mid + 1
    return index


array = [1, 2, 3, 4, 5, 67, 45, 89, 100, 111, 123, 134, 135, 136, 137, 140, 141, 142, 143, 145, 146]


print(binary_search(array=array, number=100))



