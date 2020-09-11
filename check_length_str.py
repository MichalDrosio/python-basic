# Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print al l strings line by line.


def two_stings_length(num1, num2):
    if len(num1) > len(num2):
        print(num1)
    elif len(num2) > len(num1):
        print(num2)
    else:
        print(f"{num1}\n{num2}")


print(two_stings_length(num1=input('num1:\n'), num2=input('num2:\n')))
