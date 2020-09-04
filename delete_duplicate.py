# Write a program that accepts a sequence of whitespace separated words as input and
# prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

words = input('words:\n')

array = [word for word in words.split(' ')]
print(array)
array_2 = set(array)
print(sorted(array_2))