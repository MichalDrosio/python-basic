# Please write a program which accepts a string from console and print the characters that have even indexes.

def accept_even_index(words):
    array = []
    for i, x in enumerate(words):
        if i % 2 == 0:
            array.append(x)
    return array


print(accept_even_index(words=input()))


s = input()
s = s[::2]
print(s)