# By using list comprehension, please write a program to print the list after
# removing the value 24 in [12,24,35,24,88,120,155].

def removing_value_from_array(array):
    array = [i for i in array if i != 24]
    return array

print(removing_value_from_array([12,24,35,24,88,120,155]))