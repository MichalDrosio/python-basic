# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

def remove_exclamation_marks(s):
    marks = ['!', '?']
    res = ''
    for i in s:
        if i not in marks:
            res += i
    return res

print(remove_exclamation_marks("Hello World!"))