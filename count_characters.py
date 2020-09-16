# Please write a program which count and print the numbers of each character in a string input by console.

def count_character(words):
    dictionary = {}
    for i in words:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary


print(count_character(words=input('words:\n')))

