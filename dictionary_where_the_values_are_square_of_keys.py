# Define a function which can print a dictionary where  the values are square of keys.

def dictionary_with_square(num):
    dictionary = {}
    for index in range(1, num+1):
        dictionary[index] = index ** 2
    print(dictionary)


print(dictionary_with_square(5))