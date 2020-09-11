# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the first 5 elements in the list.

def list_with_square_of_numbers(numbers):
    array = []
    for index in range(1, numbers+1):
        array.append(index ** 2)
    print(array[5:])


list_with_square_of_numbers(20)