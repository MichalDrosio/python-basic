# By using list comprehension, please write a program to print the list after
# removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

array = [12,24,35,70,88,120,155]
new_array = [i for (i, x) in enumerate(array) if i % 2 != 0]
print(new_array)
