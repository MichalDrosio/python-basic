# Write a program that accepts sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

def ar():
    array = []
    while True:
        a = input(':\n')
        if a:
            array.append(a.upper())
        else:
            break
    return array

def show():
    for i in ar():
        print(i)
show()