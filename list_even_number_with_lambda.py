# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = map(lambda x: x**2, array)
array_squared = [i**2 for i in array]
print(list(squared_numbers))
print(array_squared)