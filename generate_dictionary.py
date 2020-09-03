# With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:

def generate_dictionary(num):
    d = {}
    for index in range(1, num+1):
        d[index] = index * index
    return d


def prict_dict():
    for k, v in generate_dictionary(5).items():
        print(f"{k}:{v}")

prict_dict()