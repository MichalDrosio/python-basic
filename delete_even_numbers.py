# Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].
def delete_even_numbers(array):
    new_array = []
    for i in array:
        if i % 2 != 0:
            new_array.append(i)
    return new_array


print(delete_even_numbers([5,6,77,45,22,12,24]))


array = [5,6,77,45,22,12,24]
new_array = [x for x in array if x % 2 != 0]
print(new_array)


