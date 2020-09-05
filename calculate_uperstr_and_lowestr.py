# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

def calculet_uper_and_lower(words):
    dictionary = {'upper': 0, 'lower': 0}
    for index in words:
        if index.isupper():
            dictionary['upper'] += 1
        elif index.islower():
            dictionary['lower'] += 1
        else:
            pass
    return dictionary


def show_dictionary():
    for key, value in calculet_uper_and_lower(words=input('words:\n')).items():
        print(f'{key}:{value}')

show_dictionary()


