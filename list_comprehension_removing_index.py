# By using list comprehension, please write a program to print the list after
# removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

def removing_numbers_by(array):
     array = [x for (i, x) in enumerate(array) if i not in (0,4,5)]
     return array

print(removing_numbers_by([12,24,35,70,88,120,155]))

li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
print(li)


def removing_numbers_by_index(array):
    array = [i for (i, x) in enumerate(array) if i not in (0, 4, 5)]
    return array

print(removing_numbers_by_index([12,24,35,70,88,120,155]))