import random


def find_min(array):
    length_array = len(array)
    min_num = array[0]
    min_index = 0
    for i in range(length_array):
        if min_num > array[i]:
            min_num = array[i]
            min_index = i
    return min_index


def selection_sort(array):
    for i in range(len(array)):
        temp = array[i]
        min_index = find_min(array[i:]) + i
        print(min_index)
        array[i] = array[min_index]
        array[min_index] = temp
    return array


array = []
for x in range(10):
    array.append(random.randint(0, 100))

print(array)
print()
print('min z listy')
print(find_min(array))
print()
print('sorted list')
print(selection_sort(array))