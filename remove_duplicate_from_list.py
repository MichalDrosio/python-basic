# With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after
# removing all duplicate values with original order reserved.
def remove_duplicate_from_list(array):
    array_2 = []
    for i in array:
        if i not in array_2:
            array_2.append(i)
    return array_2


print(remove_duplicate_from_list([12,24,35,24,88,120,155,88,120,155]))


