# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
# write a program to make a list whose elements are intersection of the above given lists.
def connection_two_list(array_1, array_2):
    array = [i for i in array_1 if i in array_2]
    return array


print(connection_two_list([1, 3, 6, 78, 35, 55], [12, 24, 35, 24, 88, 120, 155]))


array_1 = set([12, 24, 35, 24, 88, 120, 155])
array_2 = set([1, 3, 6, 78, 35, 55])

array_1 &= array_2
array = list(array_1)
print(array)




