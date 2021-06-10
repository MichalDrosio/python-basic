# Write a function which takes a input string s and return a string in the following way:

def sort_vowels(s):
    vowels = ('a', 'e', 'i', 'o', 'E', 'A', 'I', 'O')
    i = 0
    result = ''
    while i < len(s):
        if s[i] not in vowels:
            result += f'{s[i]}|\n'
            i += 1
        else:
            result += f'|{s[i]}\n'
            i += 1
    return result


print(sort_vowels('Codewars'))