# Write a program to compute the frequency of the words from the input.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1


def dict_data(words):
    dictionary = {}
    words = input('slowa:\n')
    word = words.split()
    for index in word:
        if index not in dictionary:
            dictionary[index] = 1
        else:
            dictionary[index] += 1
    return dictionary


def sorted_dict_by_value():
    d = dict_data(words='words')
    sorted_by_key = dict(sorted(d.items(), key=lambda t: t[1], reverse=True))
    return sorted_by_key


def sorted_dict_by_key():
    d = dict_data(words='words')
    sorted_by_key = dict(sorted(d.items(), key=lambda t: t[0],reverse=True))
    return sorted_by_key


def print_sorted_dict_by_value():
    for k, v in sorted_dict_by_value().items():
        print(f'{k}:{v}')


def print_sorted_dict_by_key():
    for k, v in sorted_dict_by_key().items():
        print(f'{k}:{v}')


print_sorted_dict_by_value()

print_sorted_dict_by_key()

